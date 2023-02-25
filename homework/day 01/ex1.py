"""
Bài tập 1: vẽ hình tam giác vuông, sử dụng hàm Print
ví dụ:

*
**
***
****
*****
******

"""
maxshape = int(input('nhập kích cỡ: '))+1
for i in range(1,maxshape):
    for j in range(1,maxshape):
        if(i==1 or i==maxshape-1):
            print('* '*(maxshape-1),end='')
            break
        elif(j==1 or j==maxshape-1):
            print('* ', end='')
        else:
            print('  ', end='')
    print()