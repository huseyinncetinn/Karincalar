
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf.urls import handler404
urlpatterns = [
    path(_('admin/'), admin.site.urls),
]


urlpatterns += i18n_patterns ( 
    path('' , include('karincaapp.urls'))

) +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
handler404 = "karincaapp.views.page_not_found_view"