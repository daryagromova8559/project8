from django.urls import path
from rest_framework.routers import DefaultRouter

from material.views import (CourseViewSet, LessonListApiView, LessonCreateApiView, LessonUpdateApiView, \
                            LessonRetrieveApiView, LessonDestroyApiView, SubscriptionCreateApiView)
from material.apps import MaterialConfig

app_name = MaterialConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),
    path("lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path('subscription/create/', SubscriptionCreateApiView.as_view(), name='subscription_create'),
]
urlpatterns += router.urls
