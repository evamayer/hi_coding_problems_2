namescore = dict()

def add_namescore():
    name = str(input("Please enter a name: "))
    score = int(input("Please enter a score: "))
    namescore.update({name:score})
    print(namescore)


def subtract_score():
    name = str(input("Please enter a name: "))
    x = int(input("Enter points to be subtracted from score: "))
    score = namescore.get(name)
    new_score = score - x
    namescore[name] = new_score
    print(namescore)

if __name__ == "__main__":
    add_namescore()
    subtract_score()

