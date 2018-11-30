def reverse(sentence):
    if sentence == "":
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

def palindrome(sentence):
    another_sentence = reverse(sentence)
    return another_sentence == sentence

def main():
    sentence = input("Enter a string:\n")
    if palindrome(sentence):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

if __name__ == "__main__":
    main()