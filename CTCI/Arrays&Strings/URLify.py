class URLify:
    def urlify(self,s: str):
        s = s.strip()
        s = s.replace(' ','%20')
        return s
obj = URLify()
print(obj.urlify('Mr John Smith    '))