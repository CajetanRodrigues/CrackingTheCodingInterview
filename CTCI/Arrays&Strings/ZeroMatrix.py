class ZeroMatrix:
    def zeroMatrix(self,a):
        # check if first row has zero, lateron we have to set it as 0
        m = len(a)
        n = len(a[0])
        rowHasZero = 0
        for i in range(m):
            if(a[0][i]==0):
                rowHasZero = 1
                break
        
        # check if first column as zero, lateron we have to set it as 0
        columnHasZero = 0
        for i in range(n):
            if(a[i][0]==0):
                columnHasZero = 1
                break
        
        # if any element is zero, set corresponding row and column to 0
        for i in range(1,m):
            for j in range(1,n):
                if(a[i][j]==0):
                    a[i][0] = 0
                    a[0][i] = 0
        
        for i in range(m):
            if(a[i][0]==0):
                self.nullifyRow(a,i)
                
        for i in range(n):
            if(a[0][i]==0):
                self.nullifyColumn(a,i)
        
        if(rowHasZero): self.nullifyRow(a,0)
        if(columnHasZero): self.nullifyColumn(a,0)
        # whichever row/column element in the first element has 0, set it to zeroes all correspoding row/column
        
        return a
    
    def nullifyRow(self,a,x):
        n = len(a[0])
        for i in range(n):
            a[x][i] = 0
            
    def nullifyColumn(self,a,x):
        m = len(a)
        for i in range(m):
            a[i][x] = 0

obj = ZeroMatrix()
a = [
    [5,2,0,3],
    [4,2,3,5],
    [5,7,8,4],
    [7,5,4,6]
]
print(obj.zeroMatrix(a))