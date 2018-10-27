import pymysql
pymysql.install_as_MySQLdb()  # 这里出了一个错误，把这一段话写在了APP暴力的init了，应该写在跟项目重名的那个文件的init里