import ollama
class ModelManager:
    def __init__(self):
        self.ollama = ollama

    def get_response(self, prompt, model):
        print(prompt, model)
        response = self.ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}], stream=True)
        for chunk in response:
            print(model+f"Model Manager Output{chunk['message']['content']}")
            yield f"{chunk['message']['content']}"

