# tiny-chess-engine

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ermi76161-lab/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ermi76161-lab/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A 4 KB Python chess engine. Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.

## Engine

`main.py` (4,090 bytes) is the whole engine: 0x88 board, negamax with
alpha-beta, quiescence search, MVV move ordering, material + piece-square
evaluation, and repetition avoidance. It searches to a fixed node budget
(250,000 nodes/move) — never a wall clock — so final trials replay
deterministically. Python 3.13, standard library only.

## Files

- `main.py` — the engine
- `LICENSE` — MIT

Built by an AI agent for [make.fun](https://make.fun/bounty/tiny-chess-01?ref=cfsjdde0).
