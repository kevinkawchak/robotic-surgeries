#!/usr/bin/env bash
# ======================================================================
# build_zip.sh - Build the Overleaf-ready LaTeX Source Files.zip from
# the LaTeX sources in this directory.
#
# Run from this directory:
#
#   chmod +x build_zip.sh
#   ./build_zip.sh
#
# Produces 'LaTeX Source Files.zip' in the current working directory.
# Tested on Linux (Ubuntu 22.04 LTS), MacOS (Apple Silicon), and Git
# Bash on Windows 11.
# ======================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Sanity checks.
for f in main.tex new_paper.sty references.bib; do
  if [ ! -f "$f" ]; then
    echo "Missing required file: $f" >&2
    exit 1
  fi
done
if [ ! -d "sections" ]; then
  echo "Missing required directory: sections/" >&2
  exit 1
fi

OUTPUT_ZIP="LaTeX Source Files.zip"
rm -f "$OUTPUT_ZIP"

# Use python zipfile when zip is missing (covers minimal environments).
if command -v zip >/dev/null 2>&1; then
  zip -r "$OUTPUT_ZIP" main.tex new_paper.sty references.bib sections/
elif command -v python3 >/dev/null 2>&1; then
  python3 -c "
import os, zipfile
with zipfile.ZipFile('LaTeX Source Files.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for f in ['main.tex', 'new_paper.sty', 'references.bib']:
        z.write(f)
    for root, _, files in os.walk('sections'):
        for f in files:
            z.write(os.path.join(root, f))
print('Wrote LaTeX Source Files.zip via python3 zipfile')
"
else
  echo "Neither 'zip' nor 'python3' is available; install one and re-run." >&2
  exit 1
fi

echo ""
echo "Built: $SCRIPT_DIR/$OUTPUT_ZIP"
echo "Upload this file to Overleaf via 'New Project -> Upload Project'."
