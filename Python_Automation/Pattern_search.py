def isPhoneNumber(text): # Phone number should be in the above format 333-445-9909
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


message = 'I am going out call me to 666-8848-0909 or if not reachable call to 234-4564-9098'

FoundNumber = False

for i in range (len(message)):
    chunk = message[i:i+12]

    if isPhoneNumber(chunk):
        print ('Phone number is found,' + chunk)
        FoundNumber = True

if not FoundNumber:
    print("None of the phone number are not found")