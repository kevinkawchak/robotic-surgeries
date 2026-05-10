"""Patch every Zenodo pointer JSON file in the v3.9.1 1-minute output tree
with the real DOI, record_id, and SHA-256 values returned by the Zenodo API.
"""

from __future__ import annotations

import json
from pathlib import Path

import click


def patch_pointer(pointer_path: Path, doi: str, record_id: str, sha256: str) -> None:
    data = json.loads(pointer_path.read_text(encoding="utf-8"))
    data["zenodo_doi"] = doi
    data["zenodo_record_id"] = record_id
    data["sha256"] = sha256
    pointer_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


@click.command()
@click.option("--record-id", required=True)
@click.option("--doi", required=True)
@click.option("--manifest", type=click.Path(exists=True), required=True)
@click.option("--root", type=click.Path(exists=True), default="2030-gbm-1min")
def cli(record_id: str, doi: str, manifest: str, root: str) -> None:
    manifest_data = json.loads(Path(manifest).read_text(encoding="utf-8"))
    sha_lookup = {f["filename"]: f["sha256"] for f in manifest_data.get("files", [])}
    patched = 0
    for pointer in Path(root).rglob("*.zenodo_pointer.json"):
        data = json.loads(pointer.read_text(encoding="utf-8"))
        filename = data.get("zenodo_filename") or data.get("zenodo_filename_pattern")
        sha = sha_lookup.get(filename, "PLACEHOLDER")
        patch_pointer(pointer, doi, record_id, sha)
        patched += 1
    print(json.dumps({"patched": patched, "doi": doi, "record_id": record_id}))


if __name__ == "__main__":
    cli()
