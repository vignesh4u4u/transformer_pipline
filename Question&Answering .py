from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline,set_seed
from pdfminer.high_level import extract_text,extract_pages
import torch
import random
seed = 42
random.seed(seed)
torch.manual_seed(seed)
pdf=extract_text("lease\Lease (5).pdf")
output_filename = "pdf_output.txt"
with open(output_filename, "w",encoding="utf-8") as output_file:
    output_file.write(pdf)
context=output_filename
ask_query = input("enter the qustion :")
model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering',model=model_name,tokenizer=model_name)
QA_input = {'question': ask_query,
            'context': pdf
            }
res = nlp(QA_input)
answer = res['answer']
print(answer)
