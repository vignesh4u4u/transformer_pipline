from transformers import pipeline
analyzer = pipeline("sentiment-analysis")
text = input("give the comment :")
result = analyzer(text)