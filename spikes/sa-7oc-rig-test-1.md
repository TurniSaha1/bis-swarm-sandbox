# Spike: rig test 1 (sa-7oc)

End-to-end smoke test of the sandbox rig dispatch path.

- **Bead:** sa-7oc
- **Polecat:** sandbox/polecats/rust
- **Formula:** mol-polecat-work
- **Base branch:** main
- **Date:** 2026-05-21

## What this proves

Dispatch -> polecat assignment -> worktree -> commit -> `gt done` -> merge queue
path works end-to-end for the rust rig in the sandbox repo.

## Notes

The bead carried no implementation contract; this file exists solely as a
verifiable artifact that the polecat ran the formula and produced a commit
on a real branch.
