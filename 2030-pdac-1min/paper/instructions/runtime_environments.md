# Runtime Environments (MacOS, Windows, Linux, Claude Code)

This file fixes the cross platform execution recipes for the future generated PDAC 1 minute simulation tree at 2030-pdac-1min/. The future Claude Code Opus 4.7 1M Max session reads this file to author the per platform Quick Start sections of the future generated README at 2030-pdac-1min/README.md and the cross platform CI matrix at .github/workflows/ci.yml.

## Supported Platforms

The future generated simulation runs on five supported platforms. The supported platforms are identical across all 32 iterations and are part of the deterministic seed contract.

| Platform | OS | CPU | GPU | RAM | Notes |
|----------|------|-----|-----|-----|-------|
| MacOS Apple Silicon | macOS 14 Sonoma or 15 Sequoia | M3 Ultra (24 core CPU, 60 core GPU) or M2 Ultra | Apple Silicon GPU via MLX | 64 to 192 GB unified | Primary development platform |
| Windows 11 | Windows 11 23H2 or later | Intel Core i9 14900K or AMD Ryzen 9 7950X3D | NVIDIA RTX 5090 or NVIDIA RTX 4090 | 64 to 128 GB | Secondary; uses WSL2 for Rust runner |
| Linux Ubuntu 22.04 LTS | Ubuntu 22.04 LTS or 24.04 LTS | Intel Xeon Platinum 8480+ or AMD EPYC 9654 | NVIDIA A100 80 GB or NVIDIA H100 80 GB | 256 to 1024 GB | Primary high throughput platform |
| Claude Code CLI | macOS / Linux / Windows | n/a (cloud) | n/a (cloud) | n/a (cloud) | Single command via claude code init |
| Claude Code Web | n/a (browser) | n/a (cloud) | n/a (cloud) | n/a (cloud) | Web app at claude.ai/code |

The Python 3.10, 3.11, and 3.12 lint and format gates run on all five platforms in CI.

## MacOS Apple Silicon Recipe

```
# install homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install python 3.12 via homebrew
brew install python@3.12 git rustup duckdb
rustup install stable
rustup default stable

# clone the repository
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-pdac-1min

# create the virtual environment
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]

# run a single iteration
python -m src.simulation.iterate_1min --seed 20260513 --iterations 1

# run the full 32 iteration sweep on MacOS Apple Silicon (approx 90 seconds per iteration)
python -m src.simulation.iterate_1min --seed 20260513 --iterations 32

# run the Rust high throughput runner
cd src/simulation
cargo run --release --bin runner_1min -- --seed 20260513 --iterations 32
```

MacOS Apple Silicon also supports the on premises LLM tournament backend via Ollama (recommended) or via Anthropic Claude Code (cloud). The Apple Silicon GPU acceleration uses MLX for the per arm sensor ingest and the per iteration aggregator.

## Windows 11 Recipe

The Windows 11 recipe uses WSL2 for the Rust runner because the Rust runner targets POSIX. The Python runner targets Windows natively.

```
# install python 3.12 from python.org or via winget
winget install Python.Python.3.12
winget install Git.Git
winget install Rustlang.Rustup
winget install DuckDB.cli

# clone the repository
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries\2030-pdac-1min

# create the virtual environment (Windows PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac]

# run a single iteration
python -m src.simulation.iterate_1min --seed 20260513 --iterations 1

# enable WSL2 if not already enabled (one time)
wsl --install -d Ubuntu-24.04

# run the Rust high throughput runner inside WSL2
wsl
cd /mnt/c/Users/<user>/robotic-surgeries/2030-pdac-1min/src/simulation
cargo run --release --bin runner_1min -- --seed 20260513 --iterations 32
```

NVIDIA RTX 5090 acceleration is available for the per iteration aggregator via CUDA 12 and via PyTorch 2.5 with the cu125 wheel.

## Linux Ubuntu 22.04 LTS Recipe (Server Grade, A100 or H100)

```
# install python 3.12 + rust + duckdb + CUDA 12 (Ubuntu 22.04)
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3-pip git build-essential pkg-config libssl-dev
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
# CUDA 12 install per NVIDIA documentation; verify with nvcc --version

# clone the repository
git clone https://github.com/kevinkawchak/robotic-surgeries.git
cd robotic-surgeries/2030-pdac-1min

# create the virtual environment
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,pdac,cuda]

# run the full 32 iteration sweep on a Xeon Platinum 8480+ + A100 80GB
python -m src.simulation.iterate_1min --seed 20260513 --iterations 32 --device cuda

# run the Rust high throughput runner (no GPU, multi-threaded CPU)
cd src/simulation
cargo run --release --bin runner_1min -- --seed 20260513 --iterations 32
```

The Linux server platform is the primary high throughput platform. The cross 32 iteration runtime budget is approximately 6.4 minutes on the Rust runner and 48 minutes on the Python runner.

## Claude Code CLI Recipe

```
# install claude code (one time)
npm install -g @anthropic/claude-code

# initialize a session at the project root
cd robotic-surgeries/2030-pdac-1min
claude code init

# Claude Code automatically sets up the Python virtual environment
# and runs the per iteration sweep on demand
```

Claude Code CLI supports the same Python 3.10 / 3.11 / 3.12 environments as the other platforms.

## Claude Code Web Recipe

Claude Code Web at claude.ai/code provides a browser based environment with no local installation. Open a new session at claude.ai/code, paste the GitHub URL https://github.com/kevinkawchak/robotic-surgeries, and the per iteration sweep runs in the cloud.

## CI Matrix (Future Generated)

The future Claude Code session authors the CI matrix at 2030-pdac-1min/.github/workflows/ci.yml (or extends the existing .github/workflows/ci.yml at the repository root). The matrix runs ruff format --check, ruff check, and yamllint -d relaxed on Python 3.10, 3.11, and 3.12 on Ubuntu 22.04 LTS. The matrix is identical to the v3.9.1 GBM CI matrix and continues to pass on this PR because the PDAC instruction files are Markdown only and not subject to the Python lint and format gates.

## Cross References

- ci_compliance_checklist.md fixes the lint and format gates.
- pr_workflow.md fixes the nine commit pattern.
- file_format_conventions.md fixes the file format defaults.
- commit_07_repository_updates.md fixes the future generated README cross platform Quick Start.
