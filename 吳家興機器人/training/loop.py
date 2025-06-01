n=input("輸入一個正整數:")
n=int(n)
for i in range(n):
    if i*i==n:
        print("整數平方根:", i)
        break
else:
    print("沒有整數平方根")