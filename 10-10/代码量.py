# # l1 = []
# # l2 = [11, 2, 3, 11, 3, 7, 2]
# # for i in l2:
# #     if i not in l1:
# #         l1.append(i)
# # print(l1)
# # list4 = [
# #     {"name": "gold", "age": 40},
# #     {"name": "eva-J", "age": 18},
# #     {"name": "nazha", "age": 19},
# #     {"name": "gaoxin", "age": 20},
# #     {"name": "yuanju", "age": 50},
# # ]
# # l2=[]
# # for dic in list4:
# #     l2.append(dic['age'])
# # l3=set(l2)
# # l3 = sorted(l3,key=l2.index)
# # print(l3)
# # ret = sorted(list4,key=lambda x: x["age"])
# # print(ret)
# # from itertools import zip_longest
# # x = [1, 2, 3, 4, 5, 6, 8, 9, 0]
# # y = [7, 3, 7, 9, 0, 3, 2, 6, 8, 0]
# # for m, n in zip_longest(x, y):
# #     print(m, n)  # 按照最长的来取值，拉链方法，没有的元素用none来代替
# # class Animal:
# #     def __init__(self,name,kind,food,language):
# #         print('in animal')
# #         self.name = name
# #         self.kind = kind
# #         self.food = food
# #         self.language = language
# #     def yell(self):
# #         print('%s叫' % self.language)
# #     def eat(self):
# #         print('吃%s' % self.food)
# #     def drink(self):
# #         print('喝水')
# # class Cat(Animal):
# #     def __init__(self,name,kind,food,language,eye_color):
# #         print('in Cat')
# #         self.eye_color = eye_color  # 派生属性
# #         super().__init__(name,kind,food,language)  # super用法，可以直接把父类的init属性继承过来
# #     def catch_mouse(self):
# #         print('抓老鼠')
# #     def eat(self):
# #         super().eat()
# #         #或者Animal.eat(self)
# #         self.weight = 10
# # class Dog(Animal):
# #     def look_after_house(self):
# #         print('看家')
# #     def eat(self):
# #         super().eat()
# #         self.drink()
# # cat1 = Cat('mao','菊毛','牛杂','miaomiao','绿色')
# # cat1.eat()  # in Cat  in animal  吃牛杂
# # print(cat1.food)  # 牛杂
# # cat1.catch_mouse()  # 抓老鼠
# # print(cat1.eye_color)  # 绿色
# # from abc import ABCMeta,abstractclassmethod
# # class Payment(metaclass=ABCMeta):  # 模板的功能
# #     @abstractclassmethod  # abstractmethod是一个装饰器，装饰器怎么用？放在函数/类的上一行
# #     def pay(self):pass
# #     # @abstractclassmethod  # 下面代码没有实现这个方法就会报错
# #     # def shouqian(self):pass
# # class Alipay(Payment):
# #     def pay(self,money):
# #         print('使用支付宝支付了%s元'%money)
# # class Wwchatpay(Payment):
# #     def pay(self,money):
# #         print('使用微信支付了%s元'%money)
# # class ApplePay(Payment):
# #     def pay(self,money):  # 必须要写pay这个方法名，不然就会报错
# #         print('使用applepay支付了%s元'%money)
# # def pay(obj,money):
# #     obj.pay(money)
# # # p = Payment()
# # a = Alipay()
# # a.pay(100)
# # print(a,100)
# # class Animal:
# #     def __init__(self,name):
# #         self.name = name
# #     def talk(self):
# #         print('%s说话了'%self.name)
# #     def swim(self):
# #         print('%s在游泳'%self.name)
# #     def fly(self):
# #         print('%s在飞'%self.name)
# #     def walk(self):
# #         print('%s在走路'%self.name)
# # class Animal:
# #     def __init__(self,name):
# #         self.name = name
# # class FlyAnimal(Animal):
# #     def fly(self):
# #         print('%s在飞'%self.name)
# # class WalkAnimal(Animal):
# #     def walk(self):
# #         print('%s在走路'%self.name)
# # class SwimAnimal(Animal):
# #     def swim(self):
# #         print('%s在游泳'%self.name)
# # class Tiger(SwimAnimal,WalkAnimal):
# #     pass
# # class Swan(SwimAnimal,WalkAnimal,FlyAnimal):
# #     pass
# # class Parrot(FlyAnimal,WalkAnimal):
# #     def talk(self):
# #         print('%s说话了'%self.name)  # 属于鹦鹉自己的方法
# # swan = Swan()
# # swan.fly()
# # swan.walk()
# # Interface FlyAnimal:  #规范继承我的类必须实现这个方法
# #     def fly():pass
# # Interface WalkAnimal:
# #     def walk():pass
# # Interface SwimAnimal:
# #     def swin():pass
# # class Tiger(WalkAnimal,SwimAnimal):  # 继承了一个规范
# #     def walk():代码
# #     def swim():代码
# # class Person1:pass
# # class Person2:pass
# # class Person3(object):pass
# # p = Person1()  # 即便是什么都没写，但是仍然会触发一个__init__初始化
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>样式</title>-->
#     <!--<style>-->
#         <!--/*id是p1的标签*/-->
#         <!--#p1 {color: mediumspringgreen}-->
#         <!--/*id是p2的标签*/-->
#         <!--#p2 {color: lightslategrey}-->
#         <!--/*所有的div标签*/-->
#         <!--div {color: indigo}-->
#         <!--/*有c1这个class标签*/-->
#         <!--.c1 {color: yellow}-->
#         <!--.c2 {color: mediumorchid}-->
#         <!--/*有c1这个class的i标签*/-->
#         <!--i.ci {color: aqua}-->
#         <!--/** {color: blanchedalmond}*/-->
#         <!--/*找儿子标签：li的儿子a标签*/-->
#         <!--li>a {color: red}-->
#         <!--/*子子孙孙找标签*/-->
#         <!--#d1 p {color: green}-->
#         <!--/*毗邻选择器：找下面紧挨着的*/-->
#         <!--div+p {color: blueviolet}-->
#         <!--/*弟弟选择器：同级往下面找*/-->
#         <!--#d2~a {color: deeppink}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<p>我是一个p标签！</p>-->
# <!--<p>我是一个p标签！</p>-->
# <!--<p id="p1">我是一个p标签！</p>-->
# <!--<p>我是一个p标签！</p>-->
# <!--<p id="p2">我是一个p标签！</p>-->
# <!--<p>我是一个p标签！</p>-->
# <!--<hr>-->
# <!--<div>我是一个块级标签！</div>-->
# <!--<div>我是一个块级标签！</div>-->
# <!--<span>我是一个内联标签</span>-->
# <!--<span>我是一个内联标签</span>-->
# <!--<span>我是一个内联标签</span>-->
# <!--<hr>-->
# <!--<i class="ci">我是一个i标签</i>-->
# <!--<li>-->
#     <!--<a href="">云</a>-->
#     <!--<a href="">云</a>-->
#     <!--<a href="">雨</a>-->
# <!--</li>-->
# <!--<div id="'d1">-->
#     <!--<p>水</p>-->
#     <!--<div>-->
#         <!--<p>闪电</p>-->
#     <!--</div>-->
#     <!--<p>火</p>-->
# <!--</div>-->
# <!--<div>我是一个div</div>-->
# <!--<p>我是div底下的一个p</p>-->
# <!--<p>我是p下面的一个p</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>行内样式</title>-->
# <!--</head>-->
# <!--<body>-->
# <!--<p style="color: red">hello world!</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>内部样式</title>-->
#     <!--<style>-->
#         <!--p {-->
#             <!--background-color: #2b99ff;-->
#         <!--}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<p>我是被内部样式改变颜色的</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>引入CSS</title>-->
#     <!--<link rel="stylesheet" href="03.css" type="text/css">-->
# <!--</head>-->
# <!--<body>-->
# <!--<p>我是被CSS外部样式改变颜色的</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>基本选择器</title>-->
#     <!--<style>-->
#         <!--p {color: red}-->
#         <!--#p1 {color: yellow}-->
#         <!--#p2 {color: orange}-->
#         <!--/*所有div标签*/-->
#         <!--div {color: brown}-->
#         <!--/*有c1这个class标签*/-->
#         <!--.c1 {color: aqua}-->
#         <!--/*有c2这个class标签*/-->
#         <!--.c2 {color: aquamarine}-->
#         <!--/*i标签里面的c1*/-->
#         <!--i.c1 {color: deepskyblue}-->
#         <!--/*通用选择器*/-->
#         <!--* {color: cornflowerblue}-->
#     <!--</style>-->
#     <!--&lt;!&ndash;<link rel="stylesheet" href="03.css">&ndash;&gt;-->
# <!--</head>-->
# <!--<body>-->
# <!--<p>我是内部样式变得颜色</p>-->
# <!--<p>我是外部样式变得颜色</p>-->
# <!--<p id="p1">我是内部样式变得色</p>-->
# <!--<p id="p2">我是外部样式变得色</p>-->
# <!--<div>我要被内部样式变成棕色了</div>-->
# <!--<p class="c1">我是被内部样式的c1改变的颜色</p>-->
# <!--<div class="c1">我是被内部样式的c1改变颜色</div>-->
# <!--<i class="c1">我是被i标签的c1改变的颜色</i>-->
# <!--<hr>-->
# <!--<div>我是div</div>-->
# <!--<div>我是div</div>-->
# <!--<div>我是div</div>-->
# <!--<hr>-->
# <!--<span>我是span</span>-->
# <!--<p class="c1 c2 c3 c4">我是一个有c1 c2 c3 c4 class的p标签</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>组合选择器</title>-->
#     <!--<style>-->
#         <!--/*li内部的a标签设置字体颜色*/-->
#         <!--li>a {color: mediumspringgreen}-->
#         <!--/*选择所有父级是<div>元素的<p>元素*/-->
#         <!--div>p {color: lightseagreen}-->
#         <!--/*子子孙孙中找标签*/-->
#         <!--#d1 p {color: tomato}  /*跟div>p的渲染一样*/-->
#         <!--/*毗邻选择器：找下面紧挨着的*/-->
#         <!--div+p {color: mediumorchid}  /*紧挨着div下面的p*/-->
#         <!--/*弟弟选择器：同级往下找*/-->
#         <!--#d2~a {color: deepskyblue}  /*d2下面的a标签都会被改变颜色*/-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<ul>-->
#     <!--<li><a href="https://www.baidu.com">手机</a></li>-->
#     <!--<li><a href="https://www.baidu.com">电脑</a></li>-->
#     <!--<li><a href="https://www.baidu.com">苹果</a></li>-->
# <!--</ul>-->
# <!--<ol>  &lt;!&ndash;有序列表&ndash;&gt;-->
#     <!--<li><p><a href="https://www.baidu.com">哈哈哈哈哈哈</a></p></li>-->
# <!--</ol>-->
# <!--<div id="d1">-->
#     <!--<div>-->
#         <!--<div>-->
#             <!--<p>我是最里面的p标签</p>-->
#         <!--</div>-->
#         <!--<p>我是跟div同级的p标签</p>-->
#     <!--</div>-->
#     <!--<p>我是儿子p标签</p>-->
# <!--</div>-->
# <!--<hr>-->
# <!--<div id="d2">腊月</div>-->
# <!--<p>div id 是d2 下面的p</p>-->
# <!--<a href="">没有链接的a标签</a>-->
# <!--<a href="">没有链接的a标签</a>-->
# <!--<a href="">没有链接的a标签</a>-->
# <!--<p>a标签下面的p标签</p>-->
# <!--<a href="">没有链接的a标签</a>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>属性选择器</title>-->
#     <!--<style>-->
#         <!--/*找到所有有hl这个属性的标签*/-->
#         <!--div[hl] {color: cornflowerblue}-->
#         <!--/*找到hl属性值是la2的标签*/-->
#         <!--div[hl='la2'] {color: mediumspringgreen}-->
#         <!--/*判断字符串是否包含给定的值 只要有hello这个字符的都算*/-->
#         <!--div[title*='hello'] {color: mediumslateblue}-->
#         <!--/*判断属性值按照空格分割得到的列表中是否包含指定的值*/-->
#         <!--div[title~='hello'] {color: aqua}-->
#         <!--/*找到所有title属性以hello开头的元素*/-->
#         <!--div[title^='hello'] {color: blueviolet}-->
#         <!--/*找到所有title属性以hello结尾的元素*/-->
#         <!--div[title$="hello"] {color: greenyellow}-->
#         <!--/*找到所有title属性中包含（字符串）包含hello的元素*/-->
#         <!--div[title*="hello"] {color: green}-->
#         <!--/*找到所有title属性（有多个值或以空格分割）中有一个值为hello的值*/-->
#         <!--div[title~="hello"] {color: cornflowerblue}-->
#         <!--/*用于选取带有title属性的元素*/-->
#         <!--div[title] {color: blue}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div hl="la">来啊来啊</div>-->
# <!--<div hl="la2">来啊来啊来啊</div>-->
# <!--<div title="behello">鹅鹅鹅，曲项向天歌，白毛浮绿水，红掌拨清波</div>-->
# <!--<div title="helloworld">helloworld</div>-->
# <!--<div title="hello world">hello world</div>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>分组嵌套</title>-->
#     <!--<style>-->
#         <!--#d1 {color: red}-->
#         <!--.c1 {color: red}-->
#         <!--/*上面代码除了属性不一样之外，样式都是一样的，可以简化*/-->
#         <!--#d1,.c1 {color: red}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div id="d1">我是div</div>-->
# <!--<p class="c1">我是p标签</p>-->
# <!--<p>我也是p标签</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html>-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>伪类选择器</title>-->
#     <!--<style>-->
#         <!--/*未访问过的链接*/-->
#         <!--a:link {color: red}-->
#         <!--/*访问过的链接*/-->
#         <!--a:visited {color: lightslategrey}-->
#         <!--/*a标签被点击的那一刻*/-->
#         <!--a:active {color: yellow}-->
#         <!--/*鼠标移动到链接上的时候渲染样式*/-->
#         <!--a:hover {color: mediumspringgreen}-->
#         <!--/*选定的链接*/-->
#         <!--a:active {color: mediumorchid}-->
#         <!--/*input输入框获取焦点时样式*/-->
#         <!--input:focus {background-color: darkgray}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<a href="http://www.4398.com">未访问过的链接</a>-->
# <!--<a href="https://www.baidu.com">访问过的链接</a>-->
# <!--<a href="http://www.sougou.com">鼠标点击的时候会变色</a>-->
# <!--<span>我是span标签</span>-->
# <!--<hr>-->
# <!--<input type="text">-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>伪元素选择器</title>-->
#     <!--<style>-->
#         <!--/*字体放大48px*/-->
#         <!--div,c1:first-letter {color: aqua;font-size: 48px}-->
#         <!--/*p标签前面加了一个*号，并且鼠标选不中*/-->
#         <!--p:before {-->
#             <!--content: "*";-->
#             <!--color: mediumspringgreen;-->
#         <!--}-->
#         <!--/*p标签后面加了一个[?]，鼠标也选不中*/-->
#         <!--p:after {-->
#             <!--content: "[?]";-->
#             <!--color: mediumslateblue;-->
#         <!--}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div class="c1">忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</div>-->
# <!--<p>忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</p>-->
# <!--<p>忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</p>-->
# <!--<p>忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</p>-->
# <!--<p>忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>选择器的优先级</title>-->
#     <!--<style>-->
#         <!--#p1 {color: cadetblue}-->
#         <!--/*这个p1把上面那个p1覆盖了*/-->
#         <!--#p1 {color: brown}-->
#     <!--</style>-->
#     <!--&lt;!&ndash;css这个样式把上面的那个覆盖了&ndash;&gt;-->
#     <!--<link rel="stylesheet" href="03.css">-->
# <!--</head>-->
# <!--<body>-->
# <!--<p id="p1"> 我是一个P标签</p>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>选择器的优先级</title>-->
#     <!--<style>-->
#         <!--/*ID选择器*/-->
#         <!--#p1 {color: darkslategrey}-->
#         <!--/*class选择器*/-->
#         <!--.c1>.c2 {color: yellow}-->
#         <!--.c2 {color: indigo}-->
#         <!--/*元素选择器*/-->
#         <!--p {color: mediumspringgreen}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div class="c1">-->
#     <!--<p class="c2" id="p1">c1内部的p标签</p>-->
# <!--</div>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="zh-CN">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>css属性的宽度和高度</title>-->
#     <!--<style>-->
#         <!--/*div {width:1000px;height:100px;background-color: antiquewhite}*/-->
#         <!--/*span {width: 1px;background-color: gray}*/-->
#         <!--body {-->
#             <!--font-family: "Bitstream Charter", "Arial",sans-serif;-->
#         <!--}-->
#         <!--span {-->
#             <!--/*字体设置为38px大*/-->
#             <!--font-size: 38px;-->
#         <!--}-->
#         <!--div {-->
#             <!--font-weight: bold;-->
#             <!--color: brown;-->
#             <!--/*颜色有三种写法：一种是英文单词，一种是16进制#00ff00,一种是rgb（251,97,19）*/-->
#             <!--/*color：rgb(251,97,19)*/-->
#             <!--/*color: #00ff00*/-->
#             <!--/*居中对齐*/-->
#             <!--text-align: center;-->
#         <!--}-->
#         <!--p {-->
#             <!--font-size: 24px;-->
#             <!--text-decoration: overline;-->
#             <!--/*前面空出88个像素*/-->
#             <!--text-indent: 88px;-->
#         <!--}-->
#         <!--/*a {*/-->
#             <!--/*!*去除超链接下面的下划线*!*/-->
#             <!--/*text-decoration: none;*/-->
#         <!--/*}*/-->
#         <!--a {-->
#             <!--/*还原超链接下面的下划线*/-->
#             <!--text-decoration: underline;-->
#         <!--}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div>div</div>-->
# <!--<span>sssssssssssssssssssssssssssssdddddddddddddddssss</span>-->
# <!--<p>忠厚老实人的恶毒像饭里的沙砾或脱骨鱼片里未净的刺，给人一种不期待的伤痛</p>-->
# <!--<a href="">超链接</a>-->
# <!--</body>-->
# <!--</html>-->