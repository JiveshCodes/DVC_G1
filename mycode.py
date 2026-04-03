import pandas as pd
import os

# Ensure the "data" directory exists
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

# Check if file exists
if not os.path.exists(file_path):
    # Create initial dataset (V1)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print("V1 dataset created")

else:
    # Append new row (V2)
    df = pd.read_csv(file_path)

    new_row = {'Name': 'David', 'Age': 28, 'City': 'Houston'}
    df.loc[len(df.index)] = new_row

    df.to_csv(file_path, index=False)
    print("V2 row added")

print(f"CSV file saved to {file_path}")