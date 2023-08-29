from flair.data import Sentence
from flair.models import SequenceTagger
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline,set_seed
from transformers import pipeline
ner_pipeline = pipeline("ner", model="dbmdz/flair-ner-english-fast")
text = "Your input text goes here."
ner_results = ner_pipeline(text)
for entity in ner_results:
    print(entity["entity"], entity["word"])
