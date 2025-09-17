import random

def swg(comp, mine):
    if comp==mine:
        return None
    elif comp == "s" and mine == "g":
        return True
    elif comp == "w" and mine == "s":
        return True
    elif comp == "g"  and mine == "w":
        return True
    else:
        return False

choice = ('s', 'w', 'g')
comp=random.randint(0,2)
comp=choice[comp]
mine=input("Enter your choice s, w or g: ")

win=swg(comp, mine)
print(f"You choose {mine} and comp choosen {comp}")
if win is None:
    print("Match Drawn")
if win:
    print("You Won the Game")
else:
    print("You Lose the Game")

