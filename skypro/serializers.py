from rest_framework import serializers

from skypro.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title',
            'image',
            'description'
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'title',
            'image',
            'description',
            'link_video'
        )
