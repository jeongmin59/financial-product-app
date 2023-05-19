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


@api_view(['GET'])
def deposit_products_detail(request, fin_prdt_cd):
    deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(deposit_product)
    data = serializer.data

    # 연결된 DepositOptions 직렬화
    options = DepositOptions.objects.filter(fin_prdt_cd=deposit_product)
    options_serializer = DepositOptionsSerializer(options, many=True)
    data['options'] = options_serializer.data

    return Response(data)

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


@api_view(['GET'])
def saving_products_detail(request, fin_prdt_cd):
    saving_product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(saving_product)
    data = serializer.data

    # 연결된 SavingOptions 직렬화
    options = SavingOptions.objects.filter(fin_prdt_cd=saving_product)
    options_serializer = SavingOptionsSerializer(options, many=True)
    data['options'] = options_serializer.data

    return Response(data)