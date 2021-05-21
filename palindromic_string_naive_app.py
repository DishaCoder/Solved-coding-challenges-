def isPalindrome(string):
    i = 0
    j = len(string) - 1
    flag = 0
    while(i < j):
        if(string[i] != string[j]):
            flag = 1
            break
        else:
            i += 1
            j -= 1

    if flag == 0:
        return True
    else:
        return False
    

print("Result : ", isPalindrome("disha"))
