"""
viết dẫy pibonaci có số cuối dưới 4000000
"""



total_Even=0
i=0
arr=[1,2]
while arr[-1]<4000000:
    arr.append(arr[i]+arr[i+1])
    i+=1
if(arr[-1]>4000000):
    arr.remove(arr[-1])
for i in arr:
    if i%2==0:
        total_Even+=i
print(arr)
print(total_Even)