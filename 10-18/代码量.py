<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="iconfont.css">
    <style>
        .cover {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background-color: rgba(0,0,0,0.3);
            z-index: 99;
        }
        .modal {
            width: 400px;
            height: 300px;
            background-color: white;
            position: absolute;
            top: 50%;
            left: 50%;
            margin-top: -150px;
            margin-left: -200px;
            z-index: 101;
        }
        .close {
            float: right;
            margin-right: 15px;
            cursor: pointer;
        }
        .hide {
            display: none;
        }
        .style2 {
            margin-left: 40px;
            margin-top: 80px;
            /*padding: 40px;*/
            /*margin: 0 auto;*/
        }
        .name {
            /*padding: 5px;*/
        }
        .cancel {
            position: absolute;
            right: 15px;
            top: 230px;
        }
         .submit {
            position: absolute;
            right: 80px;
            top: 230px;
         }
        .close {
            float: right;
            margin-right: 15px;
            cursor: pointer;
        }
        .error {
            color: salmon;
        }
    </style>
</head>
<body>
<button id="add">新增</button>
<div class="cover hide"></div>
<div class="modal hide">
    <div class="close">
        <div>x</div>
    </div>
    <div class="style2">
        <div class="name">
            <label>姓名
                <input type="text" name="username">
            </label>
            <span class="error"></span>
        </div>
        <div class="hobby">
            <label>爱好
                <input type="text" name="username">
            </label>
            <span class="error"></span>
        </div>
        <div class="submit">
            <input type="button" value="提交">
        </div>
        <div class="cancel">
            <input type="button" value="取消">
        </div>
    </div>

</div>
<table border="1">
   <thead>
    <tr>
        <th>#</th>
        <th>姓名</th>
        <th>爱好</th>
        <th>操作</th>
    </tr>
   </thead>
    <tbody>
    <tr>
        <td><input type="checkbox"></td>
        <td>金老板</td>
        <td>开车</td>
        <td><button class="fire">开除</button></td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>景女神</td>
        <td>茶道</td>
        <td><button class="fire">开除</button></td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>苑昊（苑局）</td>
        <td>不洗头、不翻车、不要脸</td>
        <td><button class="fire">开除</button></td>
    </tr>
    </tbody>
</table>
<script src="jquery.js"></script>
<script>
    // 点开模态框
    $('#add').on('click',function () {
        $('.cover,.modal').removeClass('hide')
    });
    //收起模态框
    $('.close').on('click',function () {
        $('.cover,.modal').addClass('hide')
    });
    //提交姓名和爱好的input框不能为空
    $('.submit').on('click', function () {
        var $inputEles = $('label>input');
        for (var i=0;i<$inputEles;i++);{
            var $tmp=$($inputEles[i]);  //DOM对象-->jQuery对象
            if (!$tmp.val().trim()) {
                var prefix = $tmp.parent().text().trim();
                $tmp.parent().next().text(prefix + '不能为空');
            }
        }
    });
    //给用户输入的input框绑定事件，当光标在input框时不会显示为空
    var $inputEles = $('label>input');
    for (var i =0;i<$inputEles.length;i++) {
        $inputEles[i].onfocus = function () {
            $(this).parent().next().text("")
        }
    }
    //点击取消绑定事件
    $('.cancel').on('click',function () {
        var $inputEles = $('label>input');
        for (var i=0;i<$inputEles;i++);{
            $tam = $($inputEles[i]);
            $tam.val('')
        }
    })
</script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<button id="all">全选</button>
<button id="reverse">反选</button>
<button id="cancel">取消</button>
<table border="1">
    <thead>
    <tr>
        <th>#</th>
        <th>姓名</th>
        <th>爱好</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><input type="checkbox"></td>
        <td>金老板</td>
        <td>开车</td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>景女士</td>
        <td>茶道</td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>苑耗</td>
        <td>翻车</td>
    </tr>
    </tbody>
</table>
<script src="jquery.js"></script>
<script>
    $('#all').click(function () {
        $('input:checkbox').prop('checked',true)  //prop是获取当前标签是否被选中，全部选中，统一修改布尔值
    });   //全选
    $('#cancel').click(function () {
        $('input:checkbox').prop('checked',false)  //prop是获取当前标签是否被选中，全部选中，统一修改布尔值
    }); //取消
    $('#reverse').click(function () {
        for(var i=0;i<$(':checkbox').length;i++){
            var status = $($(':checkbox')[i]).prop('checked');  //获取原来选中与否的状态
            $($(':checkbox')[i]).prop('checked',!status)  //把原来的状态修改成相反的
        }
    })
</script>
</body>
</html>
<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body {
            margin: 0;
        }
        .item {
            /*height: 50px;*/ /*不定把高度限制住*/
            width: 234px;
            background-color: teal;
            border-bottom: 1px solid white;
            cursor: pointer;
        }
        .title {
            text-align: center;
            color: white;
            padding: 15px;
        }
        .body {
            text-align: center;
            color: white;
            background-color: lightblue;
        }
        .hide {
            display: none;
        }
    </style>
