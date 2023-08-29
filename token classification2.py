from flair.data import Sentence
from flair.models import SequenceTagger
from pdfminer.high_level import extract_text
tagger = SequenceTagger.load("flair/ner-english-ontonotes-fast")
text=extract_text("lease\Lease (5).pdf")
clean_text=text.split()
formatted_output = ' '.join(clean_text)
#a=int(input("staring_word_number :"))
#b=int(input("ending word number :"))
first_100_words = ' '.join(clean_text[0:500])
#print(first_100_words)
sentence = Sentence(first_100_words)
tagger.predict(sentence)
entity_list = []
for entity in sentence.get_spans('ner'):
    if entity.tag in ['ORG', 'PERSON']:
        entity_list.append(entity.text)
unique_entities = set(entity_list)
num_entities = sorted(unique_entities)
for i, entity_text in enumerate(unique_entities, start=1):
    variable_name = f"name_{i} = \"{entity_text}\""
    print(variable_name)
