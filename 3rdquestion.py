def binary(a,low,high,key):
    while low<=high:
        mid=(low+high)/2
        if key==a[mid]:
            return mid
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

a=[]
n=int(raw_input("enter n"))
print "enter the sorted array"
for i in range(0,n):
    a.append(int(raw_input(" ")))
print "enter k"
k=int(raw_input(" "))
for i in range(0,n):
      find=k-a[i]
      index=binary(a,0,n-1,find)
      if index!=-1:
          break

if index==-1:
    print "not found"
else:
    print i
    print index
      
      
      
      
