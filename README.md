# secure-repo-baseline

A GitHub repository security baseline: the settings and files every project should have, with proof that they work.

## The baseline

| Control | Where it is configured | What it protects against |
|---|---|---|
| Security policy | `SECURITY.md` | Gives reporters a clear way to disclose vulnerabilities |
| Private vulnerability reporting | Settings, Advanced Security | Public disclosure of unfixed bugs |
| Code owners | `.github/CODEOWNERS` | Changes to files without the owner's review |
| CodeQL (default setup) | Settings, Advanced Security | Insecure code reaching the main branch |
| Dependency graph, Dependabot alerts and security updates | Settings, Advanced Security | Known-vulnerable dependencies |
| Secret scanning and push protection | Settings, Advanced Security | Passwords and tokens committed to the repo |
| Branch ruleset `protect-main` | Settings, Rulesets | Direct pushes, force pushes, branch deletion, and merging code with serious scan alerts |

## The `protect-main` ruleset

- Changes reach `main` only through a pull request.
- Force pushes and branch deletion are blocked.
- CodeQL results are required. Security alerts of High severity or higher, and error-level alerts, block the merge.
- The bypass list is empty, so the rules apply to the owner too.

## Proof: a blocked pull request

I opened a pull request containing a deliberately insecure file with an SQL injection and a command injection. CodeQL flagged the flaws and the ruleset blocked the merge. The pull request was closed without merging, so the file never reached `main`.

## Limitations

- This is a one-person repository, so required approvals are set to 0 (GitHub does not let you approve your own pull request). `CODEOWNERS` shows the pattern, but it cannot enforce a second reviewer here.
- CodeQL runs in default setup, which scans the languages GitHub detects. It does not replace manual review or dynamic testing.
- Repository settings and rulesets are not copied when someone uses this repo as a template, so the table above doubles as a checklist.
