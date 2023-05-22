from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.conf import settings
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from django.core import serializers
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY = settings.API_KEY

@api_view(['GET'])
def deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    deposit_products = response['result']['baseList']
    deposit_products_options = response['result']['optionList']

    # 비교를 위해 기존 데이터 가져오기
    existing_deposit_product_cds = DepositProducts.objects.values_list('fin_prdt_cd', flat=True)
    existing_deposit_product_option_cds = DepositOptions.objects.values_list('fin_prdt_cd', flat=True)

    # 변경사항이 있는지 확인하고 최신화
    for product in deposit_products:
        fin_prdt_cd = product['fin_prdt_cd']
        if fin_prdt_cd not in existing_deposit_product_cds:
            deposit_product = DepositProducts(
                fin_prdt_cd=fin_prdt_cd,
                kor_co_nm=product['kor_co_nm'],
                fin_prdt_nm=product['fin_prdt_nm'],
                etc_note=product['etc_note'],
                join_deny=product['join_deny'],
                join_member=product['join_member'],
                join_way=product['join_way'],
                spcl_cnd=product['spcl_cnd'],
            )
            deposit_product.save()
            # 해당 상품의 옵션 정보 저장
            options = [option for option in deposit_products_options if option['fin_prdt_cd'] == fin_prdt_cd]
            for option in options:
                fin_prdt_cd = option['fin_prdt_cd']
                deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                deposit_product_option = DepositOptions(
                    fin_prdt_cd=deposit_product,
                    intr_rate_type_nm=option['intr_rate_type_nm'],
                    intr_rate=option['intr_rate'],
                    intr_rate2=option['intr_rate2'],
                    save_trm=option['save_trm'],
                )
                deposit_product_option.save()

    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposit_products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def deposit_products_detail(request, fin_prdt_cd):
    deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    
    if request.method == 'GET':
        serializer = DepositProductsSerializer(deposit_product)
        data = serializer.data

        # 연결된 DepositOptions 직렬화
        options = DepositOptions.objects.filter(fin_prdt_cd=deposit_product)
        options_serializer = DepositOptionsSerializer(options, many=True)
        data['options'] = options_serializer.data

        return Response(data)

    elif request.method == 'POST':
        user = request.user
        user.fin_prdt_cd = deposit_product
        user.save()
        # 저장 완료 후 처리할 내용 추가
        
        return Response({'message': 'Successfully saved the deposit product.'})


@api_view(['GET'])
def saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    saving_products = response['result']['baseList']
    saving_products_options = response['result']['optionList']

    # 비교를 위해 기존 데이터 가져오기
    existing_saving_product_cds = SavingProducts.objects.values_list('fin_prdt_cd', flat=True)
    existing_saving_product_option_cds = SavingOptions.objects.values_list('fin_prdt_cd', flat=True)

    # 변경사항이 있는지 확인하고 최신화
    for product in saving_products:
        fin_prdt_cd = product['fin_prdt_cd']
        if fin_prdt_cd not in existing_saving_product_cds:
            saving_product = SavingProducts(
                fin_prdt_cd=fin_prdt_cd,
                kor_co_nm=product['kor_co_nm'],
                fin_prdt_nm=product['fin_prdt_nm'],
                etc_note=product['etc_note'],
                join_deny=product['join_deny'],
                join_member=product['join_member'],
                join_way=product['join_way'],
                spcl_cnd=product['spcl_cnd'],
                mtrt_int=product['mtrt_int'],
            )
            saving_product.save()
            # 해당 상품의 옵션 정보 저장
            options = [option for option in saving_products_options if option['fin_prdt_cd'] == fin_prdt_cd]
            for option in options:
                fin_prdt_cd = option['fin_prdt_cd']
                saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                saving_product_option = SavingOptions(
                    fin_prdt_cd=saving_product,
                    intr_rate_type_nm=option['intr_rate_type_nm'],
                    rsrv_type_nm=option['rsrv_type_nm'],
                    intr_rate=option['intr_rate'],
                    intr_rate2=option['intr_rate2'],
                    save_trm=option['save_trm'],
                )
                saving_product_option.save()

    saving_products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(saving_products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def saving_products_detail(request, fin_prdt_cd):
    saving_product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)

    if request.method == 'GET':
        serializer = SavingProductsSerializer(saving_product)
        data = serializer.data

        # 연결된 SavingOptions 직렬화
        options = SavingOptions.objects.filter(fin_prdt_cd=saving_product)
        options_serializer = SavingOptionsSerializer(options, many=True)
        data['options'] = options_serializer.data

        return Response(data)

    elif request.method == 'POST':
        user = request.user
        user.fin_prdt_cd_saving = saving_product
        user.save()
        # 저장 완료 후 처리할 내용 추가

        return Response({'message': 'Successfully saved the saving product.'})


@api_view(['POST'])
def recommend_products(request):
    # 사용자 입력 정보 받기
    product_type = request.data.get('product_type')
    amount = request.data.get('amount')
    duration = request.data.get('duration')
    preferred_banks = request.data.get('preferred_banks', [])  # 은행명 리스트
    preferred_condition = request.data.get('preferred_condition')

    # 상품 모델 선택
    if product_type == '예금':
        products_model = DepositProducts
        options_model = DepositOptions
    elif product_type == '적금':
        products_model = SavingProducts
        options_model = SavingOptions

    # 추천 상품 리스트 생성
    recommendation_list = []
    products = products_model.objects.all()
    for product in products:
        options = options_model.objects.filter(fin_prdt_cd=product, save_trm__gte=duration)
        if options.exists():
            if preferred_condition:
                interest_rate = options.first().intr_rate2
            else:
                interest_rate = options.first().intr_rate
            recommendation_list.append((product, interest_rate))

    # 은행명이 일치하는 경우, 기간이 일치하는 경우를 체크하여 추천 상품 리스트를 생성합니다.
    filtered_recommendations = []
    for product, interest_rate in recommendation_list:
        if not preferred_banks or product.kor_co_nm in preferred_banks:
            if preferred_condition:
                options = options_model.objects.filter(fin_prdt_cd=product, save_trm__gte=duration, intr_rate2__gte=interest_rate)
            else:
                options = options_model.objects.filter(fin_prdt_cd=product, save_trm__gte=duration, intr_rate__gte=interest_rate)
            if options.exists():
                filtered_recommendations.append((product, interest_rate))

    # 이율을 기준으로 추천 리스트를 내림차순 정렬합니다.
    filtered_recommendations.sort(key=lambda x: x[1], reverse=True)

    # 상위 3개의 상품만 추천 리스트로 선택합니다.
    top_3_recommendations = filtered_recommendations[:3]

    # JSON 형식으로 변환하여 반환합니다.
    response_data = {'추천 상품': []}
    for product, interest_rate in top_3_recommendations:
        response_data['추천 상품'].append({
            '은행': product.kor_co_nm,
            '상품': product.fin_prdt_nm,
            '이율': interest_rate,
        })

    return JsonResponse(response_data)