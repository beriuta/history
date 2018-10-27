<!DOCTYPE html>
<!-- saved from url=(0042)https://v3.bootcss.com/examples/dashboard/ -->
<html lang="zh-CN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="https://v3.bootcss.com/favicon.ico">

    <title>Dashboard Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap-3.3.7/css/bootstrap.css" rel="stylesheet">


    <!-- Custom styles for this template -->
    <link href="./Dashboard Template for Bootstrap_files/dashboard.css" rel="stylesheet">

</head>

<body>

<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="https://v3.bootcss.com/examples/dashboard/#">Project name</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav navbar-left">
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Dashboard</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Settings</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Profile</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Help</a></li>
            </ul>
            <form class="navbar-form navbar-right">
            </form>
        </div>
    </div>
</nav>

<div class="container-fluid">
    <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
            <ul class="nav nav-sidebar">
                <li class="active"><a href="https://v3.bootcss.com/examples/dashboard/#">Overview <span class="sr-only">(current)</span></a>
                </li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Reports</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Analytics</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/#">Export</a></li>
            </ul>
            <ul class="nav nav-sidebar">
                <li><a href="https://v3.bootcss.com/examples/dashboard/">Nav item</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">Nav item again</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">One more nav</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">Another nav item</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">More navigation</a></li>
            </ul>
            <ul class="nav nav-sidebar">
                <li><a href="https://v3.bootcss.com/examples/dashboard/">Nav item again</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">One more nav</a></li>
                <li><a href="https://v3.bootcss.com/examples/dashboard/">Another nav item</a></li>
            </ul>
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
            <div class="table-responsive">
                <div class="panel panel-default">
                    <div class="panel-heading">Panel heading
                        <!--<button type="button" class="btn btn-success pull-right  btn-xs">添加</button>-->
                        <!--<div class="container">-->
                        <!-- 触发模态框的按钮 -->                                 <!--注意  data-toggle  data-target要对应-->
                        <button type="button" class="btn btn-success pull-right btn-sm" data-toggle="modal"
                                data-target="#myModal">
                            添加
                        </button>
                        <!-- Modal -->                                <!--注意  role要对应-->
                        <div class="modal fade" id="myModal" tabindex="-1" role="dialog"
                             aria-labelledby="myModalLabel">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal"
                                                aria-label="Close"><span
                                                aria-hidden="true">&times;</span></button>
                                        <h4 class="modal-title" id="myModalLabel">模态框</h4>
                                    </div>
                                    <div class="modal-body">
                                        <form class="form-horizontal">
                                            <div class="form-group">
                                                <label for="inputEmail3"
                                                       class="col-sm-2 control-label">Email</label>
                                                <div class="col-sm-10">
                                                    <input type="email" class="form-control" id="inputEmail3"
                                                           placeholder="Email">
                                                </div>
                                            </div>
                                            <div class="form-group">
                                                <label for="inputPassword3"
                                                       class="col-sm-2 control-label">Password</label>
                                                <div class="col-sm-10">
                                                    <input type="password" class="form-control" id="inputPassword3"
                                                           placeholder="Password">
                                                </div>
                                            </div>

                                        </form>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-default" data-dismiss="modal">关闭
                                        </button>
                                        <button type="button" class="btn btn-primary">保存</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--</div>-->
                    </div>
                    <div class="panel-body">
                    </div>
                    <div class="container">
                        <div class="row">
                            <form class="form-inline">
                                <div class="form-group">
                                    <label class="sr-only" for="exampleInputEmail3">Email address</label>
                                    <input type="email" class="form-control" id="exampleInputEmail3"
                                           placeholder="Email">
                                </div>
                                <button type="button" class="btn btn-primary">搜索</button>
                            </form>

                            <!-- Table -->
                            <div class="my-table-wrapper">
                                <table class="table table-responsive table-bordered">
                                    <thead>
                                    <tr>
                                        <th>#</th>
                                        <th>Header</th>
                                        <th>Header</th>
                                        <th>Header</th>
                                        <th>Header</th>
                                        <th>Column heading</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td>1,001</td>
                                        <td>Lorem</td>
                                        <td>ipsum</td>
                                        <td>dolor</td>
                                        <td>sit</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,002</td>
                                        <td>amet</td>
                                        <td>consectetur</td>
                                        <td>adipiscing</td>
                                        <td>elit</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,003</td>
                                        <td>Integer</td>
                                        <td>nec</td>
                                        <td>odio</td>
                                        <td>Praesent</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,003</td>
                                        <td>libero</td>
                                        <td>Sed</td>
                                        <td>cursus</td>
                                        <td>ante</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,004</td>
                                        <td>dapibus</td>
                                        <td>diam</td>
                                        <td>Sed</td>
                                        <td>nisi</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,005</td>
                                        <td>Nulla</td>
                                        <td>quis</td>
                                        <td>sem</td>
                                        <td>at</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,006</td>
                                        <td>nibh</td>
                                        <td>elementum</td>
                                        <td>imperdiet</td>
                                        <td>Duis</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,007</td>
                                        <td>sagittis</td>
                                        <td>ipsum</td>
                                        <td>Praesent</td>
                                        <td>mauris</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1,008</td>
                                        <td>Fusce</td>
                                        <td>nec</td>
                                        <td>tellus</td>
                                        <td>sed</td>
                                        <td class="text-center">
                                            <button type="button" class="btn btn-sm btn-success "><i
                                                    class="glyphicon glyphicon-pencil"></i> 编辑
                                            </button>
                                            <button type="button" class="btn btn-sm btn-danger "><i
                                                    class="glyphicon glyphicon-trash"></i> 删除
                                            </button>
                                        </td>
                                    </tr>

                                </table>
                            </div>

                        </div>
                    </div>
                    <!--分页开始-->
                    <nav aria-label="Page navigation">
                        <ul class="pagination pull-right">
                            <li>
                                <a href="#" aria-label="Previous">
                                    <span aria-hidden="true">&laquo;</span>
                                </a>
                            </li>
                            <li><a href="#">1</a></li>
                            <li><a href="#">2</a></li>
                            <li><a href="#">3</a></li>
                            <li><a href="#">4</a></li>
                            <li><a href="#">5</a></li>
                            <li>
                                <a href="#" aria-label="Next">
                                    <span aria-hidden="true">&raquo;</span>
                                </a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</div>


