import random
answer=""
print("\t\t\t!!!Welcome to THE LOTTERY MACHINE!!!")
print("- CORRECT ROW OR COLUMN MEANS U GET 200% THE MONEY")
print("- JACKPOT MEANS YOU GUESS THE EXACT POSITION AND WIN 1000% OF YOUR BET")
print("-"*70)
grid =[ [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
       ]
balance=int(input("How much money would you like to top up:"))

while balance > 0:
    print("Balance: $",balance)
    pos = int(input("What number would you like to guess? (0-99):"))
    while pos<0 or pos>=100:
        print("NOT A VALID NUMBER")
        pos = int(input("What number would you like to guess? (0-99):"))
    bet = int(input("How much would you like to bet:"))
    while bet>balance:
            print("!Bet amount exceeds your balance!")
            bet = int(input("How much would you like to bet:"))
    balance=balance-bet
    X=pos//10
    Y=pos%10
    x=random.randint(0,9)
    y=random.randint(0,9)
    truepos=int((str(x)+str(y)))
    grid[x][y]="$"

    for row in grid:
        for dot in row:
            print(dot,end="  ")
        print()
    print("The real position:",truepos)

    if truepos==pos:
        print("Congratulations you win THE JACKPOT OF $",bet*10,"!!")
        balance=balance+(bet*10)
    elif Y==y:
        print("Correct column you win",bet*2)
        balance = balance + (bet * 2)
    elif X==x:
        print("Correct row you win",bet*2)
        balance = balance + (bet * 2)
    elif truepos!=pos:
        print("SO CLOSE,TRY AGAIN")
    grid = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
            ]
    print("")
    if balance>0:
        print("Balance: $", balance)
        while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
            answer=input("Would you like to withdrawl?(Y,N):")
        if answer=="Y" or answer=="y":
            withdrawl=int(input("How much money would you like to withdrawl:"))
            while withdrawl>balance:
                print("Withdrawl amount is greater than balance")
                withdrawl = int(input("How much money would you like to withdrawl:"))
            balance=balance-withdrawl
            print("You should receive your money in a short moment")
    answer=""
    if balance <=0:
        print("WARNING,you will not be able to countinue betting if you dont top up")
        while answer!="Y" and answer!="y" and answer!="N" and answer !="n":
            answer=input("Would you like to top up? (Y,N):")
            if  answer=="Y" or  answer=="y":
                balance = int(input("How much money would you like to top up:"))
            if answer=="N" or answer=="n":
                print("Thank you for playing with us!")
            else:
                print("Invalid input data,Please try again")
        answer=""