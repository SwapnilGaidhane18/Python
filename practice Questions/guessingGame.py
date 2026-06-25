import random

jackpot = random.randint(1,100)
guess = int(input("Number guess kar: "))
 
while jackpot != guess : 
    if guess > jackpot : 
        print("guess lowar")
    else :
        print("higher")
    
   
    guess = int(input("Fir se guess kar : "))
print("sahi jawaab!")