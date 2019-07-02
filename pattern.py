def pattern():
    n=int(input("Enter the value-->"))
    k=n
    for i in range(0,n):
        for j in range(0,k-1):
          print(" ",end="")

        k=k-1
        for j in range(0,i+1):
          print("*",end="")
        print("\n")
pattern()
