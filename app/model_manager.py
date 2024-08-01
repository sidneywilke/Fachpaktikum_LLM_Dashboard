import ollama

#Nimmt Eingabewerte entgegen und schickt sie an das ausgewählte Modell. Gibt die Antwort dieser zurück.
class ModelManager:
    def __init__(self):
        self.ollama = ollama

    def get_response(self, prompt, model):

        response = self.ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']

