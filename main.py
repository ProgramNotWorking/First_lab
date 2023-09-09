import rectangle
import two_numbers
import divider


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
            int(input('Enter a: ')),
            int(input('Enter b: '))
        )
        numbers.print_result()

        break
    elif task == 3:
        divider = divider.Divider(
            int(input("Enter number: "))
        )
        divider.print_result()

        break
    else:
        task = int(input('Enter task number: '))

