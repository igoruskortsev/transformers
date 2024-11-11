from transformers import pipeline, Pipeline


def func(text, labels):
    classifier: Pipeline = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")
    results = classifier(text, labels)
    res = results[0]
    print(res)
