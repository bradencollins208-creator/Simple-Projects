ls=[]
ls.append("_____")
ls.append("|   |")
ls.append("|   O")
ls.append("|  /|\\")
ls.append("|  / \\")
ls.append("|")
word = input("Enter word: ")
blankWord=""
wordLs=[]
for i in word:
    blankWord+=("_ ")
print(blankWord)
while True:
    guess=input("Enter guess: ")
    for i in word:
        if guess==i:
            print("true")
            break
    if guess=="0":
        break