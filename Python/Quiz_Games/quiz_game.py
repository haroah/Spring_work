print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Let's play :D")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the original name for a phone? ")
if answer.lower() == "speaking telegraph":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does NPC stand for? ")
if answer.lower() == "non player character":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got "  +  str(score)  +  " questions correct!")
print("You got "  +  str((score/4) * 100)  +  "%.")
