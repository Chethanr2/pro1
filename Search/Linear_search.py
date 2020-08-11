pos = -1

def search(list, n):

    i = 0
    while (i < len(list)):

        if (list[i] == n):
            globals()['pos'] = i
            return True

        i = i + 1

list = [2,4,89,76,5,10]
n = 5

if search(list, n):
    print("Found in Position", pos)
else:
    print("Not Found")