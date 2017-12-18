from django.template.response import TemplateResponse
from .models import SiteDrv
from .forms import AddNews


def index(request):
    if request.method == 'POST':
        form = AddNews(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # name = request.POST  # не безопасно
    else:
        form = AddNews()
    drv = SiteDrv.objects.all()
    return TemplateResponse(request, "drv_list.html", locals())
