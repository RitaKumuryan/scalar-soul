"""
crosslink_csv.py
Author: Scalar Soul / Haykyan Research Team

Description:
Reads and summarizes the contents of all .csv files in /data/csv_data/.
Outputs number of rows, columns, and headers for each file.
Use this to audit, crosslink, or debug data-driven modules in the HBT model.
"""

import os
import pandas as pd

# Set the relative path to the csv_data folder
csv_folder = os.path.join("..", "data", "csv_data")

# Dictionary to store summary
summary = {}

# Read all CSV files in the folder
for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        path = os.path.join(csv_folder, file)
        try:
            df = pd.read_csv(path)
            summary[file] = {
                "rows": df.shape[0],
                "columns": df.shape[1],
                "column_names": list(df.columns)
            }
        except Exception as e:
            summary[file] = {"error": str(e)}

# Print the summary
print("\n=== CSV Crosslink Summary ===")
for fname, info in summary.items():
    print(f"\n📄 {fname}")
    for key, value in info.items():
        print(f"  {key}: {value}")
