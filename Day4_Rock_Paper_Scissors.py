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

#Write your code below this line 👇
import random 

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3: 
  exit (print("You typed an invalid number, you lose"))
elif user_input == 0:
  print(rock)
elif user_input == 1: 
  print(paper)
elif user_input == 2: 
  print(scissors)


possibilities = [rock, paper, scissors]
random_selection = random.randint(0,2)

computer_answer = possibilities[random_selection]

print(f"Computer chose: {computer_answer}")

# rock beats scissors 
# scissors beats paper 
# paper beats rock 



if (user_input == 0 and computer_answer == scissors) or (user_input == 2 and computer_answer == paper) or (user_input == 1 and computer_answer == rock):
  print ("You win!")
elif (user_input == 0 and computer_answer == rock) or  (user_input == 1 and computer_answer == paper) or (user_input == 2 and computer_answer == scissors):
  print("It's a draw")
else: 
  print("You lose")
