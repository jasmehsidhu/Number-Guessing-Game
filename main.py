import random
random=random.randint(1,100)
while True:
  Guess=int(input("Guess the Number: "))
  if(Guess<random):
    print("Try a Higher Number")
  elif(Guess>random):
    print("Try a lower number")
  else:
    print("you won")
    break
