from datasets import load_dataset
import os

# Loading the dataset
train = load_dataset("yaful/MAGE", split="train").to_pandas()
valid = load_dataset("yaful/MAGE", split="validation").to_pandas()
test = load_dataset("yaful/MAGE", split="test").to_pandas()

# Create a directory for data if it doesn't exist
data_dir = os.getenv("DATA_DIR", "data")
os.makedirs(data_dir, exist_ok=True)

# Saving to CSV
train.to_csv(os.path.join(data_dir, "train.csv"), index=False)
valid.to_csv(os.path.join(data_dir, "valid.csv"), index=False)
test.to_csv(os.path.join(data_dir, "test.csv"), index=False)

# Print confirmation with full paths
print("Train CSV saved at:", os.path.abspath(os.path.join(data_dir, "train.csv")))
print("Valid CSV saved at:", os.path.abspath(os.path.join(data_dir, "valid.csv")))
print("Test CSV saved at:", os.path.abspath(os.path.join(data_dir, "test.csv")))
