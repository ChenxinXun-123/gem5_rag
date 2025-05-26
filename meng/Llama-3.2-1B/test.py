
import torch
from transformers import pipeline
from huggingface_hub import login
import time

# login(token = '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')

print("111111111111111111111111111111111111111111111111111111111")
model_id = "meta-llama/Llama-3.2-1B"
print("222222222222222222222222222222222222222222222222222222222")
pipe = pipeline(
    "text-generation", 
    model=model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)
print("333333333333333333333333333333333333333333333333333333333")
# Set pad_token_id to eos_token_id to avoid padding warning
pipe.model.config.pad_token_id = pipe.model.config.eos_token_id

# Generate text with max_new_tokens to control length
time1 = time.time()
output = pipe("Artificial intelligence is ", max_new_tokens=1)
print("Time Execute: ", time.time()-time1)

# Print output
print(output)