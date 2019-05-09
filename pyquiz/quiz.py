2.Write a function named sorted that combines and sorts these three lists
['apple','banana','mango']
[‘avocado’,’peach’,’orange’]
[‘pineapple’,lemon’]


def sorted(c,b,a):
	d=c+b+a
	d.sort()
	return d     

def smallest(x):
	return min(x)


4.Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]


m=[ ]
x= [[1,2],[3,4],[5,6]]
for x in l:
for y in x:
m.append(y)


5.Write a Python function named smallest that accepts a list of integers and returns the smallest number in the list. Example:
smallest([1,3,6,8,2,4,5.7]) returns 1


 def smallest([1,3,6,8,2,4,5.7]) 
 return 1

7.Write a function named squares that; Using the range function and a for loop 
creates a dictionary that contains all the numbers between 149 and 159 with
 each number as the key and it’s square as the value



 d=dict()
for x in range(149,160):
    d[x]=x**2
print(d) 



8.Given this list of students and their age,  students = [{‘age’: 19, 'name': ‘Eunice’}, {‘age’: 21, 'name': 'Agnes'}, {‘age’: 18, 'name': 'Teresa'}, {age: 22, 'name': 'Asha'}]
Write a function that greets each student and tells them the year they were born. ~>  “hello {name}, you were born in year {year}” for each student.



def student(name,age):
    student= {"a":"b","c":"d"}
    students=[]
    for student in students:
    	year=2019-(student[age])
        message="Hello {} you were born in {}".format(student["name"],year)
        print(message)
        




	





