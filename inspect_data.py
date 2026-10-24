import csv
with open("waterbodies.csv", encoding = "utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print("Number of rows:", len(rows))
    print("columns:", list(rows[0].keys()))

import csv

def inspect_column(filename,column):
    with open(filename, encoding = "utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        values = []
        for row in rows:
            raw = row[column].strip()
            if raw == "":
                continue
            values.append(float(raw))
    return {"smallest area": min(values),
            "largest area": max(values),
            "count": len(values)}

results = inspect_column("waterbodies.csv","area_km2")
print(results)