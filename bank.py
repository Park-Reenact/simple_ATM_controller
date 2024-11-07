class Bank:
    def __init__(self):
        self.accounts = []
        self.cards = []

    def add_account(self, account):
        self.accounts.append(account)
        
    def add_card(self, card):
        self.cards.append(card)

