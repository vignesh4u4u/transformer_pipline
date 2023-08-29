import transformers
from transformers import BloomForCausalLM
model = BloomForCausalLM.from_pretrained("bigscience/bloom-560m")
pipeline = transformers.TextGenerationPipeline(model=model,tokenizer=transformers.AutoTokenizer.from_pretrained("bigscience/bloom-560m"))
output = pipeline("what is factorial.",max_length=100)
print(output[0]["generated_text"])