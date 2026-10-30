# North Carolina: law history in git

The statute law of North Carolina as a git repository: one file per section, committed with the official publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of North Carolina | 14 | Internet Archive captures, 2022 to 2026 |
| `chapter-14/` | General Statutes chapter 14: Criminal Law | 5 | Captures of 2019, 2021, 2023, 2025, 2026 |
| `chapter-55/` | General Statutes chapter 55: North Carolina Business Corporation Act | 4 | Captures of 2021, 2023, 2025, 2026 |
| `chapter-42/` | General Statutes chapter 42: Landlord and Tenant | 4 | Captures of 2021, 2023, 2025, 2026 |

Nothing else of North Carolina's law is in it yet.

## Where the text comes from

Only section headings and text are taken; the history notes in brackets are left out.

## Dates

A version is dated by the day the Internet Archive captured the page, not by the day a change took effect. Only a sample of captures is used (the Constitution: first, middle and last per article; chapters: one per year from 2019 and the last), so a change shown on one date may have happened earlier.

## What it does not show

- Changes are credited to the capture, not to the act that made them.
- The Constitution's articles were captured on different days; each version uses each article's latest sampled capture on or before its date.
- Only the Constitution and chapters 14, 42 and 55 are included.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher (North Carolina General Assembly) because this first build holds one version of each act, the oldest version available. The committer is always Lexifina.
