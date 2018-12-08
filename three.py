str1 = input("请输入一个整数：")
print(str1[:-2])

str2 = input("请输入需要分隔的内容：")
str2 = str2.split()
for i in str2:
    print(i)

weeks = ["一","二","三","四","五","六","日"]
str3 = eval(input("请输入1-7的数字："))

print("星期"+weeks[str3-1]) if 1<=str3<=7 else print("非1-7的数字")

str4 = input("请输入一个5位数：")
if str4 == str4[::-1]:
    print("{}是回文数".format(eval(str4)))
else:
    print("{0}不是回文数".format(eval(str4)))

str5 = eval(input("请输入一个十进制数："))
if type(str5) == type(1):
    print("二进制是：{}，八进制是：{}，十六进制是：{}".format(bin(str5),oct(str5),hex(str5)))
else:
    print("输入有误")
