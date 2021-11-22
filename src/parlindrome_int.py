import sys

def is_palindrome(val:int)->bool:
    """
    This function will check whether the given value is parlindrome or not.
    """
    reversed_val:int = 0
    result:bool = False
    counters:int = 0
    if val>-1 and val<10: #single digit always are palindrome.
        result = True
    elif val>=10 and val%10!=0: #end with 0 are not palindrome, since they lost first digits after reversed.
        while(val>reversed_val): #reversed_val will greater than val when iterate over half position.
            reversed_val=reversed_val*10+(val%10)
            val=int(val/10)
            if val==reversed_val or int(val/10)==reversed_val: #check case even and odd digits.
                result=True
                break
            counters+=1
    return result


