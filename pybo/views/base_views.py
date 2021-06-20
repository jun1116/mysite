# Index , Detail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    page = request.GET.get('page','1') #page
    
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 10 question for 1 page
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html',context)
'''
render 함수는 context에 있는 Question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다. 
그리고 장고에서는 이런 파일(pybo/question_list.html)을 템플릿이라 부른다. 
템플릿은 장고의 태그를 추가로 사용할 수 있는 HTML 파일이라 생각하면 된다. 
'''

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