</tbody>
<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>


</body>
</html>
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
while True:
    conn,addr = sk.accept()
    data = conn.recv(8090)
    print(data)
    conn.send(b'ok')
    conn.close()
    < !DOCTYPE
    html >
    < html
    lang = "en" >
    < head >
    < meta
    charset = "UTF-8" >
    < title > Title < / title >
    < link
    rel = "stylesheet"
    href = "bootstrap-3.3.7/css/bootstrap.css" >
    < link
    rel = "stylesheet"
    href = "font-awesome-4.7.0/css/font-awesome.css" >
< / head >
< body >

< div


class ="container" >

< ul


class ="list-group" > < !--想要图标都大小一致，在class里面加上 fa-fw 这个属性-->

< li


class ="list-group-item" > < i class ="fa fa-heartbeat fa-fw" > < / i > Cras justo odio < / li >

< li


class ="list-group-item" > < i class ="fa fa-bath fa-fw" > < / i > Dapibus ac facilisis in < / li >

< li


class ="list-group-item" > < i class ="fa fa-bomb fa-fw" > < / i > Morbi leo risus < / li >

< li


class ="list-group-item" > < i class ="fa fa-diamond fa-fw" > < / i > Porta ac consectetur ac < / li >

< li


class ="list-group-item" > < i class ="fa fa-motorcycle fa-fw" > < / i > Vestibulum at eros < / li >

< / ul >
< / div >
< script
src = "jquery.js" > < / script >
< script
src = "bootstrap-3.3.7/js/bootstrap.js" > < / script >
< / body >
< / html >
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
    <link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.css">
</head>
<body>
<div class="container">
    <span class="glyphicon glyphicon-search"></span>
    <span class="glyphicon glyphicon-heart" style="color: chartreuse"></span>
    <!--font awesome 图标-->
    <i class="fa fa-heartbeat" style="color: #1b6d85"></i>
    <i class="fa fa-heartbeat fa-lg" style="color: #5bc0de"></i>
    <i class="fa fa-heartbeat fa-2x" style="color: #ce8483"></i>
    <i class="fa fa-heartbeat fa-3x" style="color: teal"></i>
    <i class="fa fa-heartbeat fa-4x" style="color: salmon;"></i>
    <i class="fa fa-heartbeat fa-5x" style="color: aqua"></i>
    <hr>
    <!--旋转-->
    <i class="fa fa-refresh fa-3x fa-spin"></i>
    <i class="fa fa-spinner fa-3x fa-pulse"></i>
    <h4>正在加载，请稍后...</h4>
    <hr>
    <!--禁止图标-->
    <span class="fa-stack fa-lg">
        <i class="fa fa-bell-o fa-stack-1x"></i>
        <i class="fa fa-ban fa-stack-2x text-danger"></i>
    </span>
    <hr>
    <button class="btn btn-danger "><i class="fa fa-trash-o"></i> 删除</button>
