from transformers import pipeline, Pipeline, XLMRobertaTokenizer

def func(text: str, labels: list):
    tokenizer = XLMRobertaTokenizer.from_pretrained(
        "joeddav/xlm-roberta-large-xnli",
        use_fast=False
    )

    classifier: Pipeline = pipeline(
        "zero-shot-classification",
        model="joeddav/xlm-roberta-large-xnli",
        tokenizer=tokenizer
    )
    results: dict = classifier(text, labels)
    labels: list = results.get('labels')
    scores: list = results.get('scores')
    print(text)
    print('Это ' + labels[0] + ' с вероятностью ')
    print(scores[0])

    if len(labels) < 1:
        return list()
    else:
        return labels[:5]

# func(
#     "Отпало колесо",
#     [
#         "Техническое обслуживание/Неисправность салона/Кухня",
#         "Техническое обслуживание/Повреждение ВС/Другое",
#         "Опоздание/неявка на вылет",
#         "Наземное обслуживание/АЭРОМАР/Отсутствие порций питания/напитков (класс обсл-ния)/Отсутствие БКО",
#         "Без темы",
#         "Техническое обслуживание/Неисправность салона/Кресло",
#         "Техническое обслуживание/Техническое состояние ВС/Неисправность систем ВС"
#     ]
# )