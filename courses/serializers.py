from rest_framework import serializers

from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} # Enable the field only in recording mode
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'created',
            'evaluation_number',
            'active'
        )


class CourseSerializer(serializers.ModelSerializer):
    # Nested Realationship
    # evaluations = EvaluationSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    '''evaluations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='evaluation-detail'
    )'''

    # Primary Key Related Field
    evaluations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active',
            'evaluations',
        )
