'''
Brute force approach

Store the occurences in the dictionary/hashmap.
Iterate through dictionary/hashmap to create the compressed string
Takes additional O(k) space, where k is the number of distinct letters

Optmised approach

Do in place comparison with the next letter and create the compression string on the go
While concatenation, use .join() method (same as javas stringbuilder) which gives O(n) compexity,
Rather than using normal concatenation which is O(n^2)

More Optmised

First do a count of all the char sequences, and check if the string length is smaller than the
orignal string provided, if not, then terminate and return the orignal string only

Imp Note

For normal Concatenation----
Since java strings are immutable each + gets you a new copy of the string. 
So as you were saying, first you build "h", then "he", then "hel" and so on. 
Let's suppose I have an n character string. 
The first + requires building a string of length 2. 
The next plus requires building a string of length 3, and so on for a total cost of 2 + 3 + ... + n. 
This is the arithmetic series (minus 1, but constant differences don't affect big-O). 
The sum of the arithmetic series is (n2 + n) / 2, which is O(n2) (dividing by 2 doesn't change that!). 

For join() / StringBuilder() concatenation

Here the appending happens in O(1) time, so overall TC is O(n)
'''

class StringCompression:
    def compressBad(self,s: str):
        compressStr = ''
        consecutiveCount = 0
        for i in range(len(s)):
            consecutiveCount+=1
            if((i+1)==len(s) or s[i]!=s[i+1]):
                compressStr = compressStr + s[i] + str(consecutiveCount)
                consecutiveCount = 0
        return compressStr if len(compressStr)<len(s) else s

obj = StringCompression()
print(obj.compressBad('aaaabbbccd'))  
        