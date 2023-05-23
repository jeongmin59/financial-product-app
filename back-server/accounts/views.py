from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user
    data = {
        'username': user.username,
        'fin_prdt_cd': user.fin_prdt_cd,
        'fin_prdt_cd_saving': user.fin_prdt_cd_saving,
    }
    return JsonResponse(data)