class Bank:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.__balance = 0
    def money_x(self):
        user = int(input("сколько вы хотите пополнить баланс: "))
        self.__balance += user
        return f"на вашем счёте: {self.__balance}, Имя влодельца: {self.__name}"
    def _kill(self):
        user = int(input("сколько вы хотите обноличить: "))
        self.__balance -= user
        return f"на вашем счёте: {self.__balance}"
    def __jackpot(self):
        self.__balance * 10
        return f"на вашем счёте: {self.__balance}"
bank = Bank("askhat")
print(bank.money_x())
