
try:
    num = int(input("Enter a number:"))
    print(num)
except ValueError:
    print("This is not a number. Enter a number")


###############################################


x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print("This is a list")

elif type(x) is set:
    print("This is a set")

elif type(x) is tuple:
    print("This is a tuple")

else:
    print("Neither of all is either a set, tuple or list")


########################################################


def divisible(num1, num2):

    # num1 = int(input("Enter a number to divide: "))
    # num2 = int(input("Enter a number to divide with: "))

    if num1 % num2 == 0:
        return True
    else:
        return False


print(divisible(7, 4))
print(divisible(64, 2))


##########################################################

def remove_nums(int_list):
    position = 3 - 1
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position+idx) % len_list
        print(int_list.pop(idx))
        len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)


##############################################################

a = int(input("Input an interger: "))
n1 = int( "%s" % a)
n2 = int( "%s" "%s" % (a, a))
n3 = int("%s" "%s" "%s" % (a,a,a))
print(n1 + n2 + n3)


#############################################################


def sumthrce(a,b,c):
    sum = a + b + c

    if a == c == c:
        sum = sum * 3
    return sum

print(sumthrce(1,2,3))
print(sumthrce(3,4,5))

    #if a == b == c:


##############################################################


userInput = str(input("Enter a string: "))
palindrome_reverse = userInput[::-1]

if userInput == palindrome_reverse:
    print("This word is a palindrome")

else:
    print("This word is not a palindrome")

##########################################################


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlist = []

for i in a:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)


###############################################################


import random

a = random.randint(1, 9)
guess = 0
count = 0

while guess != a and guess != "exit":
    guess = int(input("Guess a number between 1 and 9: "))
    count += 1

    if guess == "exit":

        print("You have exited")
    elif guess > a:
        print("Too high")
    elif guess < a:
        print("Too low")
    else:
        print("You got it right")
        print("Number of times played", count)


##########################################################################


L = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        L.append(str(i))

print(','.join(L))


#################################################################


n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)


#################################################################


raw_input = input("Enter number and comma to seperate them: ")
listed = raw_input.split(",")
tupled = tuple(listed)
print(listed)
print(tupled)


###################################################################


import math
c = 50
h = 30
value = []

d = input("enter a number: ").split(',')
q = math.sqrt((2 * c * float(d)/h))

for x in d:
    value.append(str(int(round(q))))

print(',').join(value)



################################################################


userInput = input().split(',')
print("user Input is: ", userInput)
userInput.sort()
print(','.join(userInput))


####################################################################


import math
c = 50
h = 30
value = []
item = input("Enter a value: ").split(",")
for d in item:
    value.append(str(int(round(math.sqrt(2 * c * float(d)/h)))))

print((','.join(value)))

###########################################################

nums = input("Enter list of numbers: ").split(",")
lenght_nums = len(nums)
print("length of 'nums' is: ", lenght_nums)

fifth_nums = nums[5]
print("The fifth element of 'nums' is: ", fifth_nums)


#########################################################


# Write a Python program that accepts an integer and determines whether
# it is greater than 4^4 and which is 4 mod 34.

nums = int(input("Enter a list of numbers: "))

def test(nums):
    return nums % 34 == 4 and nums > 4 ** 4

print(test(nums))


#####################################################################


# Write a Python program to add 'ing' at the end of a given
# string (length should be at least 3). If the given string
# already ends with 'ing', add 'ly' instead. If the string
# length of the given string is less than 3, leave it unchanged.





sample_string = input("Enter a string: ")
expected_result = ''
if len(sample_string) >= 3:
    expected_result = sample_string + 'ing'
    print(expected_result)

elif "ing" in sample_string:
    expected_result = sample_string + "ly"
    print(expected_result)

elif len(sample_string) < 3:
    print(sample_string)



#########################################################################



