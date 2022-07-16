import datetime

from django.shortcuts import render
from rest_framework.views import APIView

from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from sweetapp.models import *
from django.core.paginator import Paginator
from django.views.generic import ListView

page_limit = 20
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


# Create your views here.
class ProductListView(APIView):
    """
    View to get all products
    page_limit and page_num
    http://127.0.0.1:8866/products/products/?limit=2&page=1
    http://127.0.0.1:8866/products/products/?limit=2&page=2
    """

    def get(self, request):
        limit = request.GET.get('limit', page_limit)
        page = request.GET.get('page', 1)
        ProductQuerySetLimit = Paginator(Product.objects.all().order_by('id'), limit)  # order_by('id')
        ProductQuerySet = ProductQuerySetLimit.get_page(page)

        product_data = []
        for ProductInstance in ProductQuerySet:
            product_dict = model_to_dict(ProductInstance)
            if 'create_time' in product_dict and product_dict['create_time']:
                product_dict['create_time'] = product_dict['create_time'].strftime(DATETIME_FORMAT)
            product_data.append(product_dict)
            print(product_data)

        return JsonResponse(data={
            'data': product_data,
            'code': 1
        }, status=200, safe=False)


class CreateProductView(APIView):
    """
    View to add product

    {"name": "sweet200",
    "price": 20,
    "cost": 10,
    "amount": 978,
    "product_link": "199",
    "profit_rate": 0.1,
    "is_active": 1
     }

    """

    def post(self, request):
        name = request.data.get("name")
        price = request.data.get("price", 100) if request.data.get("price", 100) else 100
        cost = request.data.get("cost", 50) if request.data.get("cost", 50) else 50
        sales_volume = request.data.get("sales_volume", 100) if request.data.get("sales_volume", 100) else 100
        amount = request.data.get("amount", 100) if request.data.get("amount", 100) else 100
        product_link = request.data.get("product_link", None)
        profit_rate = request.data.get("profit_rate", 0.1) if request.data.get("profit_rate", 0.1) else 0.1
        is_active = request.data.get("is_active", True)
        # create_time = request.data.get("create_time", datetime.datetime)
        if not name:
            return JsonResponse(data={
                'message': "Error, Required fields not exist",
                'code': 0
            }, status=200, safe=False)

        if Product.objects.filter(name=name).first():
            return JsonResponse(data={
                'message': "Error, Product exists",
                'code': 0
            }, status=200, safe=False)
        Product.objects.create(
            name=name,
            price=price,
            cost=cost,
            sales_volume=sales_volume,
            amount=amount,
            product_link=product_link,
            profit_rate=profit_rate,
            is_active=is_active,
            # create_time=create_time,
        )

        return JsonResponse(data={
            'message': "add succeed",
            'data': {"name": name,
                     "price": price,
                     "cost": cost,
                     "amount": amount,
                     "sales_volume": sales_volume,
                     "product_link": product_link,
                     "profit_rate": profit_rate,
                     "is_active": is_active,
                     },
            'code': 1
        }, status=200, safe=False)


