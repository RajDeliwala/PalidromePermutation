'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
Palidrome Permutation
Problem Statement: Given a string, write a function to check if it is  apermutation of a palindrone, A palindrone is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palidrone does not needed to be limited to just dictionary words. You can ignore casting and non-letter characters
example:
    input: Tact coa
    output: True because one of the permutation is Taco Cat which is the same forwards and backwards ie. "atco cta"
Constraits or Questions you need to ask:
- Not case sensitive and no non-letters
- does not need to be limited to dictionary words
Solution notes:
- Given a string, get a list of possible permutations of it
- Check each permutation if it's possibly a palidrome
- t a c o c a t ->2(t) 2(a) 2(c) and only 1(o)
 seems like we can have even numbers of x characters and only 1 character of an odd number
'''
from itertools import permutations


#Brute force, seems like a O(n^2 * n!)
def permutation_palidrome(string):

    #Remove any spaces and any cap issues
    string = string.replace(" ", "")
    string = string.lower()

    #Getting list of all possible permutations on string given as lists of indivdual chars
    a=permutations(string)

    #Join the lists into forward and backward strings to see if they match, if they do. They are indeed Palidrome permutations
    for i in a:
        forward = ("".join(i))
        backward = forward[::-1]
        if (forward == backward):
            return True
        else:
            return False

print(permutation_palidrome("taco cat") == True)
print(permutation_palidrome("Testing gnitset") == True)
print(permutation_palidrome("tacocat") == True)
print(permutation_palidrome("race car") == True)
print(permutation_palidrome("racecar") == True)


'''
let's try a more effiecent method using hash table
Example: taco cat
t a c o c a t -> We have 2(t)s 2(a)s 2(c)s and 1(o)
We should have an all even amount of letters and only 1 odd number
for it to be a perm palidrome

Iterate through the string and add each char into
the hash table and update the key +1 if it already exist

We also count the amount of odd chars in the hash table
and make sure it's only 1, if more than 1 then it's false
'''
#Time complexity of O(n) where n is the number of char in the string
def is_palin_perm(string):
    #Get rid of anomalies of spaces and caps
    string = string.replace(" ", "")
    string = string.lower()

    #intialize a dictionary
    d = dict()

    #For eacg character in string
    for char in string:
        #if that char already exist in the dictionary
        if char in d:
            #Update it's key by 1
            d[char] += 1
        #if it's the first time seeing that char
        else:
            d[char] = 1

    #Odd counter for more than 1 odd char in string 
    odd_counter = 0

    #For each key and value pair in dictionary
    for key, value in d.items():
        #if the value of said char is odd and odd counter is 0 add 1 to odd counter
        if value % 2 != 0 and odd_counter == 0:
            #Adding 1 t odd counter
            odd_counter += 1
        #Else if value of said char is odd and odd counter doesn't equal 0
        elif value % 2 != 0 and odd_counter != 0:
            #Return False
            return False
    #Return True
    return True

print(is_palin_perm("taco cat") == True)
print(is_palin_perm("Testing nope") == False)
print(is_palin_perm("tacocat") == True)
print(is_palin_perm("race car") == True)
print(is_palin_perm("racecar") == True)


