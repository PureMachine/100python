import requests

class TriviaData:
    def __init__(self, amount=0):
        self.token = ""
        self.questions = []
        self.amount = amount
        self.type_of_question = "boolean"


    def get_token(self):
        params = {"command": "request"}
        tok = requests.get(url="https://opentdb.com/api_token.php", params=params)
        tok.raise_for_status()
        self.token = tok.json()["token"]


    def get_questions(self):
        if not self.token:
            self.get_token()

        params = {"amount": self.amount, "token": self.token, "type": self.type_of_question}

        qs = requests.get(url="https://opentdb.com/api.php", params=params)
        qs.raise_for_status()
        raw_questions = qs.json()["results"]
        q = [{"question": item["question"], "answer": item["correct_answer"]} for item in raw_questions]
        self.questions = q

