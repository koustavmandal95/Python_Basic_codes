def swap_case_worst(s):
    s=list(s)
    new_string=[]
    for i in range(0,len(s)):
        if s[i]==' ':
            new_string=new_string+[s[i]]
        elif s[i] in "!@#$%^&*()><?}{[].,123456789\"":
            new_string=new_string+[s[i]]
        elif s[i] in '\"qqwertypasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"':
            if s[i].isupper()==True:
                new_string=new_string+[s[i].lower()]
            elif s[i].islower()==True:
                new_string=new_string+[s[i].upper()]
        elif s[i].isupper()==True:
            new_string=new_string+[s[i].lower()]
        elif s[i].islower()==True:
            new_string=new_string+[s[i].upper()]
        else:
           return -1
    '''
    print(new_string)
    string=[str(i) for i in new_string]
    print(string)
    '''
    res = "".join(new_string)
    return res
def swap_case(s):#Best and smaller code 
    s=list(s)
    new_string=[]
    for i in range(0,len(s)):
        if s[i].isalpha()==False:
            new_string=new_string+[s[i]]
        elif s[i].isupper()==True:
            new_string=new_string+[s[i].lower()]
        elif s[i].islower()==True:
            new_string=new_string+[s[i].upper()]
        else:
           return -1
    new_string = "".join(new_string)
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''
if __name__ =='__main__':
    s = input()
    result = swap_case(s)
    result="".join(result)
    print(result)
#HackerRank.com presents "Pythonist 2".
#output-->hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
        '''
        elif s[i] in '\"qwertypasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()><?}{[].,+-_"':
            if s[i].isupper()==True:
                new_string=new_string+[s[i].lower()]
                print("i and here")
            elif s[i].islower()==True:
                new_string=new_string+[s[i].upper()]
        '''
