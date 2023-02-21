from rest_framework import viewsets, generics

from skypro.models import Course, Lesson
from skypro.permissions import OwnerOrStaff
from skypro.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [OwnerOrStaff]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerOrStaff]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerOrStaff]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
