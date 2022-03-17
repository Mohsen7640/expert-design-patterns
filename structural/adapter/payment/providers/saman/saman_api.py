class SamanAPI:

    def __init__(self, api_key):
        self.api_key = api_key

    def pay(self, amount):
        return f'Do Payment In Saman Gateway => {amount}'
