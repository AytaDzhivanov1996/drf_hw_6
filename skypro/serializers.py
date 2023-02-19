from rest_framework import serializers

from skypro.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'title',
            'image',
            'description',
            'link_video'
        )


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = (
            'title',
            'image',
            'description',
            'lesson_count'
        )

    def get_lesson_count(self, instance):
        lesson_object = Lesson.objects.filter(course_title=instance)
        if lesson_object:
            return lesson_object.count()
        return 0
