# f = open("nestech.txt", "r", encoding="utf-8")
# print(f.read())

def chiphi(giuxe, ansang, antrua):
    print()
    print()
    print()
    return (giuxe+ansang+antrua)*30

print(chiphi(5,18,30))

def tamgiac(n):
    for i in range(1,n+1):
        print('*'*i)

tamgiac(7)
