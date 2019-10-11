def check(str1):
   list1, para=[],{"[":"]","(":")","{":"}"}
   for x in str1:
        if x in para:
            list1.append(x)
        elif para[list1.pop()]!=x:
            return "invalid"
        if len(list1)==0:
           return "valid"

b=input('enter the string')
a=check(b)
print(a)
