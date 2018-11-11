import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day66.settings")
    import django
    django.setup()
    from applistions.models import Comment

    ret = Comment.objects.filter(pcommen_id=2)
    print(ret)
    for i in ret:
        print(Comment.objects.filter(pcommen_id=i))

    ret1 = Comment.objects.filter(pcommen_id=None)
    print(ret1)