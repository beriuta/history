# <!--<!DOCTYPE html>-->
# <!--<html lang="en">-->
# <!--<head>-->
# <!--<meta charset="UTF-8">-->
# <!--<title>Title</title>-->
# <!--<style>-->
# <!--.cover{-->
# <!--position:fixed;  /*固定定位*/-->
# <!--top: 0;-->
# <!--left: 0;-->
# <!--right: 0;-->
# <!--bottom: 0;-->
# <!--background-color: rgba(230,235,230,0.5);-->
# <!--z-index: 99;-->
# <!--}-->
# <!--.modal{-->
# <!--width: 400px;-->
# <!--height: 300px;-->
# <!--background-color: white;-->
# <!--position: absolute;-->
# <!--top: 50%;-->
# <!--left: 50%;-->
# <!--margin-top: -150px;-->
# <!--margin-left: -200px;-->
# <!--z-index: 100;-->
# <!--}-->
# <!--.close{-->
# <!--float:right;-->
# <!--margin-right: 15px;-->
# <!--cursor: pointer;  /*鼠标移上去光标显示小手*/-->
# <!--}-->
# <!--.hide{-->
# <!--display: none;  /*HTML文档中元素存在，但是在浏览器中不显示。收起模态框*/-->
# <!--}-->
# <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div sz="'深圳">深圳的</div>-->
# <!--<div sz="'上海">上海的</div>-->
# <!--<form action="">-->
# <!--<input type="text">-->
# <!--<input type="password">-->
# <!--<input type="checkbox" value="2">-->
# <!--<input type="email">-->
# <!--<input type="checkbox" value="1"/>-->
# <!--<input type="radio">-->
# <!--<input type="file">-->
# <!--<select id="">-->
# <!--<option value="1">1</option>-->
# <!--<option value="2">2</option>-->
# <!--</select>-->
# <!--</form>-->
# <!--<select id='s1'>-->
# <!--<<option value='beijing'>北京市</option>-->
# <!--<option value='shanghai'>上海市</option>-->
# <!--<option selected value='guangzhou'>广州市</option>-->
# <!--<option value='shenzhen'>深圳市</option>-->
# <!--</select>-->
# <!--<div>-->
# <!--<div>-->
# <!--<p>aaaa</p>-->
# <!--</div>-->
# <!--</div>-->
# <!--<div>-->
# <!--<p>aaaaa</p>-->
# <!--<span>-->
# <!--<h1>-->
# <!--ahahahh-->
# <!--</h1>-->
# <!--</span>-->
# <!--</div>-->
# <!--<input type="checkbox" value="baskeball" name="hobby">篮球-->
# <!--<input type="checkbox" value="fooball" name="hobby">足球-->
# <!--<select multiple id="s1">-->
# <!--<option value="1">1</option>-->
# <!--<option value="2">2</option>-->
# <!--<option value="3">3</option>-->
# <!--<option value="4">4</option>-->
# <!--</select>-->
# <!--<label for="c1">女</label>-->
# <!--<input name="gender" id="c1" type="radio" value="0">-->
# <!--<label for="c2">男</label>-->
# <!--<input name="gender" id="c2" type="radio" value="1">-->
# <!--<input type="text">-->
# <!--<input type="checkbox" value="1">-->
# <!--<input type="radio" value="2">-->
# <!--<input type='checkbox' id='i1' value='1'>-->
# <!--<input type="checkbox" checked id="i1" value="1" me="自定义属性">-->
# <!--<div>-->
# <!--<h1>《钗头凤》唐婉</h1>-->
# <!--<p>世情薄</p>-->
# <!--<p>人情恶</p>-->
# <!--<p>雨送黄昏花易落</p>-->
# <!--<p>晓风干</p>-->
# <!--<p>泪痕残</p>-->
# <!--<p>欲笺心事</p>-->
# <!--<p>独语斜阑</p>-->
# <!--<p>难 难 难</p>-->
# <!--<p>人成各</p>-->
# <!--<p>今非昨</p>-->
# <!--<p>病魂长似秋千索</p>-->
# <!--<p>角声寒</p>-->
# <!--<p>夜阑珊</p>-->
# <!--<p>怕人询问</p>-->
# <!--<p>咽泪装欢</p>-->
# <!--<p>瞒 瞒 瞒</p>-->
# <!--</div>-->
# <!--<button id="login">登录</button>-->
# <!--<div class="cover hide"></div>-->
# <!--<div class="modal hide">-->
# <!--<div class="close">x</div>-->
# <!--</div>-->
# <!--<script src="jquery.js"></script>-->
# <!--<script>-->
# <!--$('#login')[0].onclick = function () {-->
# <!--//去掉cover和modal的hide样式类,点击登录就弹出模态框-->
# <!--$('.cover,.modal').removeClass('hide')-->
# <!--};-->
# <!--// 绑定close事件-->
# <!--$('.close')[0].onclick =function () {-->
# <!--$('.cover,.modal').addClass('hide')-->
# <!--}-->
# <!--</script>-->
# <!--</body>-->
# <!--</html>-->
# <!--<!DOCTYPE html>-->
# <!--<html lang="en">-->
# <!--<head>-->
#     <!--<meta charset="UTF-8">-->
#     <!--<title>Title</title>-->
#     <!--<style>-->
#         <!--.menu {-->
#             <!--width: 234px;-->
#         <!--}-->
#         <!--.item {-->
#             <!--/*height: 50px;*/-->
#             <!--border-bottom: 1px solid white; /*上面加入横线*/-->
#             <!--cursor: pointer;-->
#         <!--}-->
#         <!--.title {-->
#             <!--background-color: teal;-->
#             <!--height: 50px;-->
#             <!--line-height: 50px;-->
#             <!--color: white;-->
#             <!--text-align: center;-->
#         <!--}-->
#         <!--.hide {-->
#             <!--display: none;-->
#         <!--}-->
#         <!--.body {-->
#             <!--text-align: center;-->
#             <!--color: white;-->
#             <!--background-color: lightblue;-->
#         <!--}-->
#     <!--</style>-->
# <!--</head>-->
# <!--<body>-->
# <!--<div class="menu">-->
#     <!--<div class="item">-->
#         <!--<div class="title">菜单一</div>-->
#         <!--<div class="body hide">-->
#             <!--<div>内容一</div>-->
#             <!--<div>内容二</div>-->
#             <!--<div>内容三</div>-->
#         <!--</div>-->
#     <!--</div>-->
#     <!--<div class="item">-->
#         <!--<div class="title">菜单二</div>-->
#         <!--<div class="body hide">-->
#             <!--<div>内容一</div>-->
#             <!--<div>内容二</div>-->
#             <!--<div>内容三</div>-->
#         <!--</div>-->
#     <!--</div>-->
#     <!--<div class="item">-->
#         <!--<div class="title">菜单三</div>-->
#         <!--<div class="body hide">-->
#             <!--<div>内容一</div>-->
#             <!--<div>内容二</div>-->
#             <!--<div>内容三</div>-->
#         <!--</div>-->
#     <!--</div>-->
# <!--</div>-->
# <!--<script src="jquery.js"></script>-->
# <!--<script>-->
#     <!--for (var i = 0; i < $('.title').length; i++) {-->
#         <!--$('.title')[i].onclick = function () {-->
#             <!--$('.body').addClass('hide');-->
#             <!--$(this).next().removeClass('hide');  /*这一个点击下一个菜单栏的内容就收起来*/-->
#         <!--}-->
#     <!--}-->
# <!--</script>-->
# <!--</body>-->
# <!--</html>-->
# <!DOCTYPE html>
# <html lang="CN">
# <head>
#     <meta charset="UTF-8">
#     <title>返回顶部</title>
#     <style>
#         .c1{
#             width:100px;
#             height: 200px;
#             background-color: red;
#         }
#         .c2 {
#             height: 50px;
#             width:50px;
#             position: fixed;  /*固定定位*/
#             bottom:15px;
#             right:15px;
#             color: white;
#             background-color: #2b669a;
#         }
#         .hide{
#             display: none;
#         }
#     </style>
# </head>
# </html>
# <boty>
#     <button id="'b1" class="'btn">点我</button>
#     <div class="c1">1</div>
#     <div class="c2">2</div>
#     <div class="3">3</div>
#     <div class="4">4</div>
#     <div class="5">5</div>
#     <div class="6">6</div>
#     <div class="7">7</div>
#     <div class="8">8</div>
#     <div class="9">9</div>
#     <div class="10">10</div>
#     <div class="11">11</div>
#     <div class="12">12</div>
#     <div class="13">13</div>
#     <div class="14">14</div>
#     <div class="15">15</div>
#     <div class="16">16</div>
#     <div class="17">17</div>
#     <div class="18">18</div>
#     <div class="19">19</div>
#     <div class="20">20</div>
#     <div class="21">21</div>
#     <div class="22">22</div>
#     <div class="23">23</div>
#     <div class="24">24</div>
#     <div class="25">25</div>
#     <div class="26">26</div>
#     <div class="27">27</div>
#     <div class="28">28</div>
#     <div class="29">29</div>
#     <div class="30">30</div>
#      <div class="6">6</div>
#     <div class="7">7</div>
#     <div class="8">8</div>
#     <div class="9">9</div>
#     <div class="10">10</div>
#     <div class="11">11</div>
#     <div class="12">12</div>
#     <div class="13">13</div>
#     <div class="14">14</div>
#     <div class="15">15</div>
#     <div class="16">16</div>
#     <div class="17">17</div>
#     <div class="18">18</div>
#     <div class="19">19</div>
#     <div class="20">20</div>
#     <div class="21">21</div>
#     <div class="22">22</div>
#     <div class="23">23</div>
#     <div class="24">24</div>
#     <div class="25">25</div>
#     <div class="26">26</div>
#     <div class="27">27</div>
#     <div class="28">28</div>
#     <div class="29">29</div>
#     <div class="30">30</div>
# <button id="'b2" class="btn">返回顶部</button>
#     <script src="jquery.js"></script>
# <script>
#     $('#b1').on('click',function () {
#         $('c1').offset({left:200,top:200});
#     });
# </script>
# </boty>
