from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
from datetime import datetime

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

print(model.get_memory_footprint())
start = datetime.now()
input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=1000)
print(tokenizer.decode(outputs[0]))

print(model.get_memory_footprint())
print(datetime.now() - start)
