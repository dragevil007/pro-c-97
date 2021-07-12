import random

number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")

while chances<5:
    guess=int(input("enter you guess"))

    if guess==number:
        print("congratulation you won")
     
    elif guess< number:
        print("your guess was too low",guess)

    else:
        print("your guess was too high",guess)


    chances += 1  
     
      
   
    
    

























