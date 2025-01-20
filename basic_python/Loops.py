successful = False
for number in range(1, 4):
    print("Email Attempt", number)
    if successful:
        print(successful)
        break
    else:
        print("Email Attempt failed after", number, "trials")


# Panlindrome implementation


def getValue(userInput):
    run = True
    while run:
        try:
            userInput = userInput.lower()
            if userInput.isalpha() and userInput == userInput[::-1]:
                return True
            elif userInput == "exit":
                run = False
                return False
        except ValueError as e:
            print("check Invalid value", e)


if __name__ == "__main__":
    print(getValue("Radar"))
