dict = {}
for x in range(3):
    name = input("Enter Student Name: ")
    marks = int(input("Enter marks: "))
    dict[name] = marks

print("Student Records: ")
for name in dict:
    print(name,":",dict[name])
    
