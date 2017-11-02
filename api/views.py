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
from json import loads
from django.core.serializers import serialize
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from .models import (
    Category,
    Keyword,
    LayerInfo,
    MessageRecord,
    MetaData,
    Topic,
    UserMap,
    Attachment, )
from .serializers import (
    CategorySerializer,
    KeywordSerializer,
    LayerInfoSerializer,
    MessageRecordSerializer,
    MetaDataSerializer,
    TopicSerializer,
    UserMapSerializer,
    UserSerializer,
    AttachmentSerializer, )

from .serializers.layer import get_serializer, get_model


def login_view(request):
    if request.method == "POST":
        data = loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        # next = data.get('next', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            json_data = JSONRenderer().render(UserSerializer(user).data)
            # if next:
            #     next_comps = next.split('/')
            #     next_app = next_comps[0]
            #     next_path = '/'.join(next_comps[1:])
            #     next_url = reverse('clients.root', args=(next_app, next_path))
            #     return HttpResponseRedirect(next_url)
            return HttpResponse(json_data)
        else:
            return HttpResponseBadRequest('Authentication Failed')

    return HttpResponseBadRequest('Wrong Verb')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse(JSONRenderer().render('logout'))
    return HttpResponseBadRequest('Wrong Verb')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user maps to be viewed or edited.
    """
    queryset = UserMap.objects.all().order_by('-last_modified')
    serializer_class = UserMapSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user maps to be viewed or edited.
    """
    queryset = MessageRecord.objects.all()
    serializer_class = MessageRecordSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user maps to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LayerInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user maps to be viewed or edited.
    """
    queryset = LayerInfo.objects.all()
    serializer_class = LayerInfoSerializer


class Pagination(PageNumberPagination):
    page_size = 12


class MetaDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MetaData to be viewed or edited.
    """
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer
    pagination_class = Pagination


class TopicViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class AttachmentViewSet(viewsets.ModelViewSet):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class LayerViewList(generics.ListCreateAPIView):
    def get_queryset(self):
        schema = self.kwargs.get('schema')
        table = self.kwargs.get('table')
        model = get_model(schema, table)

        return model.objects.all()

    def get_serializer_class(self):
        schema = self.kwargs.get('schema')
        table = self.kwargs.get('table')

        return get_serializer(schema, table)
