'''
Given a number n , find if the elements in the list individually
or on summation can give you the number.
say n =7
list = [5,3,4,7]
7 = [7]
7 = [3,4]
Output : True or false

'''
import time

def canSum( targetSum , my_list, my_hash ={} ) :
    if targetSum in my_hash:
        return my_hash[targetSum]

    #Base case  
    if targetSum == 0 :
        return True;
    #-ve numbers ko avoid karne ke liye
    if targetSum < 0 :
        return False;
        
    for x in my_list:
            if(canSum(targetSum - x , my_list, my_hash) == True):
                my_hash[targetSum] = True
                return True

    my_hash[targetSum]= False            
    return False


print (canSum(7,[2,4], {})) # False
print (canSum(300,[7,14], {})) # false
print (canSum(7,[5,3,4,7], {})) #True
print (canSum(8,[2,3,5], {})) #True
print( canSum(7,[2,3], {}) ) #True


