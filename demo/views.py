import json

from demo.models import Person
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PersonOptions(View):

    def get(self, request, *args, **kwargs):
        """
        获取用户列表
        """
        page_size = request.GET.get("pageSize")
        page_num = request.GET.get("pageNum")
        person_objs = Person.objects.all()
        paginator = Paginator(person_objs, per_page=int(page_size))
        try:
            persion_obj = paginator.page(int(page_num))
        except EmptyPage:
            persion_obj = paginator.page(int(page_num) - 1)
        total_num = person_objs.count()
        user_list = [model_to_dict(person) for person in persion_obj]
        return JsonResponse({"code": 200, "data": user_list, "total_num": total_num})

    def post(self, request, *args, **kwargs):
        """
        新增用户列表
        """
        data_json = request.body.decode('utf-8')
        name = data_json.get("name")
        sex = data_json.get("sex")
        phone = data_json.get("phone")
        email = data_json.get("email")
        address = data_json.get("address")
        state = data_json.get("state")
        Person.objects.create(name=name, sex=sex, phone=phone, email=email, address=address, state=state)
        return JsonResponse({"code": 200, "data": "success"})

    def patch(self, request, *args, **kwargs):
        """
        修改用户列表
        """
        data_json = request.body.decode('utf-8')
        id = data_json.get("id")
        name = data_json.get("name")
        sex = data_json.get("sex")
        phone = data_json.get("phone")
        email = data_json.get("email")
        address = data_json.get("address")
        state = data_json.get("state")
        person_object = Person.objects.get(id=id)
        person_object.name = name
        person_object.sex = sex
        person_object.sex = phone
        person_object.email = email
        person_object.address = address
        person_object.state = state
        person_object.save()
        return JsonResponse({"code": 200, "data": "success"})

    def delete(self, request, *args, **kwargs):
        """
        删除用户列表
        """
        pass
