from django.urls import path
from rest_framework.routers import DefaultRouter

from skypro.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    LessonRetrieveAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('retrieve_lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('destroy_lesson/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
              ] + router.urls
