class User:

    def __init__(self, pk, username, email, password):
        self.pk = pk
        self.username = username
        self.email = email
        self.password = password
        self.wallet = 0

    def increase_wallet(self, amount):
        current_wallet = self.wallet
        self.wallet = current_wallet + amount
        self.save()
