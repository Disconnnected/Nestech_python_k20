def check(a : list) -> bool:
    print(f'check: {a}')
    if a[0] < a[1] and a[1] < a[2]:
        return True
    else:
        return False
    
def sort_3_els(a : list) -> list:
    if a[0] < a[1]:
        if a[1] < a[2]:
            a = [a[0],a[1],a[2]]
        else:
            a = [a[0],a[2],a[1]]
    else:
        a = [a[1],a[0],a[2]]
    # print( f'sorted-1: {a}' )
    if check(a) == True:
        print( f'sorted: {a}' )
        return a 
    else:
        return sort_3_els(a)
    # print( f'sorted-2: {a}' )

print(sort_3_els([6,9,3]))
# print(sort_3_els([6,9,3]))
# print(sort_3_els([9,6,3]))