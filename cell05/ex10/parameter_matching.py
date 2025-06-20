import sys
def main():
    if len(sys.argv)!=2:
        print("none")
        return
    param=sys.argv[1]
    answer=input("what was the paramenter?")
    if answer==param:
        print("Good job!")
    else:
        print("Nope,sorry...")
main()
