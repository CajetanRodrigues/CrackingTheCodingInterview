'''
save top
put bottom to top
put right to bottom
put top to right
'''

class RotateMatrix:
    def rotateMatrix(self,m):
        if(len(m)==0 and len(m)!=len(m[0])): return False
        
        n = len(m)
        for i in range(int(n/2)):
            first = i
            last = n - 1 - i
            for j in range(first,last):
                offset = j - first # 0 1 2 3 # 0 1 
                # save top - so it will go as 00 01 02 03 
                top  = m[first][j]  
                
                # save left to top - so it will go as  30 20 10 00
                m[first][j] = m[last-offset][first] 
                
                # save bottom to left - so it will go as 33 32 31 30
                
                m[last-offset][first] = m[last][last-offset]
                
                # save right to bottom - so it will go as 03 13 23 33 
                
                m[last][last-offset] = m[j][last]
                
                # save top to right - so it will go as 03 13 23 33
                m[j][last] = top
                
        return m
        
obj = RotateMatrix()
M = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(obj.rotateMatrix(M))