class UpdateProductView(APIView):
    """
    View to add product

    {"id':8
    "name": "sweet200",
    "price": 20,
    "cost": 10,
    "amount": 978,
    "product_link": "199",
    "profit_rate": 0.1,
    "is_active": 1
     }

    """

    def post(self, request):
        id = request.data.get("id")
        name = request.data.get("name")
        price = request.data.get("price", 100) if request.data.get("price", 100) else 100
        cost = request.data.get("cost", 50) if request.data.get("cost", 50) else 50
        sales_volume = request.data.get("sales_volume", 100) if request.data.get("sales_volume", 100) else 100
        amount = request.data.get("amount", 100) if request.data.get("amount", 100) else 100
        product_link = request.data.get("product_link", None)
        profit_rate = request.data.get("profit_rate", 0.1) if request.data.get("profit_rate", 0.1) else 0.1
        is_active = request.data.get("is_active", True)
        # create_time = request.data.get("create_time", datetime.datetime)
        if not id:
            return JsonResponse(data={
                'message': "Error, id not exist",
                'code': 0
            }, status=200, safe=False)

        product = Product.objects.filter(id=id).first()
        if not product:
            return JsonResponse(data={
                'message': "Error,product not exist",
                'code': 0
            }, status=200, safe=False)

        if Product.objects.filter(name=name).first():
            return JsonResponse(data={
                'message': "Error, Product exists",
                'code': 0
            }, status=200, safe=False)

        product.name = name
        product.price = price
        product.cost = cost
        product.sales_volume = sales_volume
        product.amount = amount
        product.product_link = product_link
        product.profit_rate = profit_rate
        product.is_active = is_active
        product.save()

        return JsonResponse(data={
            'message': "update succeed",
            'data': {"name": name,
                     "price": price,
                     "cost": cost,
                     "amount": amount,
                     "sales_volume": sales_volume,
                     "product_link": product_link,
                     "profit_rate": profit_rate,
                     "is_active": is_active,
                     },
            'code': 1
        }, status=200, safe=False)


class DeleteProductView(APIView):
    def post(self, request):
        id = request.data.get("id")

        if not id:
            return JsonResponse(data={
                'message': "Error, ID not exist",
                'code': 0
            }, status=200, safe=False)
        product = Product.objects.filter(id=id).first()
        if not product:
            return JsonResponse(data={
                'message': "Error,product not exist",
                'code': 0
            }, status=200, safe=False)

        product.delete()

        return JsonResponse(data={
            'message': "delete product succeed",
            'data': {"name": product.name
                     },
            'code': 1
        }, status=200, safe=False)


class UserListView(APIView):
    """
    View to get all products
    page_limit and page_num
    http://127.0.0.1:8866/products/products/?limit=2&page=1
    http://127.0.0.1:8866/products/products/?limit=2&page=2
    """

    def get(self, request):
        limit = request.GET.get('limit', page_limit)
        page = request.GET.get('page', 1)
        UserQuerySetLimit = Paginator(User.objects.all().order_by('id'), limit)  # order_by('id')
        UserQuerySet = UserQuerySetLimit.get_page(page)

        user_data = []
        for UserInstance in UserQuerySet:
            user_dict = model_to_dict(UserInstance)
            if 'create_time' in user_dict and user_dict['create_time']:
                user_dict['create_time'] = user_dict['create_time'].strftime(DATETIME_FORMAT)
            user_data.append(user_dict)
            print(user_data)

        return JsonResponse(data={
            'data': user_data,
            'code': 1
        }, status=200, safe=False)


class CreateUserView(APIView):
    """
    View to add user

    """

    def post(self, request):
        name = request.data.get("name")
        password = request.data.get("password", '')
        is_superuser = request.data.get("is_superuser", False)
        is_active = True
        if not name:
            return JsonResponse(data={
                'message': "Error, Required fields not exist",
                'code': 0
            }, status=200, safe=False)

        if User.objects.filter(name=name).first():
            return JsonResponse(data={
                'message': "Error, Product exists",
                'code': 0
            }, status=200, safe=False)
        user = User.objects.create(
            name=name,
            password=password,
            is_active=is_active,
            is_superuser=is_superuser, )

        return JsonResponse(data={
            'message': "add user succeed",
            'data': {"name": name
                     },
            'code': 1
        }, status=200, safe=False)


class DeleteUserView(APIView):
    """
    View to delete user

    """

    def post(self, request):
        id = request.data.get("id")
        if not id:
            return JsonResponse(data={
                'message': "Error, ID not exist",
                'code': 0
            }, status=200, safe=False)
        user = User.objects.filter(id=id).first()
        if not user:
            return JsonResponse(data={
                'message': "Error,user not exist",
                'code': 0
            }, status=200, safe=False)

        user.delete()

        return JsonResponse(data={
            'message': "delete user succeed",
            'data': {"name": user.name
                     },
            'code': 1
        }, status=200, safe=False)
