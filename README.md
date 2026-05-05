# Roman Catholic Popes Dataset

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![DOI](https://zenodo.org/badge/671685469.svg)](https://doi.org/10.5281/zenodo.20044659)

A structured, open dataset of Roman Catholic popes, canonical pontificate records, and antipopes.

This repository is designed for historical reference, Catholic reference tools, timelines, APIs, research notes, and educational projects.

## Dataset files

| File | Description |
|---|---|
| `data/canonical-popes.json` | Canonical pope person records. |
| `data/pontificates.json` | Canonical pontificate records. Benedict IX has three records. |
| `data/antipopes.json` | Antipope claimant records separated from the canonical list. |
| `data/canonical-popes.csv` | CSV export of canonical pope person records. |
| `data/pontificates.csv` | CSV export of canonical pontificate records. |
| `data/antipopes.csv` | CSV export of antipope records. |
| `data/canonical-popes.txt` | Plain text canonical person list. |
| `data/canonical-pontificates.txt` | Plain text canonical pontificate list. |
| `data/antipopes.txt` | Plain text antipope list. |

## Counts

- Canonical pope person records: **265**
- Canonical pontificate records: **267**
- Antipope records: **41**
- Current pope: **Leo XIV**

## Modeling approach

The dataset separates:

1. canonical pope people
2. canonical pontificate records
3. antipope claimant records

This allows historically difficult cases to be modeled cleanly.

Benedict IX appears once in `canonical-popes.json`, but three times in `pontificates.json`.

Benedict X is excluded from the canonical pope files and included in `antipopes.json`.

## Validation

```bash
python scripts/validate.py
```

## Export regeneration

```bash
python scripts/export.py
```

## License

CC0-1.0.
