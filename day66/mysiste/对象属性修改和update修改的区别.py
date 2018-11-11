import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiste.settings")

    import django
    django.setup()

    from applition2.models import Publisher

    # 把出版社的CEO改成元宵
    # 1. 基于对象的修改(会更新所有字段)
    p_obj = Publisher.objects.first()
    p_obj.ceo = '元宵'
    p_obj.save()
    # 把表格里面的name,city,birthday,ceo都更新了一遍，浪费内存，浪费时间

    # 2. 基于QuerySet的update更新(只更新指定的字段)
    ret = Publisher.objects.filter(id=1).update(ceo='曲妖精')
    # 只把表格里面的ceo更新了
