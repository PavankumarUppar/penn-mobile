from rest_framework import serializers

from portal.models import Poll, PollOption, PollVote


class UserPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ("id", "source", "question", "expire_date", "admin_comment")

    def create(self, validated_data):
        # adds user to the Poll
        validated_data["user"] = self.context["request"].user
        # ensuring user cannot create an admin comment upon creation
        validated_data["admin_comment"] = ""
        return super().create(validated_data)


class AdminPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = (
            "id",
            "poll",
            "choice",
        )


class RetrievePollSerializer(serializers.ModelSerializer):

    options = PollOptionSerializer(source="polloption_set", many=True)

    class Meta:
        model = Poll
        fields = ("id", "source", "created_date", "question", "expire_date", "options")


class CreateUpdatePollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = ("id", "poll_option")

    def create(self, validated_data):
        # adds poll and user to the vote
        validated_data["user"] = self.context["request"].user
        validated_data["poll"] = validated_data["poll_option"].poll
        return super().create(validated_data)


class RetrievePollVoteSerializer(serializers.ModelSerializer):

    poll = RetrievePollSerializer()
    poll_option = PollOptionSerializer()

    class Meta:
        model = PollVote
        fields = ("id", "poll", "poll_option")
