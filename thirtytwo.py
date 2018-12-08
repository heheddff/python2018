n = input("请输入一个整数：")
n = eval(n)
print(pow(n,32))

str1 = input("请输入一段文字：")
i = 0
while i<len(str1):
    print(str1[i])
    i+=1

m = input("请输入一个合法运算公式：")
print(eval(m))

ft = input("请输入一个小数：")
index = ft.index(".")
print(eval(ft[0:index]))
