def pairs(sentence):
    sentence = sentence.split()
    count = 0
    for i in sentence:
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                count += 1
    return count

print(pairs("hello, Salaama"))