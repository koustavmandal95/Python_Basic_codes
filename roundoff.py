def roundoff(grades):
    for i in range(0,len(grades)):
        if grades[i]>37:
            rem=grades[i]%5
            if (5-rem)<3:
                grades[i]=grades[i]+(5-rem)
            else:
                grades[i]=grades[i]
        else:
             grades[i]=grades[i]
    return grades 
if __name__=="__main__":
    grade_count=int(input().strip())
    grades=[]
    for _ in range(grade_count):
        grade_item=a=int(input("Enter the input --->").strip())
        grades.append(grade_item)
    result=roundoff(grades)
    print(result)


