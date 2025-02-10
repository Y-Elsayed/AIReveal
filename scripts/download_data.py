import pandas as pd
from datasets import load_dataset
import os
# Loading the dataset
train = load_dataset("yaful/MAGE", split="train")
valid = load_dataset("yaful/MAGE", split="validation")
test = load_dataset("yaful/MAGE", split="test")

# Converting to pandas DataFrame
train_df = pd.DataFrame(train)
valid_df = pd.DataFrame(valid)
test_df = pd.DataFrame(test)

# Creating a directory to save the CSV files
data_dir = "./data"
os.makedirs(data_dir, exist_ok=True)

# Saving to CSV
train_df.to_csv(os.path.join(data_dir, "train.csv"), index=False)
valid_df.to_csv(os.path.join(data_dir, "valid.csv"), index=False)
test_df.to_csv(os.path.join(data_dir, "test.csv"), index=False)

# Print confirmation with full paths
print("Train CSV saved at:", os.path.abspath(os.path.join(data_dir, "train.csv")))
print("Valid CSV saved at:", os.path.abspath(os.path.join(data_dir, "valid.csv")))
print("Test CSV saved at:", os.path.abspath(os.path.join(data_dir, "test.csv")))
