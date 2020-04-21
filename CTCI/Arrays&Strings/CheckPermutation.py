# is the permutation comparison case sensitive?
# is the permutation comparison white space sensitive?

# soln 1: find all permutations of one & check if it contains the other O(n!)
# soln 2: compute char counts in first string, and then decrease the count for second string, if count<0, then False O(n)
# soln 3: sort the strings and then check if both are identical O(nlog(n))


class CheckPermutation:
    def checkPermutation(self,str1: str,str2: str):
        if(len(str1)!=len(str2)): 
            return False
        str1.sort()
        str2.sort()
        if(str1==str2):
            return True
        return False
    
        