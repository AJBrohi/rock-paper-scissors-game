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

user_played = int(input('What do you want to play? Type 0 for "Rock", 1 for "Paper" or 2 for "Scissors"\n'))

computer_played = random.randint(0,2)

print("You played:")
if user_played == 0:    
    print("Rock\n"+rock)
    
    print("Computer played:")
    if computer_played == 0:
        print("Rock\n"+rock)        
        print("DRAW!")
    elif computer_played == 1:
        print("Paper\n"+paper)        
        print("YOU LOSE!")
    else:
        print("Scissors\n"+scissors)        
        print("YOU WIN!")
        
elif user_played == 1:    
    print("Paper\n"+paper)
    
    print("Computer played:")
    if computer_played == 0:
        print("Rock\n"+rock)        
        print("YOU WIN!")
    elif computer_played == 1:
        print("Paper\n"+paper)        
        print("DRAW!")
    else:
        print("Scissors\n"+scissors)        
        print("YOU LOSE!")
        
elif user_played == 2:    
    print("Scissors\n"+scissors)
    
    print("Computer played:")
    if computer_played == 0:
        print("Rock\n"+rock)        
        print("YOU LOSE!")
    elif computer_played == 1:
        print("Paper\n"+paper)        
        print("YOU WIN!")
    else:
        print("Scissors\n"+scissors)        
        print("DRAW!")
        
else:
    print("Wrong Selection. Try Again.")