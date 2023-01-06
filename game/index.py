import sys

argumento = sys.argv

print(argumento[1])

def rock_paper_scissors(rounds):
    for i in range((rounds)):
        print(rounds)
        rounds -= 1




# print(rock_paper_scissors(int(input("How many rounds?"))))