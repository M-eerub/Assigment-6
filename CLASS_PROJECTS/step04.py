# step 4 (puvlic variables and methods-bank class)

class Bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_bank_name(self):
        print("Bank name is:", self.bank_name)

b1 = Bank()
b2 = Bank()

b1.show_bank_name()
b2.show_bank_name
Bank.change_bank_name("State Bank")  # Correct way to change the bank name

b1.show_bank_name
b2.show_bank_name()
