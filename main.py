import rectangle
import two_numbers
import money


task = int(input('Enter task number: '))

while True:
    if task == 1:
        rectangle = rectangle.Rectangle(
            int(input('Enter x1: ')),
            int(input('Enter y1: ')),
            int(input('Enter x2: ')),
            int(input('Enter y2: '))
        )

        rectangle.find_sides_size(
            lambda a, b: print(a * 2 + b * 2),
            lambda a, b: print(a * b)
        )

        break
    elif task == 2:
        numbers = two_numbers.Numbers(
            int(input('Enter K: ')),
            int(input('Enter N: '))
        )
        numbers.get_result()

        break
    elif task == 3:
        percent = int(input('Enter percent (between 0 and 25): '))

        while percent <= 0 or percent >= 25:
            percent = int(input('Between 0 and 25 i said >:3'))

        money_task = money.Money(
            percent
        )
        money_task.find_deposit()

        break
    else:
        task = int(input('Enter task number: '))

