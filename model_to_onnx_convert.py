from pathlib import Path
from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer, XLMRobertaTokenizer

model_id = "MoritzLaurer/ernie-m-large-mnli-xnli"
onnx_path = Path("onnx_model")

model = ORTModelForFeatureExtraction.from_pretrained(model_id, from_transformers=True)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model.save_pretrained(onnx_path)
# tokenizer = XLMRobertaTokenizer.from_pretrained(
#     model_id,
#     use_fast=False
# )

# tokenizer.save_pretrained("onnx_tokenizer")

# python -m optimum.exporters.onnx --model MoritzLaurer/ernie-m-large-mnli-xnli --task zero-shot-classification onnx_model