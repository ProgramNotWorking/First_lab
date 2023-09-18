class Numbers:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_result(self):
        for number in range(0, self.__b):
            print(self.__a)

