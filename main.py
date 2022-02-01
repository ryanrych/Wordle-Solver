from random import choice

file = open("words.txt", "r")
words = []
for line in file:
    words.append(line[:-1].lower())
file.close()

rankedLetters = "eariotnslcudpmhgbfywkvxzjq"

letterScores = {}
for i in range(len(rankedLetters)):
    letterScores[rankedLetters[i]] = len(rankedLetters) - i

wordScores = {}

for word in words:
    score = 0
    taken = []
    for i in range(len(word)):
        if word[i] in taken:
            continue
        else:
            score += letterScores[word[i]]
            taken.append(word[i])

    wordScores[word] = [score, False]
wordScores = dict(reversed(sorted(wordScores.items(), key=lambda item: item[1][0])))


target = choice(words)
requirements = {"solved":['*','*','*','*','*'], "contains":[], "out":[]}
correct = False
for i in range(6):
    guess = ""

    for word in wordScores:

        if wordScores[word][1]:
            continue

        flag = True

        for j in range(len(requirements["out"])):
            if requirements["out"][j] in word:
                flag = False
                break

        if not flag:
            continue

        for j in range(5):
            if word[j] != requirements["solved"][j] and requirements["solved"][j] != '*':
                flag = False
                break

        if not flag:
            continue

        for j in range(len(requirements["contains"])):
            if not requirements["contains"][j] in word:
                flag = False
                break

        if not flag:
            continue

        guess = word
        wordScores[word][1] = True
        break

    print("Guessed " + guess)

    if guess == target:
        print("Guessed " + target + " in " + str(i + 1) + " guesses!")
        correct = True
        break

    for j in range(len(guess)):
        if guess[j] == target[j]:
            requirements["solved"][j] = guess[j]
            print("Letter " + guess[j] + " in correct spot")

        elif guess[j] in target:
            requirements["contains"].append(guess[j])
            print("Letter " + guess[j] + " in word")

        else:
            requirements["out"].append(guess[j])


if not correct:
    print("couldn't guess " + target)
