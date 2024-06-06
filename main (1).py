import random
while True:
  user_choice = int(input("enter choice:type 1 for rock,2 for paper,3 for scissors"))
  if user_choice > 3 or user_choice < 0:
    print("enter valid input,exit.")
    continue
  else:
    computer_choice = random.randint(1, 3)
    print("computer choose:")
    print(computer_choice)
    if computer_choice == user_choice:
      print("Tie")
    elif computer_choice == 1 and user_choice == 2:
      print("user wins")
    elif computer_choice == 1 and user_choice == 3:
      print("computer wins")
    elif computer_choice == 2 and user_choice == 1:
      print("computer wins")
    elif computer_choice == 2 and user_choice == 3:
      print("user wins")
    elif computer_choice == 3 and user_choice == 1:
      print("user wins")
    elif computer_choice == 3 and user_choice == 2:
      print("computer wins")
  play_again = input("user want to play?(yes/no):").strip().lower()
  if play_again != 'yes':
    print("hope u enjoyed")
    break
