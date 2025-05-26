# import torch
# print(torch.version.cuda)  # Should print 'None' if no CUDA
# print(torch.version.hip)   # Should print a ROCm version if using ROCm
# print(torch.cuda.is_available())  # Should be False if CUDA is not installed






from vllm import LLM, SamplingParams

prompts = ["""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>

What is the capital of France?<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

vllm_model = LLM(model="./Llama-3.2-1B-Instruct", max_model_len=100000)

outputs = vllm_model.generate(prompts, sampling_params)
for output in outputs:
    response = output.outputs[0].text
    print(f"\n\nGenerated text: {response}\n\n")
