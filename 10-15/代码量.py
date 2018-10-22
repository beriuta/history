# # 面试真题：
# # 1. 编写函数，实现功能：将[1，2，[3，[4，5]]，6，[7，]] 转换成[1，2，3，4，5，6，7]
# #
# # 2. [1，2，[3，[4，5]]，6，[7，]]  用生成器将其生成[1，2，3，4，5，6，7]
# a = [1,2,[3,[4,5]],6,[7,]]
# b = []
# def func(x):
#     for i in x:
#         if isinstance(i, list):
#             func(i)
#         else:
#             b.append(i)
#     return b
# ret=func(a)
# print(ret)
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <script>
#         <!--// 在这里写你的代码-->
#         // 这是单行注释
#         /*这是
#         多行
#         注释*/
#         // var name = 'Beriuta';
#         // var age = 18;
#         // for (let i=0;i<arr.length;i++){...}
#         // const PI = 3.1415;
#         // PI //3.1415
#         // PI = 3
#         //TypeError: "PI" is read-only
#         // var a = 12.34;
#         // var b = 20;
#         // var c = 123e5;  // 12300000
#         // var d = 123e-5;  // 0.00123
#         // var a = true;
#         // var b = false;
#         // var a = [123,'ABC'];
#         // console.log(a[1]);  // 输出"ABC"
#         // function sortNumber(a,b){
#         //     return a - b
#         // }
#         // var arr1 = [11,200,22,55,33,44]
#         // arr1.sort(sortNumber)
#         // typeof 'abc'  //string
#         // typeof null  //object
#         // typeof true //boolean
#         // typeof 123 //number
#         // 1 == '1'  //true
#         // 1 ==='1'  //false
#         // var a = 10;
#         // if (a > 5){
#         //     console.log('yes')
#         // }else{
#         //     console.log('no')
#         // }
#         // var a = 10;
#         // if (a > 5){
#         //     console.log('a > 5');
#         // }else if (a < 5) {
#         //     console.log('a < 5');
#         // }else {
#         //     console.log('a = 5')
#         // }
#         // var day = new Date().getDay();
#         // switch (day) {
#         //     case 0:
#         //         console.log('鸡公煲');
#         //         break;
#         //     case 1:
#         //         console.log('西红柿蛋汤');
#         //         break;
#         //     case 2:
#         //         console.log('糖醋里脊')
#         //         break;
#         //     default:
#         //         console.log('不吃了')
#         // }
#         // for (var i=0;i<10;i++) {
#         //     console.log(i)
#         // }
#         // var i = 0;
#         // while (i < 10) {
#         //     console.log(i);
#         //     i++;
#         // }
#         // var a = 1;
#         // var b = 2;
#         // var c = a > b ? a:b
#         //普通定义
#         // function f1() {
#         //     console.log('hello world');
#         // }
#         //带参数的函数
#         // function f2(a,b) {
#         //     console.log(arguments);  //内置的arguments对象
#         //     console.log(arguments.length);
#         //     console.log(a,b)
#         // }
# // var age = 18;
# // function foo() {
# //     console.log(age);
# //     var age = 22;
# //     console.log(age);
# //     function age() {
# //         console.log('hehe');
# //     }
# //     console.log(age);
# // }
# // foo()
# //         //带返回值的函数
# //         function sum(a,b) {
# //             return a + b;
# //         }
# //         sum(1,2);
# //         var sum = function (a,b) {
# //             return a + b;
# //         }
# //         sum(1,2)
# //             (function (a,b) {
# //                 return a + b;
# //             })(1,2);
# //         var f = v => v;
# //         var f = function (v) {
# //             return v;
# //         }
# //         var f = () => 5;
# //         //等同于
# //         var f = function () {
# //             return 5
# //         };
# //         var sum = (num1,num2) => num1 + num2;
# //         //等同于
# //         var sum = function (num1,num2) {
# //             return num1 + num2
# //         }
# //         function add(a,b) {
# //             console.log(a+b);
# //             console.log(arguments.length)
# //         }
# //         add(1,2)
# //         var city = '北京';
# //         function f() {
# //             var city = '上海';
# //             function inner() {
# //                 var city = '深圳';
# //                 console.log(city);
# //             }
# //             inner()
# //         }
# //         f();
# //         var city = '北京';
# //         function bar() {
# //             console.log(city);
# //         }
# //         function f() {
# //             var city = '深圳';
# //             return bar;
# //         }
# //         var ret = f();
# //         ret();
# //         var city = '深圳';
# //         function f() {
# //             var city = '上海';
# //             function inner() {
# //                 console.log(city)
# //             }
# //             return inner
# //         }
# //         var ret = f();
# //         ret();
# //         var age = 18;
# //         function foo() {
# //             console.log(age);
# //             var age = 22;
# //             console.log(age);
# //         }
# //         foo();
# //         var age = 18;
# //         function foo() {
# //             console.log(age);
# //             var age = 22;
# //             console.log(age);
# //             function age() {
# //                 console.log('呵呵');
# //             }
# //             console.log(age);
# //         }
#  //       foo();
#     <!--<script src="myscript.js"></script>-->
# <!--</head>-->
# <!--<body>-->
# <!--</body>-->
# <!--</html>-->