from django.shortcuts import render,redirect
from recipebookapp.models import recipebookapp
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    context = {}
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('userhome')
        data = recipebookapp.objects.all()
        self.context['data'] = data
        return render(request,self.template_name , self.context)
