# Example: Extracting differences between two dictionaries
# (could be used in bot logs or version checks)

from datetime import datetime

dict1 = {
    "id": 1,
    "cost": 100,
    "datetime": "2025-08-25 10:00:00"
}

dict2 = {
    "id": 1,
    "cost": 120,
    "datetime": "2025-08-25 12:00:00"
}

def extract_diff(d1, d2):
    diff = {}
    for key in d1:
        if d1[key] != d2.get(key):
            diff[key] = {"old": d1[key], "new": d2[key]}
    return diff

if __name__ == "__main__":
    differences = extract_diff(dict1, dict2)
    print("Differences found:", differences)
