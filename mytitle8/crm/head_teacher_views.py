"""
班主任相关的视图都放在这里
"""
from django import views
from django.shortcuts import render, redirect, HttpResponse
from crm.models import ClassList, CourseRecord, StudyRecord
from crm.forms2 import ClassListForm, ConsultRecordForm, CourseRecordForm, StudyRecordForm
from django.http import QueryDict
from django.urls import reverse
from django.forms import modelformset_factory


class ClassListView(views.View):
    def get(self, request):
        # 拿到所有的学生
        query_set = ClassList.objects.all()
        return render(request, 'class_list.html', {'class_list': query_set})


# 新增和编辑班级
def op_class(request, edit_id=None):
    # 拿到班级对象
    edit_obj = ClassList.objects.filter(id=edit_id).first()
    # 根据班级对象到form表单里面获取到内容
    form_obj = ClassListForm(instance=edit_obj)
    if request.method == 'POST':
        form_obj = ClassListForm(request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/class_list/')
    return render(request, 'op_class.html', {'form_obj': form_obj, 'edit_id': edit_id})


# 课程记录表
class CourseListView(views.View):
    def get(self, request, class_id):
        print(class_id)
        print('*' * 120)
        # 根据班级id查询出所有的上课记录
        query_set = CourseRecord.objects.filter(re_class_id=class_id)
        current_url = request.get_full_path()
        qd = QueryDict(mutable=True)
        qd['next'] = current_url
        return render(request, 'course_list.html',
                      {'course_record_list': query_set, 'next_url': qd.urlencode(), 'class_id': class_id})

    def post(self, request, class_id):
        # 从post提交过来的数据里找action和勾选的课程记录id
        cid = request.POST.getlist('cid')
        action = request.POST.get('action')
        print(cid)
        print(action)
        # 利用反射执行指定的动作
        if hasattr(self, '_{}'.format(action)):
            ret = getattr(self, '_{}'.format(action))(cid)
        else:
            return HttpResponse('滚')
        if ret:
            return ret
        else:
            return redirect(reverse('course_record_list', kwargs={'class_id': class_id}))

    def _multi_init(self, cid):
        # 根据cid找到要初始化学习记录的 那些课程
        courser_objs = CourseRecord.objects.filter(id__in=cid)
        # 针对每个课程 挨个初始化学习记录
        # 创建学习记录,课程记录对象在上面已经找到了,找学生,然后根据课程记录找 re_class,反向查找这个班级的所有学生
        for course_record in courser_objs:  # 一个for循环拿到每一个课程,根据课程找所有的学生
            all_student = course_record.re_class.customer_set.all()  # 60个学生
            print(all_student)
            # 创建学习记录
            studentreord_objs = (StudyRecord(course_record=course_record, student=student) for student in all_student)
            StudyRecord.objects.bulk_create(studentreord_objs)  # 数据批量导入bulk_create()
            # 一个课程提交一次,一次提交60个学生的数量
        return HttpResponse('初始化好了')


def course_record(request, class_id=None, course_record_id=None):
    class_obj = ClassList.objects.filter(id=class_id).first()
    edit_obj = CourseRecord.objects.filter(id=course_record_id).first()
    form_obj = CourseRecordForm(instance=edit_obj, initial={'re_class': class_obj})
    if request.method == 'POST':
        form_obj = CourseRecordForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            next_url = request.GET.get('next', '/class_list/')
            return redirect(next_url)
    return render(request, 'course_record.html', {'form_obj': form_obj, 'edit_id': course_record_id})


# 学习记录表
def study_record_list(request, course_record_id):
    FormSet = modelformset_factory(StudyRecord, StudyRecordForm, extra=0)  # 返回值是一个类
    # 拿到这一个可课程记录的所有同学的学习记录
    query_set = StudyRecord.objects.filter(course_record_id=course_record_id)
    formset_obj = FormSet(queryset=query_set)
    if request.method == 'POST':
        formset_obj = FormSet(request.POST, queryset=query_set)
        if formset_obj.is_valid():
            formset_obj.save()
    return render(request, 'study_record_list.html', {'formset_obj': formset_obj})
    # return HttpResponse('ok')