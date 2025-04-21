import pandas as pd

# Step 1: Load the Dataset
df = pd.read_csv('raw_dataset.csv')

# Step 2: Inspect the Data
print(df.info())
print(df.describe())
print(df.head())

# Step 3: Handle Null Values
# Example: Fill nulls with the mean for numerical columns and mode for categorical columns
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    df[column].fillna(df[column].mean(), inplace=True)

for column in df.select_dtypes(include=['object']).columns:
    df[column].fillna(df[column].mode()[0], inplace=True)

# Step 4: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 5: Standardize Formats
# Example: Convert date columns to datetime format
if 'date_column' in df.columns:
    df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Example: Standardize string casing
for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].str.lower().str.strip()

# Step 6: Rename Columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Step 7: Save the Cleaned Dataset
df.to_csv('cleaned_dataset.csv', index=False)

# Summary of changes
summary = {
    'null_values_handled': True,
    'duplicates_removed': True,
    'formats_standardized': True,
    'columns_renamed': {'old_name': 'new_name'},
    'total_rows_after_cleaning': df.shape[0],
    'total_columns_after_cleaning': df.shape[1]
}

print(summary)