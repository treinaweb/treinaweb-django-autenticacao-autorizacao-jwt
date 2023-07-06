from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Skill
        fields = "__all__"

    def get_links(self, obj):
        links = []
        self_link = reverse(
            "skills:detail", request=self.context["request"], kwargs={"pk": obj.pk}
        )
        links.append(
            {
                "type": "GET",
                "rel": "self",
                "href": self_link,
            }
        )
        links.append(
            {
                "type": "PUT",
                "rel": "update_skill",
                "href": self_link,
            }
        )
        links.append(
            {
                "type": "DELETE",
                "rel": "delete_skill",
                "href": self_link,
            }
        )
        return links
