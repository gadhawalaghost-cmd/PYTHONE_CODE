# wap to ask the user to enter name of their 3 favorite movies & store them in a list

movie_list=[]
movie1= str(input("enter your 1st favourite movie:"))
movie2= str(input("enter your 2nd favourite movie:"))
movie3= str(input("enter your 3rd favourite movie:"))

movie_list.append(movie1)
movie_list.append(movie2)
movie_list.append(movie3)

print (movie_list)

# wap to check if a list contains a palindrome of eliments.

list1=["w","o","w"]

copy_list1=list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("palindrome true")

else:
    print("palindrome false")

# wap to count the number of students with the "a" grade in the following tuple

grade=["c","d","a","a","b","b","a"]
print(grade.count("a"))

# wap to above value in a list & sort them from "a" to "d".

grade=["c","d","b","a",]
grade.sort()
print(grade)