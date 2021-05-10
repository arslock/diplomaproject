from .views import HomeWorkCommentViewSet, QuizCommentViewSet, MaterialCommentViewSet, LessonCommentViewSet, ClassHWComments, ClassMaterialComments, ClassLessonComments, ClassQuizComments
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hw-comment', HomeWorkCommentViewSet)
router.register(r'quiz-comment', QuizCommentViewSet)
router.register(r'material-comment', MaterialCommentViewSet)
router.register(r'lesson-comment', LessonCommentViewSet)

urlpatterns = [
path('hw-class/<int:hw_id>', ClassHWComments.as_view(), name='class-homework-comment-list'),
path('material-class/<int:material_id>', ClassMaterialComments.as_view(), name='class-material-comment-list'),
path('lesson-class/<int:lesson_id>', ClassLessonComments.as_view(), name='class-lesson-comment-list'),
path('quiz-class/<int:quiz_id>', ClassQuizComments.as_view(), name='class-quiz-comment-list'),

] + router.urls
