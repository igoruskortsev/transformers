from pathlib import Path
from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer, XLMRobertaTokenizer

model_id = "joeddav/xlm-roberta-large-xnli"
onnx_path = Path("onnx_model")

model = ORTModelForFeatureExtraction.from_pretrained(model_id, from_transformers=True)
# tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer = XLMRobertaTokenizer.from_pretrained(
    model_id,
    use_fast=False
)

# save onnx checkpoint and tokenizer
model.save_pretrained(onnx_path)
# tokenizer.save_pretrained("onnx_tokenizer")

# python -m optimum.exporters.onnx --model tabularisai/multilingual-sentiment-analysis --task sequence-classification exported