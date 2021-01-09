from . import models, forms
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
class Index(generic.ListView):
    model = models.Images
    template_name = 'app/index.html'
    context_object_name = 'images'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = models.Tags.objects.all()
        return context


class ImageView(generic.DetailView):
    model = models.Images
    context_object_name = 'image'
    template_name = 'app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = models.Tags.objects.all()
        return context


class TagFormView(generic.CreateView):
    form_class = forms.TagForm
    model = models.Tags
    context_object_name = 'form'
    template_name = 'app/form.html'

    def get_success_url(self):
        return reverse('gallery:index')


class ImageFormView(generic.CreateView):
    form_class = forms.ImageForm
    model = models.Images
    context_object_name = 'form'
    template_name = 'app/form.html'

    def get_success_url(self):
        return reverse('gallery:index')


def search(request, *args, **kwargs):
    key = request.GET.get('s', '')
    data = models.Images.objects.filter(tag__tag__exact=key)
    return render(request, 'app/index.html', {'images': data, 'tags': models.Tags.objects.all()})


def tag_create_popup(request):
    form = forms.TagForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_tag");</script>' % (instance.pk, instance))
    return render(request, 'app/popup_form.html', {'form': forms.TagForm()})


def rotate(request, *args, **kwargs):
    slug = kwargs.get('slug')
    angle = kwargs.get('angle')
    model = models.Images.objects.get(slug=slug)
    model.rotate_image(angle)
    return redirect('gallery:view-image', slug)
