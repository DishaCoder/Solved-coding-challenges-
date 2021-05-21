global remlist
remlist = list()
def toHex(decimal):
    if(decimal > 0):
        rem = decimal % 16
        decimal = int(decimal / 16)
        remlist.append(rem)
        toHex(decimal)

toHex(125)
for i in remlist:
    print(i)
for i in remlist:
    if (i == 10):
        remlist[i] = 'a'
    if i == 11:
        remlist[i] = 'b'
    if i == 12:
        remlist[i] = 'c'
    if i == 13:
        remlist[i] = 'd'
    if i == 14:
        remlist[i] = 'e'
    if i == 15:
        remlist[i] = 'f'
hexStr = ''
for i in range((len(remlist)-1), -1, -1):
    hexStr = hexStr + str(i)

print(hexStr)
    
    

        
    
