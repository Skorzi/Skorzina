from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Goods
from .forms import BasketAddProductForm
from .basket import Basket


# class IndexView(generic.ListView):
#     template_name = "mainApp/index.html"
#     model = Goods
#     context_object_name = "last_goods"
#     basket_form = BasketAddProductForm()

# def basket_add(self, request, product_id):
#     basket = Basket(self.request)
#     if self.basket_form.is_valid():
#         cd = form.cleaned_data
#         basket.add(product=model)
#     return basket

# def get_context_data(self, **kwargs):
#     context = super(IndexView, self).get_context_data(**kwargs)
#     context['basket_goods'] = self.basket_add(self.request, self.model)
#     context['basket_product_form'] = self.basket_form
#     return context


class IndexView(generic.View):

    def get(self, request):
        goods = Goods.objects.all()
        basket = Basket(self.request)
        # if request.method == 'GET':
        #     print(request.GET)
        #     if 'get_items' in request.GET:
        #         print("HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUI")
        #         return JsonResponse(basket.returnBasket())
        return render(request, 'mainApp/index.html', context={"last_goods": goods, 'basket': basket})

    def post(self, request):
        basket = Basket(self.request)
        goods = Goods.objects.all()
        print(request.POST)
        if request.method == 'POST':
            if 'add_item' in request.POST:
                basket_add(request)
                
            elif 'remove_item_basket' in request.POST:
                basket_remove(request)

        return render(request, 'mainApp/index.html', context={"last_goods": goods, 'basket': basket})


class ShopView(generic.ListView):
    template_name = "mainApp/shop.html"
    model = Goods
    context_object_name = "last_goods"


class HelpView(generic.TemplateView):
    template_name = "mainApp/help.html"


class AboutView(generic.TemplateView):
    template_name = "mainApp/about.html"


def handler404(request, *args, **argv):
    response = render_to_response('mainApp/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def basket_add(request, product_qty=1):
    product_id = request.POST.get('id')
    basket = Basket(request)
    product = get_object_or_404(Goods, id=product_id)
    basket.add(request, product=product, qty=product_qty)
    basketqty = basket.__len__()
    print(basket.returnBasket())
    return JsonResponse(basket.returnBasket())


def basket_remove(request, product_qty=1):
    product_id = request.POST.get('id')
    product = get_object_or_404(Goods, id=product_id)
    basket = Basket(request)
    basket.remove(request, product)
    response = JsonResponse({'qty': product_qty, "OK":"true"})
    return response


# отправил пост запрос без перезагрузки в эту пизду, хочу чтобы динамически обновил также корзину
