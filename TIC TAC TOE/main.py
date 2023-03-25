import os
import random
 
g = []
won = False
 
for i in range(9):
    g.append('.')
    
choice=int(input("1:Player vs player or 2:Player vs Bot "))

if choice == 1:
    
    for _ in range(10):
     os.system('cls')
     for i in range(9):
        print(g[i], end='')
        if (i+1) % 3 == 0:
            print()
 
     if g[0] == g[1] == g[2] != '.' or \
         g[3] == g[4] == g[5] != '.' or \
         g[6] == g[7] == g[8] != '.' or \
         g[0] == g[3] == g[6] != '.' or \
         g[1] == g[4] == g[7] != '.' or \
         g[2] == g[5] == g[8] != '.' or \
         g[0] == g[4] == g[8] != '.' or \
         g[2] == g[4] == g[6] != '.':
         print(g[x-1], 'WON!')
         break
     
     elif '.' not in g:
         print("Draw")
         break
     

 
     x = int(input(">"))
 
     if g[x-1] == '.':
         g[x-1] = 'X' if _ % 2 == 0 else 'O'
     else:
         while g[x-1] != '.':
             x = int(input(">"))
        
         g[x-1] = 'X' if _ % 2 == 0 else 'O'    
elif choice==2:
    for _ in range(9):
        os.system('cls')
        for i in range(9):
            print(g[i], end='')
            if (i+1) % 3 == 0:
                print()

        if _ % 2 == 1:
            while True:
                bot = random.randint(1, 10)
                if g[bot-1] == '.':
                    g[bot-1] = 'O'
                    break
          
           
        else:
            x = int(input(">"))
       
            while g[x-1] != '.':
                x = int(input())
            g[x-1] = 'X'

        
        if g[0] == g[1] == g[2] != '.' or \
            g[3] == g[4] == g[5] != '.' or \
            g[6] == g[7] == g[8] != '.' or \
            g[0] == g[3] == g[6] != '.' or \
            g[1] == g[4] == g[7] != '.' or \
            g[2] == g[5] == g[8] != '.' or \
            g[0] == g[4] == g[8] != '.' or \
            g[2] == g[4] == g[6] != '.':
            print(g[x-1], 'WON!')
            break





        