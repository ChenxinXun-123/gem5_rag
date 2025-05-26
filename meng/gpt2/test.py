import torch
print("Torch version:", torch.__version__)

if torch.cuda.is_available():
    print("CUDA is available.")
    print("CUDA version:", torch.version.cuda)
    # print("Torch is using CUDA:", torch.backends.cuda.is_built())

if torch.version.hip:
    print("ROCm is available.")
    print("ROCm version:", torch.version.hip)
    # print("Torch is using ROCm:", torch.backends.hip.is_available())

import transformers
print(transformers.__version__)
# print(dir(transformers))
print("----------------------------------------------------------------------")
from transformers import AutoModel

from transformers import pipeline
# from huggingface_hub import login
import time

# login(token = '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')

print("111111111111111111111111111111111111111111111111111111111")
model_id = "openai-community/gpt2"
print("222222222222222222222222222222222222222222222222222222222")
pipe = pipeline(
    "text-generation", 
    model=model_id, 
)
print("333333333333333333333333333333333333333333333333333333333")
# Set pad_token_id to eos_token_id to avoid padding warning
pipe.model.config.pad_token_id = pipe.model.config.eos_token_id
print("444444444444444444444444444444444444444444444444444444444")
# Generate text with max_new_tokens to control length
time1 = time.time()
print("start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
output = pipe("Artificial intelligence is ", max_new_tokens=1)
# print("end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Time Execute: ", time.time()-time1)

# Print output
print(output)