from django.urls import path
# from django.urls.resolvers import URLPattern

from . import views
app_name = 'pybo'

urlpatterns = [
    # config/urls.py에서 이미 pybo/ 처리를 해준상태라, 여기선 pybo/가 아닌 ''의 빈 문자열을 인자로 넘겨준것.
    path('', views.index, name='index'),
     
    path('<int:question_id>/', views.detail, name='detail'),

    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    #질문수정버튼
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),

    #질문삭제버튼
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),

    #답변수정URL매핑
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),

    #답변삭제btn
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    #질문의 Comment
    path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:question_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:question_id>/', views.comment_delete_question, name='comment_delete_question'),

    # 답변의 Comment
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
]