from transformers import pipeline, Pipeline


def func(text, labels):
    classifier: Pipeline = pipeline("zero-shot-classification", model="model/roberta-large")
    results:dict = classifier(text, labels)
    # res:dict = results[0]
    labels:list = results.get('labels')
    scores:list = results.get('scores')
    print(text)
    print('Это ' + labels[0] + ' с вероятностью ')
    print(scores[0])
    return labels[0]
