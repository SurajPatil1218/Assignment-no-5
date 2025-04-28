## Task no 1

List = {'Alice':85,'Raj':80,'Jatin':90}
n = input("Entre the student's name :")
if n in List:
    print("Alice marks is :",List[n])
else:
    print("student not found")

Output:
Entre the student's name : Alice
Alice marks is : 85

List = {'Alice':85,'Raj':80,'Jatin':90}
n = input("Entre the student's name :")
if n in List:
    print("Alice marks is :",List[n])
else:
    print("student not found")

Output:
Entre the student's name : Suraj
student not found


## Task no 2

x = [1,2,3,4,5,6,7,8,9,10]
print("Original list : ",x)

Output:
Original list :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = [1,2,3,4,5,6,7,8,9,10]
print("Extract first five elements : ",x[:5])

Output:
Extract first five elements :  [1, 2, 3, 4, 5]

x = [1,2,3,4,5,6,7,8,9,10]
print("Reversed extracted element : ",x[-6::-1])

Output:
Reversed extracted element :  [5, 4, 3, 2, 1]