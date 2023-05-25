from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

@api_view(['GET'])
@login_required
def profile_view(request):
    user = request.user
    deposit_fin_prdt_nm = user.fin_prdt_cd.fin_prdt_nm if user.fin_prdt_cd else '저장된 예금 상품이 없습니다'
    saving_fin_prdt_nm = user.fin_prdt_cd_saving.fin_prdt_nm if user.fin_prdt_cd_saving else '저장된 적금 상품이 없습니다'

    data = {
        'username': user.username,
        'deposit_fin_prdt_nm': deposit_fin_prdt_nm,
        'saving_fin_prdt_nm':saving_fin_prdt_nm,
    }
    return JsonResponse(data)