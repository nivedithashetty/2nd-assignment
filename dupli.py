a=[0,0,0,0,0,0,0,0,0]

def mergeSort(arr,low,mid,high):
    temp=[0,0,0,0,0,0,0,0,0,0,0]
    l=low;
    i=low;
    m=mid+1;
    while l<=mid and m<=high:
        if(arr[l]<=arr[m]):
             temp[i]=arr[l]
             l=l+1
        else:
            temp[i]=arr[m]
            m=m+1
        i=i+1


    if l>mid:
        for k in range(m,high+1):
             temp[i]=arr[k];
             i=i+1
         
    else:
        for k in range(l,mid+1):
            temp[i]=arr[k]
            i=i+1
   
    for k in range(low,high+1):
        arr[k]=temp[k]
   
def partition(arr,low,high):
    if(low<high):
        mid=(low+high)/2
        partition(arr,low,mid)
        partition(arr,mid+1,high)
        mergeSort(arr,low,mid,high)

print "Enter the total number of elements: "
n=int(raw_input(" "))

print "Enter the elements which to be sort: "
for i in range(0,n):
    a[i]=int(raw_input(" "))
         
partition(a,0,n-1);
         

j=0
count=0
b=[0,0,0,0,0,0,0,0,0,0]

for i in range(0,n):
    if a[i]!=a[i+1]:
         b[j]=a[i]
         j=j+1
         count=count+1
print" after removing duplicates are:"
for i in range(0,count):
    print b[i]
