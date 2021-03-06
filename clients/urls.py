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

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bundle/(?P<app_name>[-_\w]+)/bundle.js.map$',
        views.app_map, name='clients.bundle.map'),

    url(r'^bundle/(?P<app_name>[-_\w]+)/(?P<path>.*)$',
        views.app, name='clients.bundle'),
    url(r'^assets/(?P<app_name>[-_\w]+)/(?P<path>.*)$',
        views.style, name='clients.assets'),
    url(r'^(?P<app_name>[-_\w]+)/(?P<path>.*)$',
        views.app_index, name='clients.root'),
    url(r'^$', views.index, name='clients.index'),
]
