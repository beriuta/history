<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录页面</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
    <style>
        body {
            background-color: #eeeeee;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4" style="margin-top: 70px">
            <h2 class="text-center">欢迎登陆</h2>
            <form>
                <div class="form-group">
                    <label for="exampleInputEmail1">邮箱</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
                    <span class="help-block"></span>
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">密码</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                    <span class="help-block"></span>
                </div>
                <div class="checkbox">
                    <label>
                        <input type="checkbox">记住
                    </label>
                </div>
                <button type="submit" id="login-btn" class="btn btn-success btn-block">登录</button>
            </form>
        </div>
    </div>
</div>

<script src="jquery.js"></script>
<script>
    // 给登录绑定事件
    $('#login-btn').click(function () {
        // 定义一个允许提交的标志位
        var flag = true;
        // 找到登录框所有的input框，判断是否为空
        $('form input').each(function () {  //each是遍历每一个DOM对象
            var value = $(this).val();
            if (value.length === 0){
                //为空就显示提示信息
                //提示信息出现在下框中
                var errMsg = $(this).prev().text() + '不能为空';
                $(this).next().text(errMsg);
                //给父标签设置has-error的样式
                $(this).parent().addClass('has-error');
                //阻止表单提交
                flag = false;
                return false;
            }
        });
        return flag;
    });
    //给input框绑定focus事件
    $('form input').focus(function () {  //当失去焦点时就会触发
        //取到当前input框后面的span标签的文本
        $(this).next().text('');
        //去掉父标签的额has-error样式
        $(this).parent().removeClass('has-error');
    })






</script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
    <style>
        .cover {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.3);
            z-index: 99;
        }

        .modals {
            width: 400px;
            height: 300px;
            background-color: white;
            position: absolute;
            top: 50%;
            left: 50%;
            margin-top: -150px;
            margin-left: -220px;
            z-index: 100;
        }

        .hide {
            display: none;
        }

        #input-box {
            margin: 40px;
            margin-top: 100px;
        }
        table ,#add {
            font-size: 20px;
        }
        /*#cancel,#submit {*/
        /*bottom: auto;*/
        /*}*/
    </style>
</head>
<body>
<button id="add" class="btn btn-info">新增</button>
<table class="table table-hover">
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
        <td>赵本山</td>
        <td>说相声</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>郭德纲</td>
        <td>说哲学</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>小沈阳</td>
        <td>唱歌</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>沈腾</td>
        <td>耍帅</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>谢大脚</td>
        <td>跳舞</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    <tr>
        <td><input type="checkbox"></td>
        <td>赵四</td>
        <td>舞神</td>
        <td>
            <button class="fire btn btn-danger">删除</button>
            <button class="edit btn btn-warning">编辑</button>
        </td>
    </tr>
    </tbody>
</table>

<div class="cover hide"></div>
<div class="modals hide">
    <button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>
    <div id="input-box">
        <div class="form-group">
            <label for="exampleInputName">用户名
                <input type="text" id="name">
            </label>
        </div>
        <div>
            <label>爱好
                <input type="text" id="hobby">
            </label>
        </div>
        <button id="cancel" type="button" class="btn btn-warning">重置</button>
        <button id="submit" type="button" class="btn btn-success">提交</button>
    </div>
</div>
<script src="jquery.js"></script>
<script>
    // 封装一个函数，收起模态框的同时清空input里面的内容
    function hideModal() {
        $('#name,#hobby').val('');
        $('.cover,.modals').addClass('hide')
    }

    // 封装一个函数，出现模态框的函数
    function showModal() {
        $('.cover,.modals').removeClass('hide');
    }

    // //封装一个函数，里面是用户输入input的内容
    // function textInput(){
    //     var namevalue = $('#name').val();
    //     var hobbyvalue = $('#hobby').val();
    // }
    // 1.绑定新增点击事件，出现模态框
    $('#add').click(function () {
        showModal();
    });
    // 2.点击x号，清除input内容并且收起模态框
    $('.close').click(function () {
        hideModal();
    });
    //3.点击清除，所在的行全部清除
    $('body').on('click', '.fire', function () {
        $(this).parent().parent().remove()
    });
    //4.点击重置按钮，input框内的内容全部清除
    $('#cancel').click(function () {
        $('#name,#hobby').val('')
    });
    //5.点击提交按钮，添加进入input内容，另起一行
    $('#submit').click(function () {
        var namevalue = $('#name').val();
        var hobbyvalue = $('#hobby').val();
        // 判断是编辑还是提交
        var $editTr = $(this).data('editor');
        if ($editTr === undefined) {
            // 判断input框一开始的内容是否为空，如果是空就是提交，如果不是空的就是编辑
            var trEle = document.createElement('tr');  //创建一个tr标签把内容填写进去
            $(trEle).append('<td><input type="checkbox"></td>');  //添加一个td
            $(trEle).append('<td>' + namevalue + '</td>');   //添加一个td的内容
            var tdTmp = document.createElement('td');  //在每个tdTmp后面添加td标签
            tdTmp.innerText = hobbyvalue;
            $(trEle).append(tdTmp);  //在每个trEle的后面添加一个trTMp
            $(trEle).append('<td><button class="fire">删除</button> <button class="edit">编辑</button></td>');
            //把上一步的tr追加到表格的tbody后面
            $('tbody').append(trEle);
        } else {
            // 进入编辑模式
            // 取出用户之前编辑的哪一行
            //修改对应td的文本
            $editTr.children().eq(1).text(namevalue);
            $editTr.children().eq(2).text(hobbyvalue);
            //清空submit按钮身上的data
            $('#submit').removeData('editor');
        }
        //隐藏模态框，清空输入框
        hideModal();
    });
    //点击编辑要做的事
    //绑定编辑点击事件，弹出模态框
    $('body').on('click', '.edit', function () {
        showModal();
        //获取当前行的姓名和爱好
        var $currenTr = $(this).parent().parent();  //点击按钮的父标签的父标签
        var $name = $currenTr.children().eq(1).text();
        var $hobby = $currenTr.children().eq(2).text();
        // 把上一步获取的值设置给input标签
        $('#name').val($name);
        $('#hobby').val($hobby);  //text获取的是HTML的文本内容，val是获取input用户输入的内容
        //给模态框中提交按钮绑定一个data
        $('#submit').data('editor', $currenTr);
    })


