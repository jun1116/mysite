# Index , Detail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count(
            'answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page,
               'kw': kw, 'so': so}  # <------ so 추가
    return render(request, 'pybo/question_list.html', context)


# def index(request):
#     page = request.GET.get('page', '1')  # page
#     kw = request.GET.get('kw', '')  # 검색어
#     so = request.GET.get('so', 'recent')  # 정렬기준
#     question_list = Question.objects.order_by('-create_date')
#     if so == 'recommend':
#         question_list = Question.objects.annotate(
#             num_voter=Count('voter')).order_by('-num_voter', '-create_date')
#     elif so == 'popular':
#         question_list = Question.objects.annotate(num_voter=Count(
#             'answer')).order_by('-num_answer', '-create_date')
#     else:
#         question_list = Question.objects.order_by('-create_date')
#     if kw:
#         question_list = question_list.filter(
#             Q(subject__icontains=kw) |  # 제목검색
#             Q(content__icontains=kw) |  # 내용검색
#             Q(author__username__icontains=kw) |  # 저자검색
#             Q(author__author__username__icontains=kw)  # 저자검색
#         ).distinct()

#     paginator = Paginator(question_list, 10)  # 10 question for 1 page
#     page_obj = paginator.get_page(page)

#     context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}

#     return render(request, 'pybo/question_list.html', context)


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
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
