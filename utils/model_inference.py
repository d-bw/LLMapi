from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM , BitsAndBytesConfig,AutoModel
import torch
from pathlib import Path
import huggingface_hub

class ChatModel():
  def __init__(self):
    self.model=model = AutoModel.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0", trust_remote_code=True).half().cuda()
    self.tokenizer = tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0", trust_remote_code=True)
    self.pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")
       

  def inference(self,sent):
    messages = [
      {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
      },
    {"role": "user", "content": sent},
    ]
    prompt = self.pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = self.pipe(prompt, max_new_tokens=512, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    #response, history = self.model.chat(self.tokenizer, sent, history=[])
    response=outputs[0]["generated_text"]
    return response

model=ChatModel()
