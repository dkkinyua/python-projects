def difficulty(diff_input):
    if diff_input == "e":
        tries = 8
        return tries
    elif diff_input == "h":
        tries = 5
        return tries
    elif diff_input == "x":
        tries = 3
        return tries


diff_input = input("Enter difficulty, Easy(E), Hard(H) and Expert(X): ")

print("Initial Tries left: ", difficulty(diff_input))
