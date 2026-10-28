# fedramp-cpo

Maintain the FedRAMP **Certification Package Overview (CPO)** as Markdown. On merge to `main`, GitHub Actions validates it against the official FedRAMP schema and commits the generated JSON.

| Path | Purpose |
| --- | --- |
| `cpo/template.md` | Standard blank-ish template with every schema field, `(required)` markers, and allowed values. Copy it to start; CI keeps it schema-valid. |
| `cpo/cpo.md` | **Edit this.** YAML frontmatter holds structured fields; the Markdown body is the service description. |
| `cpo/cpo.json` | Generated. Do not edit by hand. |
| `schema/` | Vendored FedRAMP schemas (`2026-06-24`) that `cpo.json` is validated against. |
| `scripts/build_cpo.py` | Markdown → JSON converter and validator. |
| `scripts/check_schema.py` | Confirms `schema/` matches what fedramp.gov publishes and that FedRAMP's rules still reference the pinned CPO schema version. |
| `.github/workflows/build-cpo-json.yml` | PRs: validate. Push to `main`: validate, regenerate, commit `cpo/cpo.json`. |

## Format

Frontmatter keys mirror the schema (`serviceIdentification`, `serviceProperties`, `contactInformation`, `assessor`, `advisors`, `certifiedServices`, `thirdPartyInformationResources`). Two additions cover rule `CPO-CSO-MTD`:

- `metadata.version` and `metadata.responsibleOfficial` (name, title, contact) are written by you.
- `metadata.lastUpdated` and `metadata.updateSource` (file and commit SHA) are generated from git.

Empty strings are dropped from the output, so optional fields can be left blank.

## Manual builds

**Locally:**

```sh
make build   # validate and regenerate cpo/cpo.json
make check   # validate cpo.md and the template only
make check-schema   # compare vendored schemas to fedramp.gov
```

**On GitHub:** Actions → *Build CPO JSON* → *Run workflow*, pick a branch, and leave *commit* checked to push the regenerated `cpo.json` to that branch, or uncheck it to only validate.

## Which schema is used

`cpo.json` is validated against the FedRAMP Certification Package Overview schema dated `2026-06-24` (the version referenced by FedRAMP's official `fedramp-consolidated-rules.json`) and records it in a top-level `$schema` property. The *Check FedRAMP schema* workflow runs weekly and on schema changes, and fails if the vendored copies drift from fedramp.gov or FedRAMP moves to a newer version.

## Upgrading the schema

Download the new `fedramp-certification-package-overview-schema-*.json` and `fedramp-common-definitions-schema-*.json` into `schema/`, remove the old ones, and update `CPO_SCHEMA` in `scripts/build_cpo.py`.

## Repo settings

The workflow pushes to `main` with `GITHUB_TOKEN`. If `main` is protected, allow `github-actions[bot]` to bypass the rule (or switch the commit step to open a PR). The `[skip ci]` message and the path filter keep the bot commit from re-triggering the workflow.