</head>
<body>
<div class="menu">
    <div class="item">
        <div class="title">手机</div>
        <div class="body hide">
            <div>苹果</div>
            <div>华为</div>
            <div>三星</div>
        </div>
    </div>
    <div class="item">
        <div class="title">电脑</div>
        <div class="body hide">
            <div>苹果</div>
            <div>联想</div>
            <div>三星</div>
        </div>
    </div>
    <div class="item">
        <div class="title">服务</div>
        <div class="body hide">
            <div>在线客服</div>
            <div>机器人服务</div>
            <div>人工服务</div>
        </div>
    </div>
</div>
</body>
<script src="jquery.js"></script>
<script>
    // $('.title').on('click', function () {
    //     $('.body').addClass('hide');
    //     $(this).next().removeClass('hide')
    // )
    // }
    $('.title').on('click',function () {
        $('.body').addClass('hide');
        $(this).next().removeClass('hide')
    })
</script>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>文本操作</title>
</head>
<body>
<div class="c1">
    《前出师表》
    <p>    </p>
</div>
<input type="checkbox" name="hobby" value="basketball">篮球
<input type="checkbox" name="hobby" value="football">足球
<input type="checkbox" name="hobby" value="doublecolorball">双色球
<input type="checkbox">是否七天免登陆
<script src="jquery.js"></script>
</body>
</html>
<!--<!DOCTYPE html>-->
<!--<html lang="en">-->
<!--<head>-->
<!--<meta charset="UTF-8">-->
<!--<title>登录操作</title>-->
<!--<style>-->
<!--.error {-->
<!--color: salmon;-->
<!--}-->
<!--</style>-->
<!--</head>-->
<!--<body>-->
<!--<form action="">-->
<!--<p>-->
<!--<label>用户名-->
<!--<input type="text" name="username">-->
<!--</label>-->
<!--<span class="error"></span>-->
<!--</p>-->
<!--<p>-->
<!--<label>密码-->
<!--<input id="pwd" type="password" name="password">-->
<!--</label>-->
<!--<span class="error"></span>-->
<!--</p>-->
<!--<p>-->
<!--<button id="login" type="button">登录</button>-->
<!--</p>-->
<!--</form>-->
<!--<script src="jquery.js"></script>-->
<!--<script>-->
<!--$('#login').on('click',function () {-->
<!--var $inputAll = $('label>input');-->
<!--for (var i=0;i<$inputAll.length;i++) {-->
<!--var $tem = $($inputAll[i]);  //把DOM对象转换成jQuery对象-->
<!--if (!$tem.val().trim()) {      //trim去掉首尾的空格-->
<!--var prefix = $tem.parent().text().trim();  //其实就是label的密码跟用户名-->
<!--$tem.parent().next().text(prefix + '不能为空')-->
<!--}-->
<!--}-->
<!--});-->
<!--var $inputAll = $('label>input');-->
<!--for (var i=0;i<$inputAll.length;i++) {  //循环每一个input-->
<!--$inputAll[i].onfocus = function () {  //聚焦事件，点击input框，光标闪就收回不能为空的提示-->
<!--$(this).parent().next().text('');  //点击的input框的父标签的下一个标签的文字变成空，就是span的error-->
<!--}-->
<!--}-->
<!--</script>-->
<!--</body>-->
<!--</html>-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .error {
            color: salmon;
        }
    </style>
</head>
<body>
<form action="">
    <p>
        <label>用户名
            <input type="text" name="username">
        </label>
        <span class="error"></span>
    </p>
    <p>
        <label>密码
            <input type="password" name="pwd">
        </label>
        <span class="error"></span>
    </p>
    <button type="button" class="login">登录</button>
</form>
<script src="jquery.js"></script>
<script>
    $('.login').on('click', function () {
        var $inputAll = $('label>input');
        // for循环判断input输入框是否是空
        for (var i = 0; i < $inputAll.length;i++){
            var $input = $($inputAll[i]);  //DOM对象转换jQuery对象
            if (!$input.val().trim()) {
                var prefix = $input.parent().text().trim();
                $input.parent().next().text(prefix + '不能为空');
              }
        }
    });
  var $inputeles = $('label>input');
    for (var i=0;i<$inputeles.length;i++);{
    $inputeles[i].onfocus=function () {
        $(this).parent().next().text('');
        }
    }
</script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>位置相关返回顶部</title>
    <link rel="stylesheet" href="../10-17/iconfont.css">
    <style>
        body {
            margin:0;
        }
        .c1 {
            position: relative;
            height: 4000px;
            width: 100%;
            background-color: lightblue;
        }
        #icon {
            position: fixed;
            font-size: 100px;
            border-radius: 50%;
            right: 15px;
            bottom:15px;
            cursor: pointer;

        }
        .hide {
            display: none;
        }
    </style>
</head>
<body>
<div class="c1">
    <div class="iconfont hide" id="icon">&#xe623;</div>
</div>
<!--<button>返回顶部</button>-->
<script src="jquery.js"></script>
<script>
    $(window).scroll(function () {
        if ($(window).scrollTop() > 100) {
            $('#icon').removeClass('hide');
        }else {
            $('#icon').addClass('hide');
        }
        // console.log('dd')
    });
    $('#icon').on('click',function () {
        $(window).scrollTop(0);
    })
</script>
</body>
</html>