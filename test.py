import pandas as pd

# Reading the CSV file
file_path = "modified_data_without_cpr.csv"
# df = pd.read_csv(file_path)
df = pd.read_csv(file_path, nrows=20)

# If you want to save the expanded data to a new CSV
df.to_csv("20_record_data.csv", index=False)