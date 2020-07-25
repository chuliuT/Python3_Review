
arr = "wwwrunoobcom"

def countSort(arr):
    dict={}
    for i in arr:
        dict[i]=0
    for i in arr:
        dict[i]+=1
    res=[]
    for key in sorted(dict.keys()):
       res.append(key*dict[key])
    return "".join(res)

ans=countSort(arr)
print(ans)