# Spike: existing polecat target test (sa-oxt)

End-to-end smoke test of the sandbox dispatch path via the dust polecat.

- **Bead:** sa-oxt
- **Polecat:** sandbox/polecats/dust
- **Formula:** mol-polecat-work
- **Base branch:** main
- **Date:** 2026-05-21

## What this proves

Dispatch -> polecat assignment -> worktree -> commit -> `gt done` -> merge queue
path works end-to-end for the dust rig in the sandbox repo, extending the
prior rust (sa-7oc) and guzzle (sa-dj1) smoke tests to an existing polecat
target.

## Notes

The bead carried no implementation contract; this file exists solely as a
verifiable artifact that the dust polecat ran the formula and produced a
commit on a real branch via the bridge dispatch path.
