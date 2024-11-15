from huggingface_hub import snapshot_download

snapshot_download(repo_id="joeddav/xlm-roberta-large-xnli", local_dir="model")