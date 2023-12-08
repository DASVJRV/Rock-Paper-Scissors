import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
comp_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print(f"You entered: {user_choice} That's an invalid number!")
elif user_choice == 1 and comp_choice == 0:
    print(f"You chose: {choices[1]} and computer chose: {choices[0]} You win!")
elif user_choice == 0 and comp_choice == 2:
    print(f"You chose: {choices[0]} and computer chose: {choices[2]} You win!")
elif user_choice == 2 and comp_choice == 1:
    print(f"You chose: {choices[2]} and computer chose: {choices[1]} You win!")
elif user_choice == comp_choice:
    print(f"You chose: {choices[user_choice]} and computer chose: {choices[comp_choice]} That's a draw!")
else:
    print(f"You chose: {choices[user_choice]} and computer chose: {choices[comp_choice]} You lose!")

