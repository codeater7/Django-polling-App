"""pollster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

#  arko file bata kei leraunee ho vani mathi include pani gara raja

urlpatterns = [

# yo blank vanako chai just /polls ho vanako 
# tala ko polls vanako polls paxadi ko ho
    path('', include('pages.urls')),

    # kunai pani polls/ 6 vani tyo polls.url use gara vanako yesleee
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# polls/I_love_django
#   it will look at the file polls.urls