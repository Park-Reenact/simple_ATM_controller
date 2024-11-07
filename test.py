from bank import Bank
from card import Card
from account import Account
from atm_controller import ATMController

def test():
    bank = Bank()

    account1 = Account(account_number="12345")
    account2 = Account(account_number="67890")
    
    bank.add_account(account1)
    bank.add_account(account2)
    
    card1 = Card(card_number="09876", pin="1234", account = account1)
    card2 = Card(card_number="54321", pin="5678", account = account2)
    
    bank.add_card(card1)
    bank.add_card(card2)

    atm = ATMController()
    
    # Successful Case
    atm.insert_card(card1, "1234")
    atm.select_account()
    atm.check_balance()
    atm.deposit(500)
    atm.withdraw(200)
    atm.check_balance()
    atm.eject_card()
    print("#########################")

    # Incorrect PIN Case
    atm.insert_card(card1, "0000")
    print("#########################")
    
    # Deposit without card
    atm.deposit(100)
    print("#########################")

    # Insert card2
    atm.insert_card(card2, "5678")
    atm.select_account()
    atm.check_balance()
    print("#########################")
    
    # Withdraw more than available balance
    atm.withdraw(600)

if __name__ == "__main__":
    test()
