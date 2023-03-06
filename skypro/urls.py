from django.urls import path
from rest_framework.routers import DefaultRouter

from skypro.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, \
    LessonRetrieveAPIView, SubscriptionCreateAPIView, SubscriptionUpdateAPIView, PaymentAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription_update'),
    path('payment/<int:pk>/', PaymentAPIView.as_view(), name='оплата')
              ] + router.urls
