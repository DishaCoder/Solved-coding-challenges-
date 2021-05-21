def sum_binary(bin1, bin2):
    c1 = len(bin1) - 1
    c2 = len(bin2) - 1
    carry = 0
    res = ""
    while c1 >= 0 or c2 >= 0:
        n1 = int(bin1[c1])
        n2 = int(bin2[c2])
        n = n1 + n2 + carry
        if n == 3:
            res = res + "1"
            carry = 1
        elif n == 2:
            res = res + "0"
            carry = 1
        else:
            res = res + str(n)

        c1 = c1-1
        c2 = c2-1
    if carry == 1:
        res = res + str(carry)
        
    return res

output = sum_binary("1001", "0011")
print(output)
for i in range((len(output)-1), (-1)):
    print(output[i], end="")
