'''

Collatz Sequence

1) This sequence works for every integer number;
2) If the number is even, collatz() returns number/2. If the number is odd, collatz returns (3 * number) + 1;
3) This program only stops when the number becomes 1.

'''

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * number) + 1


print("Enter a number:")

try:
    number = int(input())
except ValueError:
    print("Error! You must type an int number")
    print("Enter a number:")
    number = int(input())

while number != 1:
    number = collatz(number)
    print(number)