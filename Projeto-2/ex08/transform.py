import sys

def square_even_numbers(numbers : list[int]) -> list[int]:
    res = []
    i = 1
    for number in numbers:
        if (number % 2 == 0):
            res.append(number ** 2)
    return res

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("None")
    else:
        print(f"{square_even_numbers(sys.argv)}")