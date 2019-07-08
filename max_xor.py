first=int(input("enter the number"))
second=int(input("enter the second number"))
def maxzor(first,second):
    answer=[]
    for i in range(first,second+1):
        for j in range(i,second+1):
            xor_ans=i^j
            answer=answer+[xor_ans]
    print("The max is -->",max(answer),answer)
        
maxzor(first,second)
