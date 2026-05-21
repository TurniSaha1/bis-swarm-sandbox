# Spike: bridge-spike (sa-dj1)

End-to-end smoke test of the sandbox bridge dispatch path via the guzzle polecat.

- **Bead:** sa-dj1
- **Polecat:** sandbox/polecats/guzzle
- **Formula:** mol-polecat-work
- **Base branch:** main
- **Local ID:** 1779375913244
- **Date:** 2026-05-21

## What this proves

Dispatch -> polecat assignment -> worktree -> commit -> `gt done` -> merge queue
path works end-to-end for the guzzle rig in the sandbox repo, mirroring the
earlier rust-rig smoke test (sa-7oc).

## Notes

The bead carried no implementation contract; this file exists solely as a
verifiable artifact that the guzzle polecat ran the formula and produced a
commit on a real branch via the bridge dispatch path.
