from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = model.eval()

def chat(token,history):
    response, history = model.chat(tokenizer, token, history=history)
    print(response)

if __name__ == "__main__":
    chat("hello",[])