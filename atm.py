from __future__ import annotations


class ATMDispenser:
    _next_chain: ATMDispenser = None

    def set_next_chain(self, next_chain: ATMDispenser):
        self._next_chain = next_chain

    def withdraw_money(self, money: int):
        pass


class FiftyDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if money >= 50:
            bill_count = money // 50
            remainder = money % 50
            print("ATM withdrawing", bill_count, "$50 bills")
            if remainder > 0:
                self._next_chain.withdraw_money(remainder)
        else:
            self._next_chain.withdraw_money(money)


class TwentyDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if money >= 20:
            bill_count = money // 20
            remainder = money % 20
            print("ATM withdrawing", bill_count, "$20 bills")
            if remainder > 0:
                self._next_chain.withdraw_money(remainder)
        else:
            self._next_chain.withdraw_money(money)


class TenDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if money >= 10:
            bill_count = money // 10
            remainder = money % 10
            print("ATM withdrawing", bill_count, "$10 bills")
            if remainder > 0:
                self._next_chain.withdraw_money(remainder)
        else:
            self._next_chain.withdraw_money(money)


class FiveDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if money >= 5:
            bill_count = money // 5
            remainder = money % 5
            print("ATM withdrawing", bill_count, "$5 bills")
            if remainder > 0:
                self._next_chain.withdraw_money(remainder)
        else:
            self._next_chain.withdraw_money(money)


class OneDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        print("ATM withdrawing", money, "$1 bills")


class ATMChain:
    chain = None

    def __init__(self):
        twenty = TwentyDollarDispenser()
        ten = TenDollarDispenser()
        five = FiveDollarDispenser()
        one = OneDollarDispenser()

        self.chain = FiftyDollarDispenser()
        self.chain.set_next_chain(twenty)
        twenty.set_next_chain(ten)
        ten.set_next_chain(five)
        five.set_next_chain(one)


if __name__ == "__main__":
    atm = ATMChain()
    user_input = input("Enter some money (whole number): $")
    while user_input.isnumeric():
        atm.chain.withdraw_money(int(user_input))
        user_input = input("Enter some more money (whole number): $")
