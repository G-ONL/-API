from rest_framework.response import Response
from rest_framework.decorators import api_view
from payment.models import Product
from rest_framework import status
from django.forms.models import model_to_dict


@api_view(['GET'])
def Product_search(request):
    if request.method == 'GET':
        url= request.data['product_url']
        product = Product.objects.get(product_url=url)
        product_dict = model_to_dict(product)
        return Response({"code": "Success", "msg": "상품이 조회되었습니다.","results":[product_dict]},status=status.HTTP_200_OK)
