print("Welcome to my computer Quiz. ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play! ")
score = 0

answer = input("Who is the current president of kenya? ")
if answer.lower() == "ruto":
    print("correct! ")
    score += 1
else:
    print("Incorrect! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/1) * 100) + "%. ")