from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
from store.api.serializers import ProductSerializer

@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)