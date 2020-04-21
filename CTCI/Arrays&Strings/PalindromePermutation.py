class PalindromePermutation:
    def checkPalindromePermutation(self,s: str):
        charTable = [0]*26
        for char in s:
            char = char.lower()
            charTable[ord(char)-ord('a')]+=1
        flag=0
        print(charTable)
        for x in range(len(charTable)):  
            if x%2==0:
                pass
            else:
                if(x==1):
                    if flag==0:
                        flag=1
                    else:
                        return False

        return True
        
obj = PalindromePermutation()
print(obj.checkPalindromePermutation('mmalayalamm'))