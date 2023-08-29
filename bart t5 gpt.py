from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline,set_seed
set_seed(42)
model_name = "google/flan-t5-large"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
t5_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
prompt = "Translate the following English text to French: 'Hello, how are you?'"
generated_text = t5_pipeline(prompt, max_length=100)[0]['generated_text']
print(generated_text)
