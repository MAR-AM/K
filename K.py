#Here is an example of an algorithm in Python that displays the divisors of a user-entered integer.
#Before the At the end of its execution, the algorithm must display the number of divisors it has found
n=int(input('Enter a number : '))
dividers=[]
for divider in range (1,n+1):
  if n % divider==0:
    dividers.append(divider)
print('the number of divisors : ',len(dividers))
print('the dividers of ',n,'are :',dividers)
