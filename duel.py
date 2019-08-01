gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gwin = 0
swin = 0

for f, b in zip(gandalf,saruman):
    if f > b:
        print("Gandalf won this clash")
        gwin += 1
    elif b > f:
        print("Saruman won this clash")
        swin += 1
    else:
        print("It is a draw")
if gwin > swin:
    print("Gandalf is the winner")
elif swin > gwin:
    print("Saruman is the winner")
else:
    print("There is a tie")
