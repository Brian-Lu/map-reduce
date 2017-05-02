# Book Text
raw = open("Crime_and_Punishment.txt", "r").read().lower().strip().split();

def freq(word):
    w = word.lower()
    return len([x for x in raw if w == x])

