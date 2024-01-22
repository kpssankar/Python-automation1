list = [10,501,22,37,100,999,87,351]
even_numbers=[]
odd_numbers=[]
for i in list:
    if (i  % 2==0):
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("even list:" ,even_numbers)
print ("odd list:",odd_numbers)   


Output:
=========
Output:

even list: [10, 22, 100]
odd list: [501, 37, 999, 87, 351]



===================================================================================================================================================
#program to filter prem numbers from give list
def is_prime(n):
  """
  Checks if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """

  if n <= 1:
    return False
  for i in range(2, n-1):
    if n % i == 0:
      return False
  return True
list = [10,501,22,37,100,999,87,351,7]
num = len(list)
prime_numbers = []
for num in list:
  if is_prime(num):
    prime_numbers.append(num)
print(prime_numbers)

Output:

[37, 7]





===============================================================================================================================================

#Python Program to Find Sum of First and Last Digit

number = 1247
 
number = str(number)
 

first_digit = int(number[0])
last_digit = int(number[-1])
 
addition = first_digit + last_digit
 

print('Addition of first and last digit of the number is', 
      addition)

Output:

Addition of first and last digit of the number is 8

====================================================================================================================================================

#program to find duplicates between three lists
list1=[3,4,5,6,7,8,9,11,22]
list2=[9,8,7,6,5,4,3,2,1,11]
list3=[1,2,3,4,5,9,8,7,6,5,22]
duplicate_list1and2= (set(list1).intersection(list2))
duplicate_list1and3= (set(list1).intersection(list3))
duplicate_list2and3= (set(list2).intersection(list3))
print("duplicate between list1and2:" ,duplicate_list1and2)
print("duplicate between list1and3:",duplicate_list1and3)
print("duplicate between list2and3:", duplicate_list2and3)

Output:
duplicate between list1and2: {3, 4, 5, 6, 7, 8, 9, 11}
duplicate between list1and3: {3, 4, 5, 6, 7, 8, 9, 22}
duplicate between list2and3: {1, 2, 3, 4, 5, 6, 7, 8, 9}
==================================================================================================================================================

#program to find first non repeating element in given list

def firstNonRepeating(list, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if  element is present in list
        while(j < n):
            if (i != j and list[i] == list[j]):
                break
            j += 1
        # if the element is not present in array
        # except at ith index then return element
        if (j == n):
            return list[i]
 
    return -1
 
 
# Driver code
list = [9, 4, 9, 10, 7, 4]
n = len(list)
print(firstNonRepeating(list, n))

==================================================================================================================================================

# python program to find minimum element in sorted list
 
def findMin(list, N):
     
    min_ele = list[0];
 
    # Traversing over array to
    # find minimum element
    for i in range(N) :
        if list[i] < min_ele :
            min_ele = list[i]
 
    return min_ele;
 
# Driver program
list_1 = [5, 6, 1, -1, 2, 3, 4]
N = len(list_1)
list=sorted(list_1)
 
print(findMin(list,N))
 

 Output:

-1

===========================================================================================================================================
