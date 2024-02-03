from django.urls import path,include,re_path
# from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'Edit'

# router = DefaultRouter()
# router.register("question",views.QustionViewSet)

urlpatterns = [
    path('', views.index, name='QPAdd'),
    path('/qp/<id>', views.qpedit, name='QPEdit'),
    path('/qp/<id>/ques', views.qpshow, name='QPshow'),
    path('/qp/<id>/delete', views.qpdel, name='QPDel'),
    path('/<id>/ques', views.qadd, name='QAdd'),
    path('/q/<id>', views.qedit, name='QEdit'),
    path('/q/<id>/delete', views.qdel, name='Qdel'),
    path('/test2/',views.Test2QuestionView.as_view({
        'get':'list',
        'post':'create',
    })),
    path('/test2/<int:pk>/',views.Test2QuestionView.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    })),
    path('/test/<int:pk>',views.TestQuestionView.as_view(),name="test"),
    path('/question',views.QustionViewSet.as_view({
        'get':'list',
        'post':'create',
    })),
    path('/questionpapers/',views.QuestionPapersList.as_view()),
    path('/questionpapers/<int:pk>',views.QuestionPapersDetail.as_view()),
]
