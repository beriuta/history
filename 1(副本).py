#name = input('亲输入姓名：')
#age = input('请输入年龄：')
#print('此用户名是' + name +'，' + '此用户年龄是' + age)
'''choice = int(input('请输入你猜的数字：'))
if choice == 3:
	print('我请你吃饭')
elif choice == 4:
	print('我请你洗澡')
elif choice == 6:
	print('我请你打包')'''
'''s1 = 'beriuta'
s2 = 'sleep'
print(s1 + s2)'''
'''s3 = '坚持'
print(s3 * 8)'''
'''name = input('请输入姓名:')
age = input('请输入年龄:')
print(name,age)'''
'''name = input('请输入姓名:')
age = input('请输入年龄:')
print('此用户的姓名是' + name +'，' '此用户的年龄是' + age)'''
'''if 3 > 4:
	print(True)
else:
	print(False)'''
'''print(111)
if 3 > 4:
	print('这是对的')
else:
	print('这是错的')'''
'''choice = int(input('请输入你猜的数字:'))
if choice == 4:
	print('你猜中了~~')
elif choice == 3:
	print('你是我肚子的蛔虫吗？')
elif choice == 9:
elif choice == 9:
	print('你是吃了聪明果吗？')
else:
	print('笨死了')'''
'''choice = int(input('请输入你猜的大小：'))
if 0 < choice < 4:
	print('你猜的是小')
else:
	print('你猜的是大')'''
'''print("eleven" != "seven")'''
'''username = '韩蕾'
password = '123456'

user = input('请输入用户名：')
pwd = input('请输入密码：')
if user == username:
	if username == user and pwd == password:
			print("登陆成功")
	else:
		print('登陆失败')
else:
	print('登陆失败，验证错误')'''
'''username=input('请输入用户名：')
password=input('请输入密码：')
if username == 'hanlei':
	if password=='1jwe':
		print('登陆成功')
	else:
		print('密码错误')
else:
	print('用户名错误')'''
'''username = input('请输入用户名：')
password = input('请输入密码：')
if username != 'x':
	if password == '12234':
		print('登陆成功')
	else:
		print('密码错误')
else:
	print('无此用户)'''
'''username = input('请输入用户名：')
if username=='hanlei':
	password = input('请输入密码：')
	if password == '1234':
		print('登陆成功')
	else:
		print('密码错误')
else:
	print('无此用户名')'''
'''steam = input('请输入你好:')
if steam == '你好':
	print('你好，你今天要去干什么啊？')
	object = input('你是不是居居:')
	if object == '不是':
		print('你就是臭居居')
	else:
		print('不许捣乱！')
else:
	print('不听话呀！')'''
'''choice = int(input('比3小的正整数是多少：'))
if choice == 2:
	print('聪明！')
elif choice == 1:
	print('棒棒哒！')
elif choice >= 3:
	print('大了大了，太大了！')
else:
	print('小了，小了，太小了')'''
'''print('m' in 'amour')
print('l' in 'amour')
print('u' not in 'amour')'''
'''name = input('请输入麻花藤:')
if name == '麻花藤':
	print('你真聪明')
else:
	print('你是傻逼吗？')'''
'''age = int(input('请输入你的年龄：'))
if age < 10:
	print('小屁孩')
elif 10 < age < 20:
	print('青春期叛逆的小屁孩')
elif 20 < age < 30:
	print('开始定性, 开始混社会的小屁孩儿')
elif 30 < age < 40:
	print('看你老大不小了, 赶紧结婚小屁孩儿')
elif 40 < age < 50:
	print('家里有个不听话的小屁孩儿')
elif 50 < age < 60:
	print('自己马上变成不听话的老屁孩儿')
elif 60 < age < 70:
	print('提示活着还不错的老屁孩儿')
elif 70 < age < 90:
	print('人生就快结束了的一个老屁孩儿')
else:
	print('再见了这个世界')'''
'''msg = """文能提笔安天下, 
武能上马定乾坤. 
心存谋略何⼈胜, 
古今英雄唯是君.
"""
print(msg)'''
'''print(8 > 7)'''
'''s1 = '哈哈'
s2 = '哈尼'
print(s1 < s2)'''
'''n = 78
m = 45
print(n + n)
a = '一个臭皮匠'
b = '+两个臭皮匠'
c = '=三个臭皮匠'
print(a + b + c)'''
'''sam = int(input('猜猜这个数字是什么：'))
if sam == 66:
elif sam < 66:
	print('结果大了')
elif sam > 66:
	print('结果小了')
else：
	print('结果正确')'''
'''choice = int(input('请输入你猜的数字:'))
if choice == 8:
	print('你猜中了~~')
elif choice == 3:
	print('你是我肚子的蛔虫吗？')
elif choice == 9:
	print('你是吃了聪明果吗？')
else:
	print('笨死了')'''
'''print (8+9)'''
'''a= 8 + 3
print(a)'''
'''n = 'I'
m = 'L'
c = 'O'
d = 'V'
b = 'E'
f = 'y'
o = 'O'
l = 'U'
print(n+m+c+d+b+f+o+l)''' 
'''print(0 or 3)
print(4 or 3)
print(10 or 20)'''
'''count = 0
while count <= 100:#只要count<=100就不断执行下面的代码
	print('loop',count)
	if count == 5:
		break
	count += 1#每执行一次，就把count+1，不然count的值一直是0，会形成死循环
print('--------out of while loop --------')'''
count = 0
while count <= 99:
	count += 1
	if count == 5:
		continue
	print('loop',count)
print(count)









	
	

