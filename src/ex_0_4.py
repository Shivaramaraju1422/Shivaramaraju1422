"""
ex_0_4.py
"""


def int_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def main():
    n = int(input("Enter the number: "))
    result = int_sum(n)
    print(result)


if __name__ == "__main__":
    main()


def odd_sum(n):
    sum = 0
    for i in range(n):
        sum += 2*i + 1
    return sum


result = odd_sum(5)
print(result)
