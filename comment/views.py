from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from .models import Comment

# Create your views here.

def index(request):

    return render(request,'index.html')

def addData(request):
    if request.method == 'GET':
        comments = Comment.objects.all()[:10]
        list_target = []
        for comment in comments:
            data = {}
            data['username'] = comment.comment_user
            data['content'] = comment.content
            data['datatime'] = comment.datetime
            print(data)
            list_target.append(data)
        result = {'code': 200, 'message': '评论成功', 'data': list_target}
        return JsonResponse(result)
    if request.method == 'POST':
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        comment_user = json_obj.get('username')
        content = json_obj.get('content')

        if len(content)>140:
            result = {'code': 201, 'message': '评论失败，内容不能大于140'}
            return JsonResponse(result)
        try:
            Comment.objects.create(content=content,comment_user=comment_user)
        except Exception as e:
            result = {'code': 201, 'data': '评论失败'}
            return JsonResponse(result)
        result = {'code':200,'message':'评论成功'}
        return JsonResponse(result)
    return HttpResponse("请求方式有误")

def getData(request):
    if request.method == 'GET':
        try:
            size = int(request.GET.get('size'))
        except Exception as e:
            return JsonResponse({'code':202,'message':'size type error'})
        comments = Comment.objects.all()[size:size+10]
        if not comments:
            return JsonResponse({'code':201,'message':'no more data'})
        list_target = []
        for comment in comments:
            data = {}
            data['username'] = comment.comment_user
            data['content'] = comment.content
            data['datatime'] = comment.datetime
            print(data)
            list_target.append(data)
        result = {'code': 200, 'message': '评论成功', 'data': list_target}
        return JsonResponse(result)
    return HttpResponse('method is wrong')
