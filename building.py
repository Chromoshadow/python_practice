import sys


def dissect(text):
    """Count the characters in text"""
    uppers = 0
    lowers = 0
    punctuations = 0
    spaces = 0
    digits = 0
    for char in text:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isspace() or char == "\r":
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuations += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    args = sys.argv[1:]

    if (len(args) == 0):
        print("What is the text to count?", flush=True)
        try:
            text = sys.stdin.readline()
        except EOFError:
            text = ""
    elif (len(args) == 1):
        text = args[0]
    else:
        raise AssertionError("more than one argument is provided")
    dissect(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
