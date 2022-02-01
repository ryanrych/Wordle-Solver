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

    wordScores[word] = score

