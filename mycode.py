import pandas as pd
import os

# Ensure the "data" directory exists
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

# If file doesn't exist → create V1
if not os.path.exists(file_path):
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print("V1 dataset created")

else:
    df = pd.read_csv(file_path)

    # Decide what to add based on current length
    if len(df) == 3:
        # V2
        new_row = {'Name': 'David', 'Age': 28, 'City': 'Houston'}
        print("Adding V2 row")

    elif len(df) == 4:
        # V3
        new_row = {'Name': 'Emma', 'Age': 26, 'City': 'Boston'}
        print("Adding V3 row")

    else:
        print("No new rows to add")
        new_row = None

    if new_row:
        df.loc[len(df.index)] = new_row
        df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")