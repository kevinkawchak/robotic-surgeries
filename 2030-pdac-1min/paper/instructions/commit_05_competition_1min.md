# Commit 5: Competition (Four Entrant Tournament)

This file fixes the Future Commit 5 file list and authoring instructions for the four entrant multi vendor LLM tournament.

## Commit 5 File List

The future Commit 5 emits the following files at 2030-pdac-1min/.

| File | Purpose | Approx size |
|------|---------|-------------|
| src/llm/compare_agent_1min.py | LLM tournament agent with four backend support | 14 KB |
| src/llm/__init__.py | Package marker | 0.1 KB |
| prompts/comparison_prompt_1min.md | Versioned LLM tournament prompt | 6 KB |
| prompts/daraxonrasib_advisory_prompt.md | Versioned LLM advisory prompt for Daraxonrasib restart timing | 5 KB |
| results/comparison.json | Cross iteration tournament results in JSON | 200 KB |
| results/comparison_report.md | Publication grade cross iteration leaderboard | 18 KB |
| results/comparison_report.pdf | Same as md, rendered to PDF via pandoc | 800 KB |
| outputs/comparison/leaderboard.csv | Per entrant per round per iteration leaderboard | 80 KB |
| outputs/comparison_robot_vs_human/leaderboard.csv | Same but Round 3 only (robot vs human) | 20 KB |

## Commit 5 Authoring Order

1. Generate src/llm/compare_agent_1min.py with four backend support (Ollama, vLLM, Anthropic Opus, Anthropic Sonnet) and the four entrant tournament format.
2. Generate prompts/comparison_prompt_1min.md as the versioned LLM tournament prompt with frozen composite weights, structural caveat, and per round inputs.
3. Generate prompts/daraxonrasib_advisory_prompt.md as the versioned LLM advisory prompt for the postoperative Daraxonrasib restart timing per the trajectory in daraxonrasib_integration.md.
4. Generate results/comparison.json by running the LLM tournament agent across all 32 iterations and all 4 rounds (128 round results).
5. Generate results/comparison_report.md as the publication grade cross iteration leaderboard with per entrant mean composite score, 95 percent confidence interval, win rate, total wins, per entrant component breakdown, and the structural caveat.
6. Generate results/comparison_report.pdf by rendering comparison_report.md to PDF via pandoc with the same style as the v3.9.1 GBM comparison_report.pdf.
7. Generate outputs/comparison/leaderboard.csv and outputs/comparison_robot_vs_human/leaderboard.csv as the per round per iteration cross entrant CSV.

## Per Iteration Tournament Results Schema

The per iteration tournament results are recorded in results/comparison.json with the following schema:

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "comparison.schema.json",
  "type": "object",
  "required": ["iterations", "leaderboard"],
  "properties": {
    "iterations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["iteration_id", "seed", "rounds"],
        "properties": {
          "iteration_id": {"type": "integer", "minimum": 0, "maximum": 31},
          "seed": {"type": "integer"},
          "rounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["round", "entrant_a", "entrant_b", "entrant_a_composite", "entrant_b_composite", "winner", "confidence", "rationale", "caveats"],
              "properties": {
                "round": {"type": "integer", "minimum": 1, "maximum": 4},
                "entrant_a": {"type": "string"},
                "entrant_b": {"type": "string"},
                "entrant_a_composite": {"type": "number"},
                "entrant_b_composite": {"type": "number"},
                "winner": {"type": "string"},
                "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                "rationale": {"type": "string"},
                "caveats": {"type": "array", "items": {"type": "string"}}
              }
            },
            "minItems": 4,
            "maxItems": 4
          }
        }
      },
      "minItems": 32,
      "maxItems": 32
    },
    "leaderboard": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entrant", "composite_mean", "composite_ci_low", "composite_ci_high", "win_rate", "total_wins"],
        "properties": {
          "entrant": {"type": "string"},
          "composite_mean": {"type": "number"},
          "composite_ci_low": {"type": "number"},
          "composite_ci_high": {"type": "number"},
          "win_rate": {"type": "number", "minimum": 0, "maximum": 1},
          "total_wins": {"type": "integer"}
        }
      },
      "minItems": 4,
      "maxItems": 4
    }
  }
}
```

## Cross References

- competition_protocol.md fixes the four entrant tournament format.
- commit_04_iterations_1min.md fixes the 32 iteration sweep that the tournament consumes.
- robot_specification_pancrespeed.md fixes the PancreSpeed 1.0 entrant.
- daraxonrasib_integration.md fixes the Daraxonrasib advisory prompt.
