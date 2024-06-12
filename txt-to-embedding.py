from transformers import BertTokenizer, BertModel
import torch

# Initialize tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Example text
text = "Hello, how are you?"

# Tokenize text and convert to input IDs
inputs = tokenizer(text, return_tensors='pt', padding='max_length', max_length=77, truncation=True)

# Get the embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract the last hidden state
embeddings = outputs.last_hidden_state  # Shape will be [1, 77, 768]

print(embeddings.shape)  # torch.Size([1, 77, 768])
print(embeddings)