from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def index(request):

    # contatos = Contato.objects.all()
    # contatos = Contato.objects.order_by('-id').filter(
    #     mostrar=True
    # )
    # paginator = Paginator(contatos, 20)
    return render(request, 'index.html', {
        'nome': 'teste',
        # 'contatos': contatos
    })
