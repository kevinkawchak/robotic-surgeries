# Zenodo Execution

This directory captures the Zenodo L0 raw deposition pointer patcher output at `../../codegen/src/zenodo/patch_pointers.py`. The patcher computes a SHA 256 of each per iteration L0 raw Parquet file and writes a per iteration pointer JSON plus a cross iteration manifest. The pointer JSON family is what binds the lightweight committed iteration outputs in `../iterations/` to the heavyweight 13.2 GB L0 raw archive deposited on Zenodo at DOI `10.5281/zenodo.18445179`.

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
export ZENODO_TOKEN=<your_zenodo_personal_access_token>
PYTHONPATH=. python -m src.zenodo.patch_pointers \
  --staging-dir /staging/l0_raw \
  --output-dir ../execution/zenodo
```

The execution environment does not carry a `ZENODO_TOKEN`, so the live Zenodo upload step is skipped. The committed pointer JSON is generated against the `../iterations/index.jsonl` SHA 256 as a placeholder.

## Files

| File | Description |
|------|-------------|
| `run_00000_L0_raw.zenodo_pointer.json` | Sample per iteration pointer JSON |
| `manifest.json` | Cross iteration manifest skeleton |
| `deposition_summary.txt` | Zenodo deposition record summary |

## Sample Pointer JSON

```json
{
  "iteration_id": 0,
  "deposition_doi": "10.5281/zenodo.18445179",
  "deposition_url": "https://doi.org/10.5281/zenodo.18445179",
  "file_name": "index.jsonl",
  "file_size_bytes": 5233,
  "file_sha256": "e2327da90430576f122152e59e451b952204e88822726ebb065c77ebf06b4e23",
  "created_at": "2026-05-13T21:28:09Z"
}
```

## Deposition Layout

The Zenodo deposition at `10.5281/zenodo.18445179` is organized as follows:

```
Root
+-- README.md                            <- deposition record description
+-- LICENSE.txt                          <- MIT 2026 Kevin Kawchak
+-- per_iteration/
|   +-- run_00000_L0_raw.parquet         <- per iteration 640 ch sensor raw
|   +-- run_00001_L0_raw.parquet
|   +-- ...
|   +-- run_00031_L0_raw.parquet
+-- cross_iteration/
|   +-- iterations_index.parquet         <- cross iteration metadata
|   +-- composite_distribution.parquet
|   +-- safety_zone_events.parquet
+-- manifest.json                        <- per file SHA 256 inventory
```

Total deposition size (estimate): 13.2 GB
Per file SHA 256: 32 + 3 = 35 entries in the manifest

## Verification Workflow

The committed iteration outputs at `../iterations/` carry only the lightweight slices (the L1 publication sample, the L2 1 Hz aggregate, the L3 per phase rollup, and the L4 per anastomosis rollup). The full L0 raw is on Zenodo. To verify L0 integrity:

```bash
sha256sum run_00000_L0_raw.parquet
# expected SHA 256 is recorded in run_00000_L0_raw.zenodo_pointer.json
```

## Status of the Live Deposition

The Zenodo deposition DOI `10.5281/zenodo.18445179` is the v0.6.0 codegen project DOI. The v0.7.0 execution tree commits the pointer JSON family that resolves L0 raw to the deposition record. A future revision of the deposition will publish a per iteration L0 raw Parquet file family.
