ans=0
f=open("latex.log")
txt=f.readlines()
dic={}
for lines in txt:
    if dic.get(lines,0)==0:
        dic[lines]=1
        ans+=1
    elif dic[lines]==1:
        dic[lines]=2
        ans-=1
print("共{}独特行".format(ans))
---
f = open("latex.log")
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))
# 记住：如果需要"去重"功能，请使用集合类型。
   
# ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现。