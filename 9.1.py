# class Gamrole:
#     def __init__(self, nickname, ad, hd):
#         self.nickname = nickname
#         self.ad = ad
#         self.hd = hd
#     def attack(self,role):
#         role.hp = role.hp - self.ad
#         print('{}攻击了{}.{}掉了{}血,还剩{}血'.format(self.nickname, role.nickname, role.nickname, self.ad, role.hp))
#     def equip_weaon(self,w):   #给人物封装一个武器属性,这个属性值是  Weapon类的一个对象
#         self.weapon = w  #组合
# class Weapon:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#     def fight(self, name, ad):
#         self.name = name
#         self.ad = ad
#     def fight(self, role1, role2):
#         role2.hd = role2.hd - self.ad
#         print('{}用{}攻击了{},{}掉了{}血,还剩{}血'\
#               .format(role1.nickname, self.name, role2.nickname, role2.nickname, self.ad, role2.hd))
# p1 = Gamrole('盖伦',20, 500)
# p2 = Gamrole('剑豪', 100, 200)
# w1 = Weapon('大宝剑', 30)
# w2 = Weapon('武士刀', 80)
# p1.equip_weaon(w1)
# p1.weapon.fight(p1,p2)           #盖伦用大宝剑攻击了剑豪,剑豪掉了30血,还剩170血
# class Animal:
#     def __init__(self, name, kind, food, language):
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.languge = language
#     def yell(self):
#         print('{}叫'.format(self.languge))
#     def eat(self):
#         print('吃{}'.format(self.food))
#     def drink(self):
#         print('喝水')
# class Cat(Animal):
#     def catch_mouse(self):
#         print('抓老鼠')      #这个类独有的技能
# class Dog(Animal):
#     def look_after_house(self):
#         print('看家')
# cat = Cat('阿猫', '橘猫', '牛杂', '喵喵')
# print(cat.name)          #阿猫
# cat.drink()         #喝水
# cat.eat()           #吃牛杂
# cat.yell()          #喵喵叫
# dog = Dog('阿狗', '哈士奇', '阿猫', '汪汪')
# dog.drink()        #喝水
# dog.eat()          #吃阿猫
# dog.yell()         #汪汪叫
# class Animal:
#     def __init__(self, name, kind, food, language):
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.language = language
#     def yell(self):
#         print('{}叫'.format(self.language))
#     def eat(self):
#         print('吃{}'.format(self.food))
#     def drink(self):
#         print('喝水')
# class Cat(Animal):
#     def __init__(self, name, kind, food, language, eye_color):
#         print('in Cat')
#         # self.name = name
#         # self.kind = kind
#         # self.food = food
#         # self.language = language
#         # Animal.__init__( name, kind, food, language)   #子类的属性名跟父类的属性名相同,但是仍然引用父类的属性名,这时就需要这种方法
#         self.eye_color = eye_color                  #这个是猫独有的属性,所以也叫派生属性
#         super().__init__(name, kind, food, language)      #上面那种方法必须手动传入self,super直接加括号,两种方法都可以
#     def catch_mouse(self):       #派生方法
#         print('抓老鼠')
#     def eat(self):
#         # Animal.eat(self)   #不仅执行了父类食物基础功能,还完成了特殊功能
#         super().eat()
#         self.weigh = 10
# class Dog(Animal):
#     def look_after_house(self):
#         print('看家')
#     def eat(self):
#         # Animal.eat(self)
#         super().eat()
#         self.drink()
# cat = Cat('阿猫','橘猫','牛杂','喵喵','绿色')
# print(cat.eye_color)           #in Cat           绿色wd
# print(cat.food)          #牛杂
# cat.catch_mouse()                  #抓老鼠
# cat.eat()             #吃牛杂
# print(cat.weigh)          #10
# class Foo:
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')
# class Son(Foo):
#     def func(self):
#         print('in son')
# s1 = Son()    #执行子类自己的func       in son
# class Foo:
#     Country = 'China'
#     def func(self):
#         print(self.Country)
# class Son(Foo):
#     Country = 'English'
#     def func(self):
#         print(self.Country)
# s = Son()
# s.func()         #English
# class Foo:
#     Country = 'China'
#     def func(self):
#         print(self.Country)
# class Son(Foo):
#     Country = 'English'
# s = Son
# # s.func()
# s.func()
# class Foo:
#     Country = 'China'
#     def func(self):
#         print(self.Country)
# class Son(Foo):pass
# s = Son()
# s.func()        #China
# from abc import ABCMeta, abstractmethod
# class Payment(metaclass = ABCMeta):
#     @abstractmethod
#     def pay(self):pass
#
#     # @abstractmethod
#     # def shouqian(self):pass
# class Alipay(Payment):
#     def pay(self, money):
#         print('使用支付宝支付了{}元'.format(money))
# class Wechatpay(Payment):
#     def pay(self, money):
#         print('使用微信支付了{}元'.format(money))
# class ApplePay(Payment):
#     def pay(self, money):
#         print('使用applepay支付了{}元'.format(money))
# def pay(obj,money):
#     obj.pay(money)
# p = Payment()
# a = Alipay()
# a.pay(100)
# pay(a,100)
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     # def talk(self):
#     #     print('{}说话了'.format(self.name))
#     # def swim(self):
#     #     print('{}在游泳'.format(self.name))
#     # def fly(self):
#     #     print('{}在飞'.format(self.name))
#     # def walk(self):
#     #     print('{}在走路'.format(self.name))     #这样写,每一个动物都能调用这些方法,可能是老虎会飞
# class FlyAnimal(Animal):
#     def fly(self):
#         print('{}在飞'.format(self.name))
# class WalkAnimal(Animal):
#     def walk(self):
#         print('{}在走路'.format(self.name))
# class SwimAnimal(Animal):
#     def swim(self):
#         print('{}在游泳'.format(self.name))
# class Tiger(WalkAnimal,SwimAnimal,):
#     pass
# class Swan(SwimAnimal,WalkAnimal,FlyAnimal):
#     pass
# class Parrot(FlyAnimal,WalkAnimal):
#     def talk(self):
#         print('{}说话了'.format(self.name))
# swan = Swan('天鹅')
# swan.fly()         #天鹅在飞
# swan.walk()        #天鹅在走路
# Interface FlyAnimal:
#     def fly():pass
















