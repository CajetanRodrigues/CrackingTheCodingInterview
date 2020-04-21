'''
ask the interviewer what type of string it is

https://stackoverflow.com/questions/19212306/whats-the-difference-between-ascii-and-unicode
ascii - 128 chars
extended ascii - 256 chars
unicode - 2^21 chars

'''
class IsUnique:
    def isUnique(self,s: str):
        # Assuming ascii string
        if len(s)>128:
            return False
        boolArray = [0]*128
        for index,ele in enumerate(s):
            if(boolArray[ord(str(ele))]==1):
                return False
            boolArray[ord(str(ele))]=1
        return True
obj = IsUnique()
print(obj.isUnique('abd'))
            
''' 
Tips

ord() converts char to ascii value
chr() converts ascii value to char

If no datastructures are allowed:

1. check every char with every other char -> O(n^2)
2. Sort the entire string and check linearly -> O(nlog(n))
'''