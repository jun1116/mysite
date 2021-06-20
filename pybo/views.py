# from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponse
# from .models import Question, Answer, Comment
# from django.utils import timezone
# from .forms import AnswerForm, QuestionForm, CommentForm
# from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# def index(request):
#     page = request.GET.get('page','1') #page
    
#     question_list = Question.objects.order_by('-create_date')
#     paginator = Paginator(question_list, 10) # 10 question for 1 page
#     page_obj = paginator.get_page(page)
#     context = {'question_list': page_obj}

#     return render(request, 'pybo/question_list.html',context)
# '''
# render 함수는 context에 있는 Question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다. 
# 그리고 장고에서는 이런 파일(pybo/question_list.html)을 템플릿이라 부른다. 
# 템플릿은 장고의 태그를 추가로 사용할 수 있는 HTML 파일이라 생각하면 된다. 
# '''

# def detail(request, question_id):
#     '''
#     pybo 내용 출력
#     '''
#     # question = Question.objects.get(id=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question':question}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def question_create(request):
#     ## Create Question 
#     if request.method=='POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.create_date = timezone.now()
#             question.author = request.user
#             question.save()
#             return redirect('pybo:index')
#     else:
#         form=QuestionForm()
#     context = {'form':form}
#     return render(request, 'pybo/question_form.html', {'form' : form})

# @login_required(login_url="common:login")
# def question_modify(request, question_id):
#     # Modify Question
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question_id)
    
#     if request.method=="POST": #POST -> MODIFY
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modify_date = timezone.now()
#             question.save()
#             return redirect('pybo:detail', question_id=question_id)
#     else: # GET -> 수정화면으로가기
#         form=QuestionForm(instance=question)
#     context={"form":form}
#     return render(request, 'pybo/question_form.html', context)

# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     """pybo 질문삭제"""
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')

# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method=="POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.author = request.user
#             answer.save()
#             return redirect('pybo:detail', question_id = question_id)
#     else:
#         form=AnswerForm()
#     context={'question':question,'form':form}
#     return render(request, 'pybo/question_detail.html', context)
#     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#     ''' 같은 기능
#     question=get_object_or_404(Question, question_id)
#     answer=Answer(question=question, content = request.POST.get('content')), create_date=timezone.now())
#     answer.save()
#     '''
#     # return redirect('pybo:detail', question_id=question_id)

# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     ## 답변수정
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한 X')
#         return redirect('pybo:detail', question_id = answer.question.id)
    
#     if request.method == "POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)


# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     """ 
#     pybo 답변삭제
#     """ 
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('pybo:detail', question_id=answer.question.id)

# @login_required(login_url='common:login')
# def comment_create_question(request, question_id):
#     # 질문 댓글 등록
#     question=get_object_or_404(Question, pk=question_id)
#     if request.method=='POST':
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date=timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('pybo:detail', question_id = question_id)
#     else:
#         form=CommentForm()
#     context = {'form':form}
#     return render(request, 'pybo/comment_form.html', context)

# @login_required(login_url='common:login')
# def comment_modify_question(request, comment_id):
#     """
#     pybo 질문댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)

#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)

# @login_required(login_url='common:login')
# def comment_delete_question(request, comment_id):
#     """
#     pybo 질문댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.question.id)

# @login_required(login_url='common:login')
# def comment_create_answer(request,answer_id):
#     # Pybo 답글 댓글 등록
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.method=='POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment=form.save(commit=False)
#             comment.author=request.user
#             comment.create_date=timezone.now()
#             comment.answer=answer
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form=CommentForm()
#     context={'form':form}
#     return render(request, 'pybo/comment_form.html',context)

# @login_required(login_url='common:login')
# def comment_modify_answer(request, comment_id):
#     # Pybo답글댓글 수정
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없다.')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)
    
#     if request.method=='POST':
#         form = CommentForm(request.POST, instance=comment) #수정이므로, 기존의 상태를 갖고있어야함
#         if form.is_valid():
#             comment=form.save(commit=False)
#             comment.author=request.user
#             comment.modify_date=timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form=CommentForm(instance=comment)
#     context={'form':form}
#     return render(request, 'pybo/comment_form.html', context)

# @login_required(login_url='common:login')
# def comment_delete_answer(request, comment_id):
#     # pybo답글댓글 삭제
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없다.')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.answer.question.id)