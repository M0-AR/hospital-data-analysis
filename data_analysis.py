import pandas as pd

##################################################################################################################
def drop_column_by_index(input_path: str, column_index: int, output_path: str = "modified_dataset.csv") -> None:
    """
    Reads a CSV file, drops the specified column by its index, and saves the modified dataframe back to a CSV file.

    Parameters:
    - input_path (str): Path to the input CSV file.
    - column_index (int): Index of the column to be dropped (0-based index).
    - output_path (str, optional): Path to save the modified CSV file. Defaults to "modified_dataset.csv".

    Returns:
    None: The function saves the modified dataframe to a CSV file and does not return any value.
    """
    
    # Read the dataset
    df = pd.read_csv(input_path)
    
    # Drop the specified column by its index
    df.drop(df.columns[column_index], axis=1, inplace=True)
    
    # Save the modified dataset back to a .csv file
    df.to_csv(output_path, index=False)

# Drop cpr's column
# drop_column_by_index("Test_DATA_2023-09-18_0823.csv", 1, "modified_data_without_cpr.csv")
##################################################################################################################


##################################################################################################################
"""
We have columns with string representations of lists, and elements in the same position across these lists are correlated. 
For example, the first element in the miba_sample_type list is correlated with the first element in the miba_collection_date list for each record.
"""
import pandas as pd
import ast

def expand_section(df, section_cols):
    """
    Expand columns for a particular section that contain string representations of lists into multiple rows.

    Parameters:
    - df (DataFrame): Input DataFrame.
    - section_cols (list): Columns in the section containing string representations of lists.

    Returns:
    DataFrame: A DataFrame with expanded rows for the section.
    """
    
    def safe_literal_eval(s):
        if pd.isna(s):
            return []

        # Check if the string starts and ends with double quotes
        if s.startswith('"') and s.endswith('"'):
            s = s[1:-1]

        try:
            result = ast.literal_eval(s)
        except Exception as e:
            print(f"Error: {e}")
        
        return result
    
    # Convert string representation of lists to actual lists
    for col in section_cols:
        df[col] = df[col].apply(safe_literal_eval)

    # Use the 'explode' function to expand lists into rows for each column in the section
    for col in section_cols:
        df = df.explode(col)
    
    return df


def get_sections_by_keyword(df, keywords):
    """
    Group columns by their common prefixes (keywords).

    Parameters:
    - df (DataFrame): Input DataFrame.
    - keywords (list): List of keywords.

    Returns:
    List[List[str]]: List of lists of columns grouped by keywords.
    """
    sections = []
    for keyword in keywords:
        section = [col for col in df.columns if keyword in col]
        sections.append(section)
    return sections

# Reading the CSV file
file_path = "modified_data_without_cpr.csv"
# df = pd.read_csv(file_path)
df = pd.read_csv(file_path, nrows=1)

# Define keywords for sections
# keywords = ['miba', 'medicine', 'diagnose', 'pato', 'vital', 'blood']
keywords = ['miba']

# Generate sections based on keywords
sections = get_sections_by_keyword(df, keywords)

# Transform the DataFrame by section
for section in sections:
    df = expand_section(df, section)

# If you want to save the expanded data to a new CSV
df.to_csv("expanded_data.csv", index=False)
##################################################################################################################
