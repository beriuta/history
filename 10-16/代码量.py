# # # 编写代码实现func函数，使其实现以下效果：
# # foo = func(8)
# # print(foo(8))  # 输出64
# # print(foo(-1))  # 输出-8
# # def outer(x):
# #     def inner(y):
# #         return x * y
# #     return inner
# # foo = outer(8)
# # print(foo(-1))
#
#         <!--//把当前的时间输出成 2018-10-16 09:22 星期二-->
#         <!--// var a = {'name':'Beriuta',"age":16};-->
#         <!--// console.log(a.name);-->
#         <!--// console.log(a['age'])-->
#         <!--// var a = {'name':'sjd','age':34};-->
#         <!--// for (var i in a){-->
#         <!--//     console.log(i,a[i]);-->
#         <!--// }-->
#         <!--// var person = new Object();  // 创建一个person对象-->
#         <!--// person.name='Beriuta';  // person对象的name属性-->
#         <!--// person.age = 18;  // person对象的age属性-->
#         <!--// var m = new Map();-->
#         <!--// var o = {p:'hello world'};-->
#         <!--// m.set(o,'content');-->
#         <!--//     m.get(o)-->
#         <!--// m.has(o)-->
#         <!--// m.delete(o)-->
#         <!--// m.has(o)-->
#         <!--// // 父类构造函数-->
#         <!--// var Car = function (loc) {-->
#         <!--//     this.loc = loc;-->
#         <!--// };-->
#         <!--// // 父类方法-->
#         <!--// Car.prototype.move = function () {-->
#         <!--//     this.loc ++;-->
#         <!--// };-->
#         <!--// //子类构造函数-->
#         <!--// var Van = function (loc) {-->
#         <!--//     Car.call(this,loc);-->
#         <!--// };-->
#         <!--// // 继承父类的方法-->
#         <!--// Van.prototype = Object.create(Car.prototype);-->
#         <!--// // 修复constructor-->
#         <!--// Van.prototype.constructor = Van;-->
#         <!--// // 扩展方法-->
#         <!--// Van.prototype.grab = function() {-->
#         <!--//     /*...*/-->
#         <!--// };-->
#         <!--// // 方法1：不指定参数-->
#         <!--// var d1 = new Date();-->
#         <!--// console.log(d1.toLocaleString());-->
#         <!--// // 方法2：参数为日期字符串-->
#         <!--// var d2 = new Date('2004/3/20 11:12');-->
#         <!--// console.log(d2.toLocaleString());-->
#         <!--// var d3 = new Date('04/03/20 11:12');-->
#         <!--// console.log(d3.toLocaleString());-->
#         <!--// // 方法3：参数为毫秒数-->
#         <!--// var d3 = new Date(5000);-->
#         <!--// console.log(d3.toLocaleString());-->
#         <!--// console.log(d3.toUTCString());-->
#         <!--// // 方法4：参数为年月日小十分钟秒毫秒-->
#         <!--// var d4 = new Date(2004,2,20,11,12,0,300);-->
#         <!--// console.log(d4.toLocaleString())  //毫秒不直接显示-->
#         <!--// getDate()   获取日-->
#         <!--// getDay()    获取星期（0-6)0是星期天-->
#         <!--// getMoth()   获取月（0-11）-->
#         <!--// getFullYear()  获取完整年份-->
#         <!--// getYear()   获取年-->
#         <!--// getHours()  获取小时-->
#         <!--// getMinutes()  获取分钟-->
#         <!--// getSeconds()  获取秒-->
#         <!--// getMilliseconds()  获取毫秒-->
#         <!--// getTime()   返回累计毫秒数（从1970/1/1午夜）-->
#         <!--// var str1 = '{"name":"Beriuta","age":18}';-->
#         <!--// var obj1 = {"name":"Beriuta","age":18};-->
#         <!--// // json字符串转换成对象-->
#         <!--// var obj = JSON.parse(str1);-->
#         <!--// //对象转换成JSON字符串-->
#         <!--// var str = JSON.stringify(obj1);-->
#         <!--// var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9]{5,11}$");-->
#         <!--// // 匹配相应的字符串-->
#         <!--// var s1 = "bc123";-->
#         <!--// navigator.appName-->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# <script>
# </script>
# </head>
# <body>
# <!--<div>-->
#     <!--<div>微笑大天使</div>-->
#     <!--<div id="d1">微笑天使</div>-->
#     <!--<div>微笑小天使</div>-->
# <!--</div>-->
# <!--<p class="c1">有红</p>-->
# <!--<span>下雨</span>-->
# <!--<h1 class="c1">刷刷</h1>-->
# <!--<p>李琴</p>-->
# <input type="text" id="i1">
# <input type="button" id="start" value="开始">
# <input type="button" id="stop" value="停止">
# <div id="d1">微笑天使</div>
# <script>
#     function setTime() {
#         var i1Ele = document.getElementById('i1');
#         var now = new Date();
#         i1Ele.setAttribute('value',now.toLocaleString())
#     }
#     setTime();
#     var t;
#     var startBtn = document.getElementById('start');
#     startBtn.onclick = function () {
#         if(t === undefined) {
#             t = setInterval(setTime,1000);
#         }
#     };
#     var stopBton = document.getElementById('stop');
#     stopBton.onclick = function() {
#         clearInterval(t);
#         t = undefined
#     }
# </script>
# </body>
# </html>
