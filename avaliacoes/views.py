from django.http import JsonResponse
from .models import Avaliacao

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values()
    return JsonResponse(list(avaliacoes), safe=False)

def listar_avaliacoes_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status='PENDENTE').values()
    return JsonResponse(list(avaliacoes), safe=False)