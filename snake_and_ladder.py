#snake_and_ladder_program

rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
rows = reversed([reversed(rows[i]) if i%2 else rows[i] for i in range(len(rows))])
#creating grid

for row in rows:
    print(' | '.join(row)) #to join rows
    
import random #creating a die
count = 0 #initial count
while(count<=100): #max. count is 100
    a=input("enter 'r' to roll the dice:")
    if(a=='r'): #equality operator
        r=random.randint(1,6) #random number to be chosen in the given range
        count=count+r #value of count
        print(count)
        print(r)
        if (count==8):
            count=37 #condition to climb the ladder
            print("climb up the ladder")
        elif (count==13):
            count=34 #condition to climb the ladder
            print("climb up the ladder")
        elif (count==40):
            count=68 #condition to climb the ladder
            print("climb up the ladder")
        elif (count==52):
            count=81 #condition to climb the ladder
            print("climb up the ladder")
        elif (count==76):
            count=97 #condition to climb the ladder
            print("climb up the ladder")
        elif (count==11):
            count=2 #condition to come down
            print("ah! come down, the snake bit")
        elif (count==25):
            count=4 #condition to come down
            print("ah! come down, the snake bit")
        elif (count==38):
            count=9 #condition to come down
            print("ah! come down, the snake bit")
        elif (count==65):
            count=46 #condition to come down
            print("ah! come down, the snake bit")
        elif (count==89):
            count=70 #condition to come down
            print("ah! come down, the snake bit")
        elif (count==93):
            count=64 #condition to come down
            print("ah! come down, the snake bit")        
        elif (count==100):
            print("the player won") #condition to end the game
            break
        
while(count>100):
    print("invalid! roll the dice again") #condition given not to cross the count
    break








