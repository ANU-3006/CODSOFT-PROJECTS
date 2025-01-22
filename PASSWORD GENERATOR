import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z"
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("welcome to password generator")
letter_a = int(input("enter the no of letters needed in passward:\n"))
numbers_a = int(input("enter the numbers u need in passward:\n"))
symbols_a = int(input("enter the symbols u need in paasward:\n"))
passward = ""
for i in range(1, letter_a + 1):
    char = random.choice(letters)
    passward = passward + char
for i in range(1, numbers_a + 1):
    char = random.choice(numbers)
    passward = passward + char
for i in range(1, symbols_a + 1):
    char = random.choice(symbols)
    passward = passward + char
print(passward)



