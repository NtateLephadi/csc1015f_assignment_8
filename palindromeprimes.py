from palindrome import *

def prime(palindrome, denominator):
    if palindrome == 0 or palindrome == 1:
        return 0
    elif palindrome == 2:
        return 1
    elif palindrome % (denominator) == 0 and denominator > 1:
        return prime(1, 0)
    elif denominator < 2:
        return prime(2, 1)    
    else:
        return prime(palindrome, denominator - 1)

def palindromeprime(N, M):
    if N > M:
        quit()
    elif palindrome(str(N)):
        if prime(int(N), int(N - 1)) > 0:
            print(N)
            return palindromeprime(N + 1, M)
        else:
            return palindromeprime(N + 1, M)
    else:
        return palindromeprime(N + 1, M)

def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palindromeprime(N, M)

if __name__ == '__main__':
    main()