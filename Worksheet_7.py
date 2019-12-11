# Worksheet 7


# List the four types of data we've covered, and give an example of each:
# we studied, the types below:
string = "This is a string"
integer = 7
float = 7.32
boolean = True
tuple = ("This is a string inide a tuple", 7, 7.32, False)
list = ["This is a string inide a list", 7, 7.32, False]


# What does this code print out?
# For this and the following problems, make sure you understand WHY it prints what it does.
# You don't have to explain it, but if you don't understand why, make sure to ask. Otherwise you are wasting your time doing these.
# my_list = [5, 2, 6, 8, 101]
# print(my_list[1])
# print(my_list[4])
# print(my_list[5])
    # It will print 2, 101 and and error for the last line of code.


# What does this code print out?
# my_list=[5, 2, 6, 8, 101]
# for my_item in my_list:
#     print(my_item)
    # it will print out the elements of the list, one by one, in the same order and in a vertical line


# What does this code print out?
# my_list1 = [5, 2, 6, 8, 101]
# my_list2 = (5, 2, 6, 8, 101)
# my_list1[3] = 10
# print(my_list1)
# my_list2[2] = 10
# print(my_list2)
    # This will print out an error when trying to change the item in list 2, because it is a tuple, and so, it is immutable, if we remove that line, it will print out the following:
    # [5, 2, 6, 10, 101]
    # (5, 2, 10, 8, 101)


# What does this code print out?
# my_list = [3 * 5]
# print(my_list)
# my_list = [3] * 5
# print(my_list)
    # It prints out:
    # [15]
    # [3, 3, 3, 3, 3]


# What does this code print out?
# my_list = [5]
# for i in range(5):
#     my_list.append(i)
# print(my_list)
    # It prints out:
    # [5, 0, 1, 2, 3, 4]


# What does this code print out?
# print(len("Hi"))
# print(len("Hi there."))
# print(len("Hi") + len("there."))
# print(len("2"))
# print(len(2))
    # it prints out:
    # 2
    # 9
    # 8
    # error, because we cannot measure the lenght of an integer


# What does this code print out?
# print("Simpson" + "College")
# print("Simpson" + "College"[1])
# print( ("Simpson" + "College")[1] )
    # it prints out:
    # SimpsonCollege
    # Simpsono
    # i


# What does this code print out?
# word = "Simpson"
# for letter in word:
#     print(letter)
    # it prints out Simpson vertically, one charecter per line


# What does this code print out?
# word = "Simpson"
# for i in range(3):
#     word += "College"
# print(word)
    # it prints out:
    # SimpsonCollegeCollegeCollege


# What does this code print out?
# word = "Hi" * 3
# print(word)
    # it prints out:
    # HiHiHi


# What does this code print out?
# my_text = "The quick brown fox jumped over the lazy dogs."
# print("The 3rd spot is: " + my_text[3])
# print("The -1 spot is: " + my_text[-1])
    # it prints out:
    # The 3rd spot is:  (with double spacing in the end of the phrase)
    # The -1 spot is: .


# What does this code print out?
# s = "0123456789"
# print(s[1])
# print(s[:3])
# print(s[3:])
    # it prints out:
    # 1
    # 012
    # 3456789


# Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. Try doing this without looking at the book.
user_array = [0,1,2,3,4]
for item in range(5):
    user_array[item] = int(input("Please insert a number: "))
print(user_array)

# Write a program that take an array like the following, and print the average. Use the len function, don't just use 15, because that won't work if the list size changes.
# (There is a sum function I haven't told you about. Don't use that. Sum the numbers individually as shown in the chapter.)
# (Also, a common mistake is to calculate the average each time through the loop to add the numbers. Finish adding the numbers before you divide.)
# my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

my_list_sum = 0
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

for item in range(len(my_list)):
    my_list_sum += my_list[item]
my_list_average = my_list_sum / len(my_list)
print (my_list_average)