from rest_framework import serializers

from .models import ClassModel, HomeWorkModel, Question, QuizModel, Announcment, Answer, MaterialModel, LessonModel, AboutClass
import string
import random
from django.contrib.auth import get_user_model
# from accounts.models import TeacherUser, User, StudentUser
from submissions.serializers import SubmitQuizSerializer, SubmitHomeWorkSerializer
from accounts.models import User
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar')

# class TeacherUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = TeacherUser
#         fields = "__all__"

# class ClassTeacherSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = TeacherUser
#         fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class_id = serializers.CharField(read_only=True)
    class Meta:
        model = ClassModel
        fields = '__all__'
        read_only_fields = ('teacher',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['teacher'] = UserSerializer(instance.teacher, context=self.context).data
        return ret

# class ClassStudentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'role_type', 'avatar')

# class StudentUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = StudentUser
#         exclude = ['student_grade']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, *args, **kwargs):
        answers = self.validated_data.pop('answers')
        answers_serializer = AnswerSerializer(data=answers, many=True)
        answers_serializer.is_valid(raise_exception=True)
        a = answers_serializer.save()
        instance = Question.objects.create(**self.validated_data)
        instance.answers.set(a)
        return instance



class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = QuizModel
        fields = "__all__"

    def create(self, *args, **kwargs):
        questions = self.validated_data.pop('questions')
        created_questions = []
        for question in questions: 
            questions_serializer = QuestionSerializer(data=question)
            questions_serializer.is_valid(raise_exception=True)
            q = questions_serializer.save()
            created_questions.append(q)
        instance = QuizModel.objects.create(**self.validated_data)
        instance.questions.set(created_questions)
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # ret['students'] = StudentUserSerializer(instance.scratch_class.students.all(), many=True).data
        if hasattr(instance, 'submited_quizes_list'):
            ret['submited_quizes'] = SubmitQuizSerializer(instance.submited_quizes_list, many=True).data
        ret['object_type'] = 'quiz'
        return ret

class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWorkModel
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'homework'
        if hasattr(instance, 'submited_homework_list'):
            ret['submited_homeworks'] = SubmitHomeWorkSerializer(instance.submited_homework_list, many=True).data
        return ret






class AnnouncmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcment
        fields = "__all__"
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'announcment'
        return ret



class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialModel
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'material'
        return ret

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'lesson'
        return ret

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutClass
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'about class'
        return ret



class ClassWorkSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    class Meta:
        model = ClassModel
        fields = '__all__'

    def to_representation(self, instance):
        ls = []

        ret = super().to_representation(instance)
        if hasattr(instance, 'lesson_list'):
            ls.extend(LessonSerializer(instance.lesson_list, many=True).data)
            # ret['lessons'] = LessonSerializer(instance.lesson_list, many=True).data
        if hasattr(instance, 'homework_list'):
            ls.extend(HomeWorkSerializer(instance.homework_list, many=True).data)
            # ret['homeworks'] = HomeWorkSerializer(instance.homework_list, many=True).data
        if hasattr(instance, 'quiz_list'):
            ls.extend(QuizSerializer(instance.quiz_list, many=True).data)
            # ret['quizes'] = QuizSerializer(instance.quiz_list, many=True).data
        # if hasattr(instance, 'announcment_list'):
        #     ls.extend(AnnouncmentSerializer(instance.announcment_list, many=True).data)
        #     # ret['announcments'] = AnnouncmentSerializer(instance.announcment_list, many=True).data
        if hasattr(instance, 'material_list'):
            ls.extend(MaterialSerializer(instance.material_list, many=True).data)
            # ret['materials'] = MaterialSerializer(instance.material_list, many=True).data
        sorted_ls = sorted(ls, key=lambda x: x['created_at'], reverse=True)
        ret['classwork'] = sorted_ls
        return ret