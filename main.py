
import sys

# Implement a ls comand or help comand for <= 1 case
def main():
    if len(sys.argv) <= 1:
        print('Need some help?')
    else:
        print(sys.argv)
        match sys.argv[1]:
            case "add":
                print("add task")
            case _:
                print("other")

main()
