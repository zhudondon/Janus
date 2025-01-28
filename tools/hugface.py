from huggingface_hub import snapshot_download
import os

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'   # 这个镜像网站可能也可以换掉
# 指定模型名称和下载路径
model_name = "bert-base-uncased"
save_path = "./my_local_model"

# 下载模型
snapshot_download(repo_id=model_name, cache_dir=save_path)
