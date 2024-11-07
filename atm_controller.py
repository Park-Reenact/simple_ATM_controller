class ATMController:
    def __init__(self):
        self.current_account = None
        self.card_inserted = False

    def insert_card(self, card, pin):
        if self.card_inserted:
            print("A card is already inserted. Please eject the card first.")
            return
        
        if card.verify_pin(pin):
            self.current_account = card.account
            self.card_inserted = True
            print("Account access successful!")
        else:
            print("Incorrect PIN.")
            self.current_account = None
            
    def eject_card(self):
        if not self.card_inserted:
            print("No card inserted.")
            return
        print("Card ejected.")
        self.card_inserted = False
        self.current_account = None

    def select_account(self):
        if self.current_account:
            print(f"Current account: {self.current_account.account_number}")
        else:
            print("Please insert your card first")
    
    def check_balance(self):
        if self.current_account:
            balance = self.current_account.get_balance()
            print(f"balance: {balance}")
        else:
            print("Please insert your card first.")
            
    def deposit(self, amount):
        if self.current_account:
            self.current_account.deposit(amount)
            print(f"{amount} deposited. balance: {self.current_account.get_balance()}")
        else:
            print("Please insert your card first.")

    def withdraw(self, amount):
        if self.current_account:
            try:
                self.current_account.withdraw(amount)
            except ValueError as e:
                print(f"{e}")
            else:
                print(f"{amount} withdrawn. balance: {self.current_account.get_balance()}")
        else:
            print("Please insert your card first.")
