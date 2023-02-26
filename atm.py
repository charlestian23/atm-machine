from __future__ import annotations


debug_mode = True


class ATMDispenser:
    _next_chain: ATMDispenser = None

    def set_next_chain(self, next_chain: ATMDispenser):
        self._next_chain = next_chain

    def withdraw_money(self, money: int):
        pass


class FiftyDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if debug_mode:
            print("\tEntering $50 process in chain")
        if money >= 50:
            bill_count = money // 50
            remainder = money % 50
            print("ATM withdrawing", bill_count, "$50 bills")
            if remainder > 0:
                if debug_mode:
                    print("\tGoing from the $50 process to the next process in the chain")
                self._next_chain.withdraw_money(remainder)
            elif debug_mode:
                print("\tRemainder is 0, end of chain")
        else:
            if debug_mode:
                print("\tGoing from the $50 process to the next process in the chain")
            self._next_chain.withdraw_money(money)


class TwentyDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if debug_mode:
            print("\tEntering $20 process in chain")
        if money >= 20:
            bill_count = money // 20
            remainder = money % 20
            print("ATM withdrawing", bill_count, "$20 bills")
            if remainder > 0:
                if debug_mode:
                    print("\tGoing from the $20 process to the next process in the chain")
                self._next_chain.withdraw_money(remainder)
            elif debug_mode:
                print("\tRemainder is 0, end of chain")
        else:
            if debug_mode:
                print("\tGoing from the $20 process to the next process in the chain")
            self._next_chain.withdraw_money(money)


class TenDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if debug_mode:
            print("\tEntering $10 process in chain")
        if money >= 10:
            bill_count = money // 10
            remainder = money % 10
            print("ATM withdrawing", bill_count, "$10 bills")
            if remainder > 0:
                if debug_mode:
                    print("\tGoing from the $10 process to the next process in the chain")
                self._next_chain.withdraw_money(remainder)
            elif debug_mode:
                print("\tRemainder is 0, end of chain")
        else:
            if debug_mode:
                print("\tGoing from the $10 process to the next process in the chain")
            self._next_chain.withdraw_money(money)


class FiveDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if debug_mode:
            print("\tEntering $5 process in chain")
        if money >= 5:
            bill_count = money // 5
            remainder = money % 5
            print("ATM withdrawing", bill_count, "$5 bills")
            if remainder > 0:
                if debug_mode:
                    print("\tGoing from the $5 process to the next process in the chain")
                self._next_chain.withdraw_money(remainder)
            elif debug_mode:
                print("\tRemainder is 0, end of chain")
        else:
            if debug_mode:
                print("\tGoing from the $5 process to the next process in the chain")
            self._next_chain.withdraw_money(money)


class OneDollarDispenser(ATMDispenser):
    def withdraw_money(self, money: int):
        if debug_mode:
            print("\tEntering $1 process in chain")
        print("ATM withdrawing", money, "$1 bills")
        if debug_mode:
            print("\tLast process complete, end of chain")

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
