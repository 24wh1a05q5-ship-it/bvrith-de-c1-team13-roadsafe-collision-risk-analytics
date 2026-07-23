"""
RoadSafe Synthetic Data Generator

Week: 2
Purpose:
    Generate small educational CSV/JSON sample datasets for the RoadSafe 
    Collision Risk Analytics project.
"""

from pathlib import Path
import csv
import json
import random
from datetime import datetime, timedelta

# Edit 1: Keep the seed at 42 so work is reproducible for reviewers [1, 2]
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

BASE_DIR = Path(__file__).resolve().parents[5]
RAW_DIR = BASE_DIR / "data_sample" / "raw"
STREAMING_DIR = BASE_DIR / "data_sample" / "streaming"

RAW_DIR.mkdir(parents=True, exist_ok=True)
STREAMING_DIR.mkdir(parents=True, exist_ok=True)

# Edit 2: Rename entities and files to match the RoadSafe Data Dictionary [2]
def generate_lookups() -> None:
    """Create a small sample of the collision code lookup."""
    output_path = RAW_DIR / "collision_code_lookup_sample.csv"
    rows = [
        {"lookup_domain": "police_force", "code": "1", "description": "Metropolitan Police"},
        {"lookup_domain": "collision_severity", "code": "1", "description": "Fatal"},
        {"lookup_domain": "collision_severity", "code": "2", "description": "Serious"},
        {"lookup_domain": "collision_severity", "code": "3", "description": "Slight"},
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows.keys())
        writer.writeheader()
        writer.writerows(rows)

def generate_collisions_sample(row_count: int = 1000) -> None:
    """Create a raw collisions source file with RoadSafe fields and defects."""
    output_path = RAW_DIR / "collisions_sample.csv"
    
    # RoadSafe time boundary: 1 January to 31 December 2024 [6, 7]
    start_date = datetime(2024, 1, 1)
    
    fieldnames = [
        "collision_index", "collision_severity", "number_of_vehicles", 
        "number_of_casualties", "date", "time", "longitude", "latitude"
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, row_count + 1):
            # Create a unique collision index format: 2024 + Random ID [8]
            collision_id = f"2024{random.randint(1000000, 9999999)}"
            
            # Edit 3: Inject measured defect rates (e.g., 0.3% duplicates) [9, 10]
            if random.random() < 0.003: 
                collision_id = f"DUP_{collision_id}" 

            ts = start_date + timedelta(days=random.randint(0, 364), minutes=random.randint(0, 1439))
            
            writer.writerow({
                "collision_index": collision_id,
                "collision_severity": random.choice([5, 11, 12]),
                "number_of_vehicles": random.randint(1, 3),
                "number_of_casualties": random.randint(1, 2),
                "date": ts.strftime("%d/%m/%Y"),
                "time": ts.strftime("%H:%M"),
                # Inject missing coordinates (e.g., 1.8% nulls) [9, 13]
                "longitude": round(random.uniform(-9, 3), 5) if random.random() > 0.018 else "",
                "latitude": round(random.uniform(49, 61), 5) if random.random() > 0.018 else "",
            })

def generate_streaming_alerts(batch_number: int = 1, event_count: int = 10) -> None:
    """Create JSON lines file for streaming simulation [14]."""
    output_path = STREAMING_DIR / f"incident_alert_drop_{batch_number:02d}.json"
    start_time = datetime(2024, 11, 15, 8, 0, 0)

    with output_path.open("w", encoding="utf-8") as f:
        for i in range(1, event_count + 1):
            event = {
                "incident_event_id": f"RS-EVT-{batch_number:02d}-{i:04d}",
                "collision_reference": f"2024{random.randint(1000000, 9999999)}",
                "event_timestamp": (start_time + timedelta(minutes=i * 3)).isoformat() + "Z",
                "event_type": "INCIDENT_CREATED",
                "status": "REPORTED",
                "severity_code": random.choice(["1", "2", "3"])
            }
            f.write(json.dumps(event) + "\n")

def main() -> None:
    generate_lookups()
    generate_collisions_sample(row_count=1000) # Keep samples small for GitHub [3]
    generate_streaming_alerts(batch_number=1, event_count=10)
    print("RoadSafe synthetic sample data generated successfully.")

if __name__ == "__main__":
    main()
