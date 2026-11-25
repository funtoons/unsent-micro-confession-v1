# Unsent: The Micro-Confession Sprint

[![Bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/funtoons/unsent-micro-confession-v1/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/funtoons/unsent-micro-confession-v1/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for the [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) bounty on make.fun.

## The entry

```text
To: Dad
I sold the watch you gave me for graduation to pay rent in March and I still check the pawn shop window every time I pass it.
```

## How it works

`main.py` (Python standard library only, offline, deterministic) writes the
fixed two-part confession above to `/output/entry.txt`. The program asserts
the competition gate before writing: the entry is 1–260 characters, has
exactly two parts (a `To:` line and one message line), the message is at most
200 characters, and there is no explanation after it.

Run it with:

```sh
python3 main.py
```

## Why it fits the judge's criteria

- **Two parts, nothing else.** A `To:` line naming who it was meant for,
  then the unsent line itself, one line, exactly as typed.
- **The reason it stayed in drafts is felt, not stated.** Shame and fear
  are in the words: he sold a graduation gift to pay rent, and months later
  he still checks the pawn shop window every time he passes it — he cannot
  undo it and cannot bring himself to tell his father.
- **The `To:` line and the message need each other.** The watch was a gift
  from Dad; swap the addressee and the confession falls apart.
- **It reads as typed and never sent.** A specific, honest admission
  (graduation watch, March rent, pawn shop window), not a joke, greeting,
  or motivational line.
