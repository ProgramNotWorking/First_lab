class Numbers:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def print_result(self):
        count = 1
        print(self.__a)

        for n in range(self.__b - self.__a):
            count += 1
            print(self.__a + count)

        print(count)

