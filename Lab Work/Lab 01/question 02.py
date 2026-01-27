num = int(input("Enter a number: "))
print("Even Numbers: ",end=" ")
count=0;
for x in range(1,num+1):
    if (x%2==0):
        print(x,end=" ")
        count = count+1
print()
print("Total Even Numbers: ",count)
        
