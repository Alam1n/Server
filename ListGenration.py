import pandas as pd

# Load the dataset
dataset_path = 'ProcessedFarmFeedFile.csv'  # Replace with the actual path or filename

df = pd.read_csv(dataset_path)  # Assuming it's a tab-separated file

def get_feedstuff_for_hardcoded_animal(hardcoded_animal):
    # Filter the dataset based on the hardcoded animal
    filtered_data = df[df[hardcoded_animal] == 1]

    # Extract the feedstuff names and additional information
    feedstuff_info = filtered_data[['FEEDSTUFF', 'Total_Protein', 'Total_Fiber', 'Total_Energy_Maintenance']]

    return feedstuff_info
