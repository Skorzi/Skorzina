from .models import Goods
import copy

from decimal import Decimal
from mainApp.models import Goods
from django.conf import settings


class Basket():

    def __init__(self, request):
        self.session = request.session
        if 'basket' not in request.session:
            basket = self.session['basket'] = {}
        
        basket = self.session.get('basket')
        self.basket = basket

    def add(self, request, product, qty):
        print("we will roCK YOU")
        product_id = str(product.id)
        product_cost = float(product.cost)
        totalPrice = qty * product_cost

        if product_id not in self.basket:
            self.basket[product_id] = {'cost' : str(product_cost), 'qty':str(qty), 'totalPrice':str(totalPrice)}

        self.save()
    
    def remove(self, request, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, request, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = str(qty)
            self.basket[product_id]['totalPrice'] = self.basket[product_id]['qty'] * self.basket[product_id]['cost']
            
        self.save()

    def updateSession(self):
        self.session['basket'] = basket
        self.save()

    def get_total_price(self):
        total_price = 0
        for item in self.basket.values():
            self.total_price = Decimal(item['cost'] + self.total_price)
        return self.total_price

    def save(self):
        self.session.modified = True
    
    def returnBasket(self):
        return self.basket

    def clear(self):
        self.session.remove('basket')
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Goods.objects.filter(id__in=product_ids)
        basket = copy.deepcopy(self.basket)

        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['cost'] = float(item['cost'])
            print(item['cost'], item['qty'])
            item['totalPrice'] = item['cost'] * float(item['qty'])
            
            yield item

    def __len__(self):            
        return sum(int(item['qty']) for item in self.basket.values())
# class Basket(object):
#     def __init__(self, request):
#         self.session = request.session
#         basket = self.session.get(settings.BASKET_SESSION_ID)
        
#         if not basket:
#             basket = self.session[settings.BASKET_SESSION_ID] = {}

#         self.basket = basket

#     def __iter__(self):
#         product_ids = self.basket.keys()
#         products = Goods.objects.filter(id__in=product_ids)

#         basket = self.basket.copy()
#         for product in products:
#             basket[str(product.id)]['product'] = product

#         for item in basket.values():
#             item['cost'] = Decimal(item['cost'])
#             item['total_price'] = item['price'] * item["quantity"]
#             yield item

#     def __len__(self):
#         return sum(item['quanity'] for item in self.basket.values())

#     def add(self, Goods, quantity=1, update_quantity=False):
#         product_id = Goods.id
#         if(product_id not in self.basket):
#             self.basket[product_id] = {'quantity': 0, 'cost':str(Goods.cost)}
        
#         if update_quantity:
#             self.basket[product_id]['quantity'] = quantity
#         else:
#             self.basket[product_id]['quantity'] += quantity
#         self.save()
    
#     def save(self):
#         self.session.modified = True
    
#     def remove(self, Goods):
#         product_id = str(Goods.id)
#         if product_id in self.basket:
#             del self.basket[product_id]
#             self.save()
    
#     def get_total_price(self):
#         return sum(Decimal(item['cost'] * item['quanity'] for item in self.basket.values()))

#     def clear(self):
#         del self.session[settings.BASKET_SESSION_ID]
#         self.save()

