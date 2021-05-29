'''
Given a number n , find if the elements in the list individually
or on summation can give you the number.
say n =7
list = [5,3,4,7]
7 = [7]
7 = [3,4]
Output : Find any of the the combinations 

cont from 1:43:56 , optimisation bacha hai !
'''
def howSum( targetSum , numbers):
    if targetSum == 0 :
        return [ ];
    if targetSum < 0 :
        return None;
    for num in numbers :
        remainder = targetSum - num
        reminder_result = howSum(remainder , numbers)
        if  reminder_result is not None:
            x = reminder_result
            x.append(num)
            return x

    return None

print(howSum(7,[2,3]))

