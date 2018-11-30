def pairs(sentence):
    if sentence == "":
        return 0
    elif len(sentence) == 1:
        return 0
    elif sentence[0] == sentence[1]:
        return 1 + pairs(sentence[2:])
    else:
        return pairs(sentence[1:])

def main():
    sentence = input("Enter a message:\n")
    print("Number of pairs: " + str(pairs(sentence)))

if __name__ == '__main__':
    main()