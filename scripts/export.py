import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def write_csv(name, records):
    with open(DATA / name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)

def yaml_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    return json.dumps("" if v is None else v, ensure_ascii=False)

def write_yaml(name, records):
    lines = []
    for r in records:
        first = True
        for k, v in r.items():
            lines.append(("- " if first else "  ") + f"{k}: {yaml_value(v)}")
            first = False
    (DATA / name).write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    people = load("canonical-popes.json")
    pontificates = load("pontificates.json")
    antipopes = load("antipopes.json")

    (DATA / "canonical-popes.txt").write_text("\n".join(p["papal_name"] for p in people) + "\n", encoding="utf-8")
    (DATA / "canonical-pontificates.txt").write_text("\n".join(p["papal_name"] for p in pontificates) + "\n", encoding="utf-8")
    (DATA / "antipopes.txt").write_text("\n".join(a["claimant_name"] for a in antipopes) + "\n", encoding="utf-8")

    write_csv("canonical-popes.csv", people)
    write_csv("pontificates.csv", pontificates)
    write_csv("antipopes.csv", antipopes)

    write_yaml("canonical-popes.yaml", people)
    write_yaml("pontificates.yaml", pontificates)
    write_yaml("antipopes.yaml", antipopes)

    print("Exports regenerated")

if __name__ == "__main__":
    main()
