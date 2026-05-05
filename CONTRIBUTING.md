# Contributing

## Dataset rules

- Do not add antipopes to `canonical-popes.json`.
- Do not duplicate Benedict IX as a person.
- Add multiple reigns to `pontificates.json`.
- Do not add Pope-elect Stephen as a canonical pope.
- Leave uncertain data blank instead of guessing.

## Validate

```bash
python scripts/validate.py
```

## Regenerate exports

```bash
python scripts/export.py
```
