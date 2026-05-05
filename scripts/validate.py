import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def main():
    people = load("canonical-popes.json")
    pontificates = load("pontificates.json")
    antipopes = load("antipopes.json")

    assert people[-1]["papal_name"] == "Leo XIV", "Latest canonical person should be Leo XIV"
    assert pontificates[-1]["papal_name"] == "Leo XIV", "Latest pontificate should be Leo XIV"
    assert len(people) >= 260, f"Expected a full historical person list, found {len(people)}"
    assert len(pontificates) >= 267, f"Expected full canonical pontificate list through Leo XIV, found {len(pontificates)}"

    people_names = [p["papal_name"] for p in people]
    assert "Benedict X" not in people_names, "Benedict X must not appear in canonical people"
    assert people_names.count("Benedict IX") == 1, "Benedict IX must appear once as a person"

    benedict_ix = next(p for p in people if p["papal_name"] == "Benedict IX")
    bix_pontificates = [p for p in pontificates if p["pope_id"] == benedict_ix["pope_id"]]
    assert len(bix_pontificates) == 3, "Benedict IX must have three pontificate records"

    assert any(a["claimant_name"] == "Benedict X" for a in antipopes), "Benedict X must appear in antipopes"
    assert all(a["included_in_canonical_popes"] is False for a in antipopes), "Antipopes must not be canonical"

    assert len({p["pope_id"] for p in people}) == len(people), "Duplicate pope_id"
    assert len({p["pontificate_id"] for p in pontificates}) == len(pontificates), "Duplicate pontificate_id"
    assert len({a["antipope_id"] for a in antipopes}) == len(antipopes), "Duplicate antipope_id"

    txt_people = (DATA / "canonical-popes.txt").read_text(encoding="utf-8").splitlines()
    assert txt_people == people_names, "canonical-popes.txt out of sync"

    print("Validation passed")
    print(f"Canonical people: {len(people)}")
    print(f"Canonical pontificates: {len(pontificates)}")
    print(f"Antipopes: {len(antipopes)}")

if __name__ == "__main__":
    main()
