from transformers import RobertaTokenizer, RobertaForSequenceClassification
import os
# Define a local model directory
model_dir = os.path.join(os.getenv("MODEL_DIR", "models"), "roberta-base")

# Download and save tokenizer and model locally
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=2)

# Save locally
tokenizer.save_pretrained(model_dir)
model.save_pretrained(model_dir)

print(f"Model saved to {model_dir}")
