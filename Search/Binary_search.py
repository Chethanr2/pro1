pos = -1

def search (list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l + u) // 2

        if (list[mid] == n):
            globals()['pos'] = mid
            return True
        else:
            if (list[mid] < n):
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [2,5,8,10,445,789,9909,99876,152637]
n = 5

if search(list,n):
    print("found at position", pos+1)
else:
    print("Not Found")