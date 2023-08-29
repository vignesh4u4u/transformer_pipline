from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline,set_seed
from pdfminer.high_level import extract_text
set_seed(42)
model="gpt2"
generator = pipeline('text-generation', model=model)
set_seed(42)
prompt =input("enter the question :")
res = generator(text_inputs=prompt, max_length=50, num_return_sequences=5,do_sample=True,temperature=0.9)
print(res[0]["generated_text"])