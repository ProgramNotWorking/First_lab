class Money:

    def __init__(self, percent):
        self.__percent = percent * 0.01

    def find_deposit(self):
        money = 1000
        rise = money * self.__percent
        count = 0

        while money <= 1100:
            money += rise
            rise = money * self.__percent
            count += 1

        print(count)
