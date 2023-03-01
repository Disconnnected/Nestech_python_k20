
"""
tuỳ chọn 1 :If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def show_list():
    list_multiples_3_5=[]
    total=0
    i=0
    while total<1000:
        if i%3==0 or i%5==0:
            total+=i
            list_multiples_3_5.append(i)
        i+=1
    print(list_multiples_3_5)
    print(sum(list_multiples_3_5))
show_list() 