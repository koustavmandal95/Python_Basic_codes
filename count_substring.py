def count_substring(string, sub_string):
    count=0
    len_sub=len(sub_string)
    for i in range(0,len(string)):
        if string[i:(i+len_sub)]==sub_string:
            count=count+1
            #print(string[i:i+len_sub])
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
