from django.template.response import TemplateResponse
from .models import ScanDrivers
from .forms import GetDrivers


def index(request):
    if request.method == 'POST':
        form = GetDrivers(request.POST)
        if form.is_valid():
            drv = ScanDrivers.objects.filter(id_driver=form.cleaned_data['id_driver'])

    else:
        form = GetDrivers()
    return TemplateResponse(request, "new.html", locals())
