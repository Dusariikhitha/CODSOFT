import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper ->> Paper wins \n"
      + "Rock vs Scissors ->> Rock wins \n"
      + "Paper vs Scissors ->> Scissor wins \n")
while True:
    print("Enter your option1 \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    option = int(input("Enter your option :"))
    while option > 3 or option < 1:
        option = int(input('Enter a valid option please ☺'))
    if option == 1:
        option_name = 'Rock'
    elif option == 2:
        option_name = 'Paper'
    else:
        option_name = 'Scissors'
    print('User option is \n', option_name)
    print('Now its Computers Turn........')
    comp_option = random.randint(1, 3)
    while comp_option == option:
        comp_option= random.randint(1, 3)
    if comp_option == 1:
        comp_option_name = 'RocK'
    elif comp_option == 2:
        comp_option_name = 'Paper'
    else:
        comp_option_name = 'Scissors'
    print("Computer option is \n", comp_option_name)
    print(option_name, 'Vs', comp_option_name)
    if option == comp_option:
        print('Its a Draw', end="")
        result = "DRAW"
    if (option== 1 and comp_option == 2):
        print('paper wins =>>', end="")
        result = 'Paper'
    elif (option == 2 and comp_option == 1):
        print('paper wins =>>', end="")
        result = 'Paper'
    if (option == 1 and comp_option == 3):
        print('Rock wins =>>\n', end="")
        result = 'Rock'
    elif (option == 3 and comp_option == 1):
        print('Rock wins =>>\n', end="")
        result = 'RocK'
    if (option == 2 and comp_option == 3):
        print('Scissors wins =>>', end="")
        result = 'Scissors'
    elif (option == 3 and comp_option== 2):
        print('Scissors wins =>>', end="")
        result = 'Rock'

    if result == 'DRAW':
        print("<== Its a tie ==>>")
    if result == option_name:
        print("<== User wins ==>>")
    else:
        print("<== Computer wins ==>>")
    print("Do you want to play again? (Yes/No)")
    ans = input().lower()
    if ans == 'n':
        break
print("thanks for playing")