n =int(input("enter the number "))
n1=int(input("enter the ending number"))

def sum_digit(n):
    sum_fact=0
    while n>0:
        rem=n%10
        fact=1
        
        while rem>0:
            fact=fact*rem
            rem=rem-1
        n=n//10
        sum_fact=sum_fact+fact
    return sum_fact
def compare():
    for i in range(n,n1):
        a=sum_digit(i)
        if i==a:
            print("\n")
            print(" The number found is --->",i)
            continue
if __name__=="__main__":
    compare()
