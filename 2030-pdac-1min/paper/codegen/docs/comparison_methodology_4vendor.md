# Comparison Methodology Overview (4 Entrant Multi Vendor Tournament)

This document fixes the 4 entrant multi vendor LLM tournament methodology. The full protocol lives at `../../instructions/competition_protocol.md` and the agent lives at `src/llm/compare_agent_1min.py`.

## Four Entrants

| Entrant | Type | Notes |
|---------|------|-------|
| PancreSpeed 1.0 (hypothetical 2030 Medtronic) | Robot | 8 arm, 100 kHz force, 10 kHz cmd, 3 ms e stop |
| da Vinci Whipple 2030 (hypothetical Intuitive successor) | Robot | 6 arm, 50 kHz force, 5 kHz cmd, 5 ms e stop |
| Hugo PDAC 2030 (hypothetical Medtronic Hugo successor) | Robot | 6 arm modular cart, 30 kHz force, 3 kHz cmd, 8 ms e stop |
| Dutch Cohort 1000 (2025 nationwide human surgeon baseline) | Human | mean operative time 5.4 hours, mean ideal outcome rate 47 percent |

## Frozen Composite Score Weights

| Component | Weight | PancreSpeed 1.0 target | da Vinci 2030 target | Hugo PDAC 2030 target | Dutch human target |
|-----------|--------|------------------------|----------------------|------------------------|---------------------|
| Quality | 0.30 | 95 | 88 | 85 | 82 |
| Time | 0.20 | 100 | 78 | 70 | 8 |
| Cost | 0.15 | 80 | 70 | 75 | 90 |
| Safety | 0.15 | 96 | 90 | 86 | 80 |
| Patient experience | 0.05 | 92 | 88 | 84 | 78 |
| Anastomosis quality | 0.15 | 95 | 90 | 87 | 82 |
| Composite total | 1.00 | 93.55 | 84.10 | 80.60 | 56.05 |

## Per Round Format

The tournament runs 4 rounds per iteration. Each round is a pairwise comparison; the per round winner is the entrant with the higher per round composite score.

| Round | Entrant A | Entrant B | Comparison |
|-------|-----------|-----------|------------|
| 1 | PancreSpeed 1.0 | da Vinci Whipple 2030 | Modern vs prior generation top platform |
| 2 | PancreSpeed 1.0 | Hugo PDAC 2030 | Modern vs prior generation modular |
| 3 | PancreSpeed 1.0 | Dutch human baseline | Modern vs current human (structural time caveat) |
| 4 | da Vinci 2030 | Hugo PDAC 2030 | Cross competitor benchmark |

Across 32 iterations the cross round expected outcome is PancreSpeed 1.0 wins Rounds 1, 2, and 3 with confidence above 0.9. Round 4 is approximately a coin flip estimated at 60 percent da Vinci 2030 wins.

## Structural Caveat

Round 3 compares a 1 minute robot run against a 5.4 hour human baseline. The structural time dimension caveat is preserved in every per round rationale and in the cross iteration leaderboard.

## On Prem LLM Backends

| Backend | Model | Use case |
|---------|-------|----------|
| Ollama | Llama 3.3 70B Instruct | Default on premises, low latency |
| vLLM | Llama 3.3 70B Instruct or DeepSeek V3 | High throughput on premises |
| Anthropic Claude | claude-opus-4-7 (1M context) | Cloud, PHI cleared, full context |
| Anthropic Claude | claude-sonnet-4-6 | Cloud, PHI cleared, faster |

The backend is selected via the `COMPARE_AGENT_BACKEND` environment variable.

## Cross References

- `../../instructions/competition_protocol.md` fixes the 4 entrant tournament protocol.
- `../../instructions/commit_05_competition_1min.md` fixes the per round format.
- `../../instructions/commit_04_iterations_1min.md` fixes the 32 iteration sweep input.