</script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
</head>
<body>
<div class="container">
    <div class="page-header">
        <h1>信息手机卡
            <small>共三步</small>
        </h1>
    </div>
    <div class="progress">
        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0"
             aria-valuemax="100" style="width: 33%">
            <p style="font-size: 15px">1/3</p>
        </div>
    </div>
    <div class="panel panel-primary">
        <div class="panel-heading">
            <h3 class="panel-title">基本信息</h3>
        </div>
        <div class="panel-body">
            <div class="container">
                <div class="col-md-5">
                    <form class="form-horizontal">
                        <div class="form-group">
                            <label for="username" class="col-sm-2 control-label">姓名</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" id="username" placeholder="username">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputNumber3" class="col-sm-2 control-label">手机</label>
                            <div class="col-sm-10">
                                <input type="number" class="form-control" id="inputNumber3" placeholder="Phone">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">邮箱</label>
                            <div class="col-sm-10">
                                <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
                            <div class="col-sm-10">
                                <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="imgInput" class="col-sm-2 control-label">头像</label>
                            <div class="col-sm-10">
                                <input type="file" id="imgInput" accept="image/png, image/jpeg, .gif">
                                <p class="help-block">只支持png、jpg格式</p>
                            </div>
                        </div>

                        <!--属性-->
                        <div class="form-group">
                            <label for="imgInput" class="col-sm-2 control-label">属性</label>
                            <div class="col-sm-10">
                                <div class="radio">
                                    <label>
                                        <input type="radio" name="optionsRadios" id="optionsRadios1" value="option1"
                                               checked>
                                        我是一个好人
                                    </label>
                                </div>
                                <div class="radio">
                                    <label>
                                        <input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
                                        我真的是一个好人
                                    </label>
                                </div>
                                <div class="radio disabled">
                                    <label>
                                        <input type="radio" name="optionsRadios" id="optionsRadios3" value="option3"
                                               disabled>
                                        我是一个坏人
                                    </label>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>

            </div>

        </div>
    </div>
    <button type="button" class="btn btn-success" style="float: right;">下一步</button>
</div>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>常用的样式</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
</head>
<body>
<div class="container">
    <h1>
        来了，就是深圳人！
        <small> 别想走</small>  <!--变灰-->
    </h1>
    <p>在苍茫的大海上，狂风卷积着乌云。在乌云和大海之间，海燕像黑色的闪电，在高傲地飞翔。</p>
    <p class="lead">在苍茫的大海上，狂风卷积着乌云。在乌云和大海之间，<strong>海燕</strong>像黑色的闪电，在高傲地
    <mark>飞翔</mark>  <!--特殊标志-->
    </p>

    <p class="text-lowercase">ce shi</p>  <!--全部小写-->
    <p class="text-uppercase">ce shi</p>  <!--全部大写-->
    <p class="text-capitalize">ces hi</p>  <!--首字母大写-->
    <hr>

    <address>
        <strong>Knight Plan</strong><br>
        深圳市 西丽站<br>
        南山区 0755 <br>
        <abbr title="Phone">Pone:</abbr>(123) 456-7800
    </address>

    <address>
        <strong>远远</strong><br>
        <a href="mailto:#">yuanyuan@jin.com</a>
    </address>
    <hr>
    <blockquote class="blockquote-reverse">
        <p>技术的提示只是量的积累，思想的提升才是质的飞跃！</p>
        <footer>Beriuta</footer>
    </blockquote>
    <hr>
    <ul class="list-unstyled">  <!--三个三行，一行一个-->
        <li>第一项</li>
        <li>第二项</li>
        <li>第三项</li>
    </ul>
    <ul class="list-inline">  <!--三个变一行-->
        <li>第一项</li>
        <li>第二项</li>
        <li>第三项</li>
    </ul>
    <hr>
    <p><code>&lt;div&gt;</code></p>  <!--插入代码-->
    <p>按住<kbd>shift</kbd>进入批量编辑模式！</p>

    <pre>
        print('hello world')
        fmt.PrintIn('hello world')
    </pre>
    <div style="height: 100px"></div>
</div>
</body>
</html>
