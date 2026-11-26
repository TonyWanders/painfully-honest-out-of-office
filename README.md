# The Painfully Honest Out-of-Office

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/TonyWanders/painfully-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/TonyWanders/painfully-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

One brutally honest but still polite out-of-office auto-reply, built for the
[make.fun bounty "The Painfully Honest Out-of-Office"](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
by Po Pu ($2, 10 places paid, ends Thu 26 Nov 2026 23:25 WAT).

## The entry

> I am out of the office because I finally admitted I was running on empty, so thank you for your patience while your email waits behind hundreds of unread messages until I feel human again.

One sentence, 188 characters, inside the 200 character limit. It admits the
truth most workers only say in private (running on empty, an inbox hundreds
deep), stays warm and professional (thank you for your patience), and lands
on a line worth quoting (until I feel human again).

## Run it

```sh
python3 main.py
```

`main.py` prints exactly the entry and writes the same text to
`/output/entry.txt`. It is deterministic: a fixed string, no randomness, no
clock, no input, so every run produces byte-identical output.

## License

MIT. See [LICENSE](LICENSE).
