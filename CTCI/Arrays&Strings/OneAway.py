'''
Brute force approach

Find all possible inserts,replaces and deletes of the first string and compare with the second string
This would take ample amount of time, dont know how much

Optimised approach

For Replace, 1 char is only mismatched, rest all are same
For Insert,Delete, 1 char is missing, rest all are same

'''

class OneEditWay:
    def oneEditAway(self,s1: str,s2:str):
        if(len(s1)==len(s2)):
            return self.oneEditReplace(s1,s2)
        elif (len(s1)+1 == len(s2)):
            return self.OneEditInsertDelete(s1,s2)
        elif (len(s1)==len(s2)+1):
            return self.OneEditInsertDelete(s2,s1)
    def oneEditReplace(self,s1: str, s2:str):
        indexOfs1 = 0
        indexOfs2 = 0
        flag = 0
        for i in range(len(s1)):
            if(flag==1): return False
            if (s1[indexOfs1]!=s2[indexOfs2]):
                flag==1
            indexOfs1+=1
            indexOfs2+=1
        return True
    def OneEditInsertDelete(self,s1:str,s2:str):
        indexOfs1 = 0
        indexOfs2 = 0
        flag = 0
        for i in range(len(s1)):
            if(flag==1): return False
            if (s1[indexOfs1]!=s2[indexOfs2]):
                indexOfs2+=1
                flag==1
            indexOfs1+=1
            indexOfs2+=1
        return True

obj = OneEditWay()
print(obj.oneEditAway('pale','pal'))
print(obj.oneEditAway('pal','pale'))
print(obj.oneEditAway('pale','bale'))

'''
Time Complexity: O(n) where n is length of the shorter string
'''
