class Divider:

    def __init__(self, number):
        self.__number = number

    def print_result(self):
        temp = 2

        while True:
            if self.__number % temp == 0:
                break
            else:
                temp += 1

        print(temp)
