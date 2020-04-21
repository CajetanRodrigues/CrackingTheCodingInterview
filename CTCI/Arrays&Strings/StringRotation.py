'''
The trick is too just replicate the rotated string(s2) twice, and check if the other string(s1) is a
substring of s2

For ex. waterbottle of erbottlewaterbottlewat  
'''
class StringRotation:
    def stringRotation(self,s1:str,s2:str):
        if(len(s1)<=0 and len(s2)<=0 and len(s1)!=len(s2)):
            return False
        s2 = s2+s2
        return self.checkSubstring(s1,s2)
        
    def checkSubstring(self,s1:str,s2:str):
        if s1 in s2:
            return True
        return False

        

obj = StringRotation()
print(obj.stringRotation("waterbottle","erbottlewat"))