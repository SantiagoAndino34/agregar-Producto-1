from django.views import View
from .models import Product
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

# Create your views here.

class ProductView(View):


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            products=list(Product.objects.filter(id=id).values())
            if len(products )>0:
                product=products[0]
                datos = {'message': "Success", 'product': product}
            else:
                datos = {'message': "products not found..."}
            return JsonResponse(datos)
        else:
            products=list(Product.objects.values())
            if len(products )> 0:
                datos = {'message': "Success", 'products': products}
            else:
                datos = {'message': "products not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd =json.loads(request.body)
        # print(jd)
        Product.objects.create(name=jd['name'], descripccion=jd['descripccion'], precio=jd['precio'], stock=jd['stock'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd =json.loads(request.body)
        products=list(Product.objects.filter(id=id).values())
        if len(products )>0:
            product = Product.objects.get(id=id)
            product.name =jd['name']
            product.descripccion = jd['descripccion']
            product.precio =jd['precio']
            product.stock =jd['stock']
            product.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "product not found..."}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            Product.objects.filter(id=id).delete()
            datos = {'message': "Success"}

        else:
            datos = {'message': "product not found..."}
        return JsonResponse(datos)

        






