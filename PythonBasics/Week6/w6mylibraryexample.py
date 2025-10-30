def print_ecuador_ascii() -> None:
    E = ["XXXXXXX","X      ","X      ","XXXXX  ","X      ","X      ","XXXXXXX"]
    C = [" XXXXX ","X     X","X      ","X      ","X      ","X     X"," XXXXX "]
    U = ["X     X","X     X","X     X","X     X","X     X","X     X"," XXXXX "]
    A = ["  XXX  "," X   X ","X     X","XXXXXXX","X     X","X     X","X     X"]
    D = ["XXXXXX ","X     X","X     X","X     X","X     X","X     X","XXXXXX "]
    O = [" XXXXX ","X     X","X     X","X     X","X     X","X     X"," XXXXX "]
    R = ["XXXXXX ","X     X","X     X","XXXXXX ","X   X  ","X    X ","X     X"]

    letters = {'E': E, 'C': C, 'U': U, 'A': A, 'D': D, 'O': O, 'R': R}
    word = "ECUADOR"

    for row in range(7):
        line = "  ".join(letters[ch][row] for ch in word)
        print(line)

def greet(name: str) -> str:
    print(f"\n\n\nThanks {name}! For getting this far in the course, Master's Python course - Week 6th.\n")
    print_ecuador_ascii()
    print("\n\nIf you’re reading this message, take a picture (message compiled in console) and let me know — ")
    print("you’ve just earned a special souvenir from my country, Ecuador!🎁")
    return f"\n\nThanks {name}! \n\n\nGreetings from Andre!"