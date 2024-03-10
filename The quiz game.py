#The quiz game
print("Welcome tho play computer quiz")

a=input("Do you want to play")
if a != "yes":
    quit()
    
print("Let's begin")    
score=0

b=input("How many states are there in India ?")
if b == ("28"):
    print("correct")
    score+=1
else:
    print("wrong well try")

c=input("Name the father of nation ?")
if c==("Gandhi"):
    print("correct")
    score+=1
else:
    print("wrong well try") 

d=input("Name the national bird")
if d ==("peacock"):
    print("correct")
    score+=1
else:
    print("wrong well try")

e=input("How is the  prime minister of india")
if e ==("narender nath modi"):
    print("correct")
    score+=1
else:
    print("wrong well try")

print("You got" + str(score) + "correct answer") 

score=int(score)
if score == 1:
    print("nice")
elif score ==2:
    print("good")
elif score == 3:
    print("excellent")
elif score == 4:
    print("brillent")
else:
    print("well try")                    