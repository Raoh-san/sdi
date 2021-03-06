#
#  Copyright (C) 2017 Atelier Cartographique <contact@atelier-cartographique.be>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import math
import json

from django.urls import reverse
from django.db import transaction
from rest_framework import serializers
from django.db import models

from ..models import (
    BaseLayer,
    Category,
    LayerGroup,
    LayerInfo,
    MessageRecord,
    MetaData,
    UserMap,
    Attachment,
)
from .message import MessageRecordSerializer
from collections import OrderedDict


class NonNullModelSerializer(serializers.Serializer):

    def to_representation(self, instance):
        result = super(
            NonNullModelSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class CategorySerializer(serializers.ModelSerializer):
    # name = MessageRecordSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name')


class AttachmentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = MessageRecordSerializer()
    url = MessageRecordSerializer()
    mapId = serializers.PrimaryKeyRelatedField(
        many=False, source='user_map',
        pk_field=serializers.UUIDField(format='hex_verbose'),
        queryset=UserMap.objects
    )

    class Meta:
        model = Attachment
        fields = ('id', 'name', 'url', 'mapId')

    def update(self, instance, validated_data):
        instance.update(validated_data)
        return instance

    def create(self, validated_data):
        name_data = validated_data.pop('name')
        url_data = validated_data.pop('url')
        user_map = validated_data.pop('user_map')
        return Attachment.objects.create_attachment(
            name_data,
            url_data,
            user_map,
        )


class BaseLayerSerializer(serializers.ModelSerializer):
    name = MessageRecordSerializer()
    url = MessageRecordSerializer()

    class Meta:
        model = BaseLayer
        fields = ('id', 'name', 'srs', 'params', 'url')

class LayerGroupSerializer(serializers.ModelSerializer):
    name = MessageRecordSerializer()

    class Meta:
        model = LayerGroup
        fields = ('id', 'name')


class LayerInfoSerializerList(serializers.ListSerializer):
    def to_representation(self, data):
        """
        List of object instances -> List of dicts of primitive datatypes.
        """
        # Dealing with nested relationships, data can be a Manager,
        # so, first get a queryset from the Manager if needed
        # print('list {} {}'.format(type(data), dir(self)))
        # iterable = data.all() if isinstance(data, models.Manager) else data
        iterable = data.order_by('user_map_layer__sort_index')

        return [
            self.child.to_representation(item) for item in iterable
        ]

class LayerInfoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    metadataId = serializers.PrimaryKeyRelatedField(
        source='metadata',
        queryset=MetaData.objects,
        pk_field=serializers.UUIDField(format='hex_verbose'),
    )
    visible = serializers.BooleanField()
    style = serializers.JSONField()
    featureViewOptions = serializers.JSONField(source='feature_view_options')
    group = LayerGroupSerializer(allow_null=True)
    legend = MessageRecordSerializer(allow_null=True)
    minZoom = serializers.IntegerField(source='min_zoom')
    maxZoom = serializers.IntegerField(source='max_zoom')

    class Meta:
        model = LayerInfo
        list_serializer_class = LayerInfoSerializerList
        fields = (
            'id', 
            'metadataId', 
            'visible', 
            'style', 
            'featureViewOptions', 
            'group', 
            'legend',
            'minZoom',
            'maxZoom',
            )
            


class UserMapSerializer(NonNullModelSerializer):
    id = serializers.UUIDField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    lastModified = serializers.SerializerMethodField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    status = serializers.ChoiceField(UserMap.STATUS_CHOICES)
    title = MessageRecordSerializer()
    description = MessageRecordSerializer()
    baseLayer = serializers.CharField(
        source='base_layer',
    )
    imageUrl = serializers.CharField(
        source='image_url',
        required=False,
        max_length=1024,
    )

    categories = serializers.PrimaryKeyRelatedField(
        required=False, many=True,
        pk_field=serializers.UUIDField(format='hex_verbose'),
        queryset=Category.objects
    )

    attachments = serializers.PrimaryKeyRelatedField(
        required=False, many=True,
        source='attachment_user_map',
        pk_field=serializers.UUIDField(format='hex_verbose'),
        queryset=Attachment.objects
    )

    # attachments = serializers.SerializerMethodField(
    #     read_only=True,
    #     source='attachment_user_map')

    layers = LayerInfoSerializer(many=True, default=[])

    def get_lastModified(self, instance):
        d = instance.last_modified
        return math.floor(d.timestamp() * 1000)

    def get_url(self, instance):
        return reverse('usermap-detail', args=[instance.id])

    # def get_attachments(self, instance):
    # return [formatAttachment(i) for i in instance.attachment_user_map.all()]

    # def get_image_url(sel, instance):
    #     url = instance.image_url
    #     print('get_image_url {}'.format(url))
    #     if url:
    #         return url
    #     return None

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        title_data = validated_data.pop('title')
        description_data = validated_data.pop('description')
        base_layer = validated_data.pop('base_layer')
        image_url = validated_data.get('image_url')
        return UserMap.objects.create_map(
            user,
            title_data,
            description_data,
            base_layer,
            image_url,
        )

    def update(self, i, validated_data):
        status = validated_data.get('status')
        title_data = validated_data.get('title')
        description_data = validated_data.get('description')
        image_url = validated_data.get('image_url')
        categories = validated_data.get('categories', [])
        layers = validated_data.get('layers', [])
        base_layer = validated_data.get('base_layer')

        with transaction.atomic():
            instance = (
                UserMap.objects
                .select_for_update()
                .get(pk=i.pk))

            instance.update_status(status)
            instance.update_title(title_data)
            instance.update_description(description_data)
            instance.update_image(image_url)
            instance.update_categories(categories)
            instance.update_layers(layers)
            instance.update_base_layer(base_layer)
            instance.save()

        return instance
