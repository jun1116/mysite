from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import base_views, question_views, answer_views, comment_views, vote_views
# from . import views
app_name = 'pybo'

urlpatterns = [
    # config/urls.py에서 이미 pybo/ 처리를 해준상태라, 여기선 pybo/가 아닌 ''의 빈 문자열을 인자로 넘겨준것.
    
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    #질문수정버튼
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    #질문삭제버튼
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    #답변수정URL매핑
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    #답변삭제btn
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    #질문의 Comment
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    # 답변의 Comment
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py 
    # 질문추천버튼
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    # 답변추천버튼
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),


]