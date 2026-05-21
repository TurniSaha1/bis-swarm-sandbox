# Spike: no boot test (sa-a5s)

End-to-end smoke test of the sandbox dispatch path via the fury polecat.

- **Bead:** sa-a5s
- **Polecat:** sandbox/polecats/fury
- **Formula:** mol-polecat-work
- **Base branch:** main
- **Convoy:** hq-cv-kf2rk
- **Date:** 2026-05-21

## What this proves

Dispatch -> polecat assignment -> worktree -> commit -> `gt done` -> merge queue
path works end-to-end for the fury rig in the sandbox repo, mirroring the
earlier rust-rig (sa-7oc) and guzzle-rig (sa-dj1) smoke tests.

## Notes

The bead carried no implementation contract; this file exists solely as a
verifiable artifact that the fury polecat ran the formula and produced a
commit on a real branch via the dispatch path.
