from rest_framework.serializers import ModelSerializer, SerializerMethodField

from material.models import Course, Lesson, Subscription
from material.validators import YoutubeValidation


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YoutubeValidation(field="url_video")]


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
