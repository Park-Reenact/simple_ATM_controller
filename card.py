class Card:
    def __init__(self, card_number, pin, account):
        self.card_number = card_number
        self.pin = pin
        self.account = account
        
    def verify_pin(self, pin):
        return self.pin == pin
