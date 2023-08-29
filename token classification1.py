from pdfminer.high_level import extract_text
from flair.data import Sentence
from flair.models import SequenceTagger
tagger = SequenceTagger.load("flair/ner-english-fast")
text=extract_text("lease\Lease (7).pdf")
clean_text=text.split()
formatted_output = ' '.join(clean_text)
first_100_words = ' '.join(clean_text[:1000])
print(first_100_words)
sentence = Sentence(first_100_words)
tagger.predict(sentence)
entity_list = []
for entity in sentence.get_spans('ner'):
    if entity.tag in ['ORG', 'PER']:
        entity_list.append(entity.text)
unique_entities = set(entity_list)
num_entities = sorted(unique_entities)
for i, entity_text in enumerate(unique_entities, start=1):
    variable_name = f"name_{i} = \"{entity_text}\""
    print(variable_name)
