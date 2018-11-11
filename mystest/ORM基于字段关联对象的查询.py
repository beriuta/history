import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mystest.settings")

    import django

    django.setup()
    from applistions.models import Book, Author, Publisher, AuthorInfo

    # 查询第一本书关联的出版社名称
    book_obj = Book.objects.first()
    ret = book_obj.publisher.p_name
    print(ret)  # 西里出版社

    # 查询深圳出版社的所有的书   反向查找 ,
    publisher_obj = Publisher.objects.get(p_name='深圳出版社')
    # 如果有related_name属性，就直接后面跟.all(),没加就  表名_set
    ret = publisher_obj.books.all()
    print(ret)  # <QuerySet [<Book: Book object>, <Book: Book object>]>

    # 查询id=1的作者婚否
    author_obj = Author.objects.get(id=1)
    ret = author_obj.info.is_mary
    print(ret)  # True

    # 查询住在深圳的作者的姓名
    authorinfo_obj = AuthorInfo.objects.get(city='深圳')
    ret = authorinfo_obj.author.a_name
    print(ret)  # 小明

    # 查询id=1的作者关联的所有书籍
    author = Author.objects.get(id=1)
    ret = author.books.all()
    print(ret)  # <QuerySet [<Book: Book object>]>

    # 查询id=11的书的作者有哪一些
    book1 = Book.objects.get(id=11)
    # ret = author1.a_name
    # print(ret)  # 小明
    ret = book1.authors.all()
    print(ret)  # <QuerySet [<Author: Author object>]>
