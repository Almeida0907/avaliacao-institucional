from django.http import JsonResponse
from .models import Avaliacao

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values()
    return JsonResponse(list(avaliacoes), safe=False)

def listar_avaliacoes_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status='PENDENTE').values()
    return JsonResponse(list(avaliacoes), safe=False)

from django.http import JsonResponse
from django.db.models import Avg, Count, Q
from disciplinas.models import Disciplina

def resumo_disciplinas(request):
    
    resumo = Disciplina.objects.annotate(
        media_notas=Avg('avaliacao__nota'),
        total_respondidas=Count('avaliacao', filter=Q(avaliacao__status='RESPONDIDA'))
    ).values('codigo', 'nome', 'media_notas', 'total_respondidas')
    
    return JsonResponse(list(resumo), safe=False)