</div>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>起飞前的准备</title>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.css">
    <link rel="stylesheet" href="mystyle.css">  <!--如果有不想要的样式颜色，可以自己再写一个单独的CSS文件，放在最后面-->
</head>
<body>
<!--导航条通常不放在container中-->
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Brand</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">One more separated link</a></li>
                    </ul>
                </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                    </ul>
                </li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- 指示 -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!-- 滚屏 -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="banner1.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>爱可以辜负</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
    <div class="item">
      <img src="banner2.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>唯有美食不可辜负</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
    <div class="item">
      <img src="banner3.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>让我们一起做一个吃货吧</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
</div>
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
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
    <div class="dropdown">
        <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1"
                data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
            很长的一个按钮
            <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" aria-expanded="dropdownMenu1">
            <li><a href="#">开始</a></li>
            <li><a href="#">你开始吗</a></li>
            <li><a href="#">你他喵的快开始</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">点我！点我！</a></li>
        </ul>
    </div>
</div>
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
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
    <div>
        <!--这是标头导航按钮-->
        <ul class="nav nav-tabs nav-justified" role="tablist">
            <li role="presentation" class="active">
                <a href="#home" aria-controls="home" role="tab" data-toggle="tab">首页</a>
            </li>
            <li role="presentation">
                <a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">详情页</a>
            </li>
            <li role="presentation">
                <a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">售后服务</a>
            </li>
            <li role="presentation">
                <a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">评论</a>
            </li>
        </ul>
        <!--这是按钮相应的内容-->
        <div class="tab-content">
            <div role="tabpanel" class="tab-pane active" id="home">
                <img src="1.jpeg" alt="">
            </div>
            <div role="tabpanel" class="tab-pane " id="profile">
                <img src="2.jpeg" alt="">
            </div>
            <div role="tabpanel" class="tab-pane " id="messages">
                <img src="3.jpeg" alt="">
            </div>
            <div role="tabpanel" class="tab-pane " id="settings">
                <img src="4.jpeg" alt="">
            </div>
        </div>
    </div>
</div>
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
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
    <!-- 触发模态框的按钮 -->                                 <!--注意  data-toggle  data-target要对应-->
    <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
        点击测试
    </button>

    <!-- Modal -->                                <!--注意  role要对应-->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">模态框</h4>
                </div>
                <div class="modal-body">
                    <form class="form-horizontal">
                        <div class="form-group">
                            <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
                            <div class="col-sm-10">
                                <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
                            <div class="col-sm-10">
                                <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
                            </div>
                        </div>

                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary">保存</button>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
<script>
    $('#myModal').modal({
        backdrop: 'static',  //不放这个属性，点击模态框的背后，模态框就会消失，放上这个属性，点击模态框后面，模态框不会消失
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
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="banner1.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>爱可以辜负</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
    <div class="item">
      <img src="banner2.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>唯有美食不可辜负</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
    <div class="item">
      <img src="banner3.jpeg" alt="...">
      <div class="carousel-caption">
        <h2>让我们一起做一个吃货吧</h2>
        <p>做一个可爱的吃货</p>
      </div>
    </div>
</div>
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
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
    <div class="progress">
        <div id="p1" class="progress-bar progress-bar-info progress-bar-striped active" role="progressbar"
             aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 0%;min-width: 2%">
            0%
        </div>
    </div>
    <button class="btn btn-success btn-sm" id="b1">开始</button>
</div>

<script src="jquery.js"></script>
<script src="bootstrap-3.3.7/js/bootstrap.js"></script>
<script>
    var n = 0;
    var t;
    function foo(){
        $('#p1').css('width',n + '%').text(n + '%');
        n += 1;
        if (n > 100){
            clearInterval(t)
        }
    }
    // 点击开始，滚动条滚动，时间
    $('#b1').click(function () {
        // 没100毫秒，就执行一次下面的代码
        t = setInterval(foo,100);
    });
</script>
</body>
</html>