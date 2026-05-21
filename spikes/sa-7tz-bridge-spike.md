# Spike: bridge-spike (sa-7tz)

End-to-end smoke test of the sandbox bridge dispatch path via the radrat polecat.

- **Bead:** sa-7tz
- **Polecat:** sandbox/polecats/radrat
- **Formula:** mol-polecat-work
- **Base branch:** main
- **Local ID:** 1779376290
- **Date:** 2026-05-21

## What this proves

Dispatch -> polecat assignment -> worktree -> commit -> `gt done` -> merge queue
path works end-to-end for the radrat polecat in the sandbox repo, mirroring the
earlier guzzle (sa-dj1) and rust-rig (sa-7oc) smoke tests.

## Notes

The bead carried no implementation contract; this file exists solely as a
verifiable artifact that the radrat polecat ran the formula and produced a
commit on a real branch via the bridge dispatch path.
