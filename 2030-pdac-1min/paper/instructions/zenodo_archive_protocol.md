# Zenodo Archive Protocol (PDAC 1 Minute Variant)

This file fixes the Zenodo archive protocol for the PDAC 1 minute variant L0 raw deposition. The future Claude Code Opus 4.7 1M Max session reads this file to author the per iteration L0 pointer JSON files at 2030-pdac-1min/data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json, the cross iteration manifest at 2030-pdac-1min/releases/v0.5.0/manifest.json, and the Zenodo deposition script at 2030-pdac-1min/src/zenodo/patch_pointers.py.

## Why Zenodo Deposition

The full L0 raw sensor stream is 412 MB per iteration and 13.2 GB across 32 iterations. The GitHub single file commit cap is 10 MB and the GitHub repository total size soft cap is 1 GB. The L0 raw therefore cannot be committed to Git and must be archived externally. Zenodo (CERN's open access research data archive) is the canonical archive for this work because it issues a persistent DOI per deposition, supports up to 50 GB per deposition, supports SHA 256 manifest verification, and is freely accessible to all researchers worldwide.

## Deposition Layout

The PDAC 1 minute L0 deposition uses the existing repository DOI 10.5281/zenodo.18445179 (parent repository) with a new versioned sub deposition for v0.5.0. The deposition layout is:

```
Zenodo deposition: 10.5281/zenodo.18445179 (parent repository)
  + v0.5.0 sub deposition (new DOI to be assigned, e.g. 10.5281/zenodo.NNNNNNNN)
    + manifest.json (cross iteration manifest with SHA 256 per file)
    + L0_raw_iterations/
        run_00000_L0_raw.parquet (412 MB)
        run_00001_L0_raw.parquet (412 MB)
        ...
        run_00031_L0_raw.parquet (412 MB)
    + README.md (publication grade README for the deposition)
    + LICENSE.txt (CC BY 4.0 for data; MIT for code references)
```

The cross iteration L0 raw total is 13.2 GB. The deposition includes a manifest.json file with SHA 256 per file and a README.md file with the publication grade DOI badges, deposition description, file inventory, and citation block.

## Per Iteration L0 Pointer JSON Schema

Each per iteration L0 raw file is referenced from a pointer JSON at 2030-pdac-1min/data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json. The pointer JSON schema is:

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "zenodo_pointer.schema.json",
  "type": "object",
  "required": ["iteration_id", "deposition_doi", "deposition_url", "file_name", "file_size_bytes", "file_sha256", "created_at"],
  "properties": {
    "iteration_id": {"type": "integer", "minimum": 0, "maximum": 31},
    "deposition_doi": {"type": "string", "pattern": "^10.5281/zenodo.\\d+$"},
    "deposition_url": {"type": "string", "format": "uri"},
    "file_name": {"type": "string"},
    "file_size_bytes": {"type": "integer"},
    "file_sha256": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "created_at": {"type": "string", "format": "date-time"}
  }
}
```

The pointer JSON file is approximately 0.5 KB per iteration and is committed to Git. The pointer JSON file does not contain the L0 raw data; it contains the SHA 256 manifest entry and the URL to download the L0 raw from Zenodo.

## Cross Iteration Manifest Schema

The cross iteration manifest at 2030-pdac-1min/releases/v0.5.0/manifest.json aggregates the 32 per iteration pointer JSON files into a single manifest. The manifest schema is:

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "manifest.schema.json",
  "type": "object",
  "required": ["release_version", "release_date", "deposition_doi", "deposition_url", "iterations"],
  "properties": {
    "release_version": {"type": "string", "const": "v0.5.0"},
    "release_date": {"type": "string", "format": "date"},
    "deposition_doi": {"type": "string", "pattern": "^10.5281/zenodo.\\d+$"},
    "deposition_url": {"type": "string", "format": "uri"},
    "iterations": {
      "type": "array",
      "items": {"$ref": "zenodo_pointer.schema.json"},
      "minItems": 32,
      "maxItems": 32
    }
  }
}
```

The manifest.json file is approximately 16 KB and is committed to Git.

## Zenodo Patch Pointer Script

The future Claude Code session authors the Zenodo patch pointer script at 2030-pdac-1min/src/zenodo/patch_pointers.py. The script reads the 32 per iteration L0 raw Parquet files from a local staging directory, uploads them to Zenodo via the Zenodo REST API, retrieves the per file SHA 256 from the Zenodo response, and writes the per iteration pointer JSON files plus the cross iteration manifest. The script supports the ZENODO_TOKEN environment variable for authentication.

## CC BY 4.0 License

The Zenodo L0 raw deposition is distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). The license text is included in the deposition README.md and at the top of the manifest.json.

## Cross References

- file_size_pyramid_1min.md fixes the L0 raw budget that this protocol archives.
- chunking_strategy.md fixes the L0 raw chunking pattern.
- commit_04_iterations_1min.md fixes the per iteration sweep that produces the L0 raw.
- commit_07_repository_updates.md fixes the v0.5.0 release notes that reference this deposition.
