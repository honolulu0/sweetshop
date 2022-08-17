import base64
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
class ProductListPageView(APIView):
    """
    View to get products by page and limitation
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
            # print(product_data)

        return JsonResponse(data={
            'data': product_data,
            'code': 1
        }, status=200, safe=False)


class ProductListView(APIView):
    """
    View to get all products
    page_limit and page_num
    http://127.0.0.1:8866/products/products/?limit=2&page=1
    http://127.0.0.1:8866/products/products/?limit=2&page=2
    """

    def get(self, request):
        name = request.GET.get('name')
        price = request.GET.get('price', 0)
        amount = request.GET.get('amount', 0)
        # filter_dict = dict(request.GET)
        filter_dict = {}
        if name:
            filter_dict['name__contains'] = name
        if price and int(price):
            filter_dict['price'] = price
        if int(amount):
            filter_dict['amount'] = amount
        print(filter_dict)
        ProductQuerySet = Product.objects.filter(**filter_dict).all().order_by('id')
        # if filter_dict:
        #     # ProductQuerySet = Product.objects.filter(name__contains=name, price=price)
        #     ProductQuerySet = Product.objects.filter(**filter_dict)
        # else:
        #     ProductQuerySet = Product.objects.all()
        product_data = []
        for ProductInstance in ProductQuerySet:
            product_dict = model_to_dict(ProductInstance)
            if 'create_time' in product_dict and product_dict['create_time']:
                product_dict['create_time'] = product_dict['create_time'].strftime(DATETIME_FORMAT)
            product_data.append(product_dict)
            # print(product_data)

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
        price = request.data.get("price", 0) if request.data.get("price", 0) else 0
        cost = request.data.get("cost", 0) if request.data.get("cost", 0) else 0
        sales_volume = request.data.get("sales_volume", 0) if request.data.get("sales_volume", 0) else 0
        amount = request.data.get("amount", 0) if request.data.get("amount", 0) else 0
        product_link = request.data.get("product_link", None)
        profit_rate = request.data.get("profit_rate", 0) if request.data.get("profit_rate", 0) else 0
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
        price = request.data.get("price", 0) if request.data.get("price", 0) else 0
        cost = request.data.get("cost", 0) if request.data.get("cost", 0) else 0
        sales_volume = request.data.get("sales_volume", 0) if request.data.get("sales_volume", 0) else 0
        amount = request.data.get("amount", 0) if request.data.get("amount", 0) else 0
        product_link = request.data.get("product_link", None)
        profit_rate = request.data.get("profit_rate", 0) if request.data.get("profit_rate", 0) else 0
        is_active = request.data.get("is_active", True)
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

        UserQuerySet = User.objects.all().order_by('id')

        user_data = []
        for UserInstance in UserQuerySet:
            user_dict = model_to_dict(UserInstance)
            if 'create_time' in user_dict and user_dict['create_time']:
                user_dict['create_time'] = user_dict['create_time'].strftime(DATETIME_FORMAT)
            user_data.append(user_dict)
            # print(user_data)

        return JsonResponse(data={
            'data': user_data,
            'code': 1
        }, status=200, safe=False)


class UserView(APIView):
    """
    View to get all products
    page_limit and page_num
    http://127.0.0.1:8866/products/products/?limit=2&page=1
    http://127.0.0.1:8866/products/products/?limit=2&page=2
    """

    def post(self, request):
        name = request.data["name"]
        password = request.data.get("password", '')
        user = User.objects.filter(name=name, password=password).first()
        if not user:
            return JsonResponse(data={
                'message': "Error,user not exist",
                'code': 0
            }, status=200, safe=False)

        return JsonResponse(data={
            'code': 1
        }, status=200, safe=False)


class NoticeView(APIView):

    def get(self, request):
        notice = Notice.objects.all()
        data = ""
        if len(notice) > 0:
            notice = list(notice)
            data = notice[0].content

        return JsonResponse(data={
            'data': data,
            'code': 1
        }, status=200, safe=False)

    def post(self, request):
        content = request.data["noticeText"]

        Notice.objects.all().delete()

        Notice.objects.create(
            content=content,
        )

        return JsonResponse(data={
            'message': "create notice succeed",
            'code': 1
        }, status=200, safe=False)


class CreateUserView(APIView):
    """
    View to add user

    """

    def post(self, request):
        name = request.data["name"]
        password = request.data.get("password", '')
        is_superuser = request.data.get("is_superuser", False)
        is_active = True
        image = request.FILES['img']
        image_string = "data:image/jpeg;base64," + str(base64.b64encode(image.read()), encoding='utf-8')
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
            is_superuser=is_superuser,
            image=image_string
        )

        return JsonResponse(data={
            'message': "add user succeed",
            'data': {"name": name
                     },
            'code': 1
        }, status=200, safe=False)


class UpdateUserView(APIView):

    def post(self, request):
        id = request.data.get("id")
        name = request.data["name"]
        password = request.data.get("password", '')
        is_superuser = request.data.get("is_superuser", False)
        is_active = True
        image = request.FILES['img']
        image_string = "data:image/jpeg;base64," + str(base64.b64encode(image.read()), encoding='utf-8')
        if not name:
            return JsonResponse(data={
                'message': "Error, Required fields not exist",
                'code': 0
            }, status=200, safe=False)

        user = User.objects.filter(id=id).first()
        if not user:
            return JsonResponse(data={
                'message': "Error,user not exist",
                'code': 0
            }, status=200, safe=False)

        user.name = name
        user.password = password
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.image = image_string
        user.save()

        return JsonResponse(data={
            'message': "update succeed",
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
