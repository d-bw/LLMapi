from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM , BitsAndBytesConfig,AutoModel
import torch
from pathlib import Path
import huggingface_hub

huggingface_hub_token = "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"
huggingface_hub.login(token=huggingface_hub_token)
#模型量化配置

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).half().cuda()
model = model.eval()


