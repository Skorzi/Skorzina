from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Goods
from .forms import BasketAddProductForm, createUserForm, authForm
from .basket import Basket
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
import random


from .token import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


class IndexView(generic.View):

    def get(self, request):
        loginForm = authForm
        goods = Goods.objects.all()
        basket = Basket(self.request)
        return render(request, 'mainApp/index.html', context={"last_goods": goods, 'basket': basket, 'authForm': loginForm})

    def post(self, request):
        pass

class ShopView(generic.View):
    def get(self, request):
        basket = Basket(self.request)
        goods = Goods.objects.all()
        return render(request, "mainApp/shop.html", context={"basket": basket, "last_goods": goods})

    def post(self):
        pass


class HelpView(generic.View):
    def get(self, request):
        basket = Basket(self.request)
        return render(request, "mainApp/help.html", context={"basket": basket})

    def post(self):
        pass


class AboutView(generic.View):
    def get(self, request):
        basket = Basket(self.request)
        return render(request, "mainApp/about.html", context={"basket": basket})

    def post(self):
        pass


class ProductView(generic.View):
    def get(self, request, pk=None):
        good = Goods.objects.get(id=pk)
        basket = Basket(self.request)
        return render(request, "mainApp/product.html", context={"good": good, "basket": basket})

    def post(self):
        pass


def generate_code(request, userForm):
    random.seed()
    code = str(random.randint(10000, 99999))
    request.session['code'] = code
    to_email = userForm.cleaned_data.get('email')
    username = userForm.cleaned_data['username']
    emailSubj = 'Confirm Registration'
    message = render_to_string('mainApp/activateMail.html', context={
        'user': username,
        'code': code,
    })
    email = EmailMessage(emailSubj, message, to=[to_email])
    email.send()
    return code


class RegisterView(generic.View):
    def get(self, request):
        if not request.user.is_authenticated:
            success_url = "/"
            basket = Basket(self.request)
            userForm = createUserForm()
            response = render(request, "mainApp/register.html",
                              context={"basket": basket, "form": userForm})
        else:
            response = redirect("/")
        return response

    def post(self, request):
        global userForm
        userForm = createUserForm(request.POST)
        print(userForm)
        print(request.POST)
        if userForm.is_valid():
            generate_code(self.request, userForm)
            response = render(request, "mainApp/emailSend.html")
        else:
            response = render(request, "mainApp/register.html",
                              context={"form": userForm})

        return response

class ForgotPasswordView(generic.View):
    def get(self, request):
        if not request.user.is_authenticated:
            success_url = "/"
            basket = Basket(self.request)
            # pswdChangeForm = PasswordChangeForm()
            response = render(request, "mainApp/changePasswordEmail.html",
                              context={"basket": basket,})
                            #   "form": pswdChangeForm
        else:
            response = redirect("/")
        return response
        

    def post(self, request):
        basket = Basket(self.request)
        if request.POST.get('emailUser'):
            response = render(request, "mainApp/changePasswordHelpText.html",
                                context={"basket": basket,})
        return response


def confirmReg(request):
    print("we are here")
    print(userForm)
    if userForm.is_valid():
        print("huiiiiiiii")
        username = userForm.cleaned_data['username']
        password = userForm.cleaned_data["password1"]
        userForm.save()
        user = authenticate(
            username=username,
            password=password
        )
        login(request, user)
        response = redirect("/")
    return response


def activate(request):
    response = JsonResponse({"OK": "None"})
    if request.POST.get('inputCode'):
        user_code = request.POST.get('inputCode')
        if user_code != request.session['code']:
            response = JsonResponse({"OK": "false"})
        else:
            response = JsonResponse({"OK": "true"})
    return response


def login_view(request):

    loginForm = authForm(request.POST)

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        response = JsonResponse({"OK": "true", "url": "/"})
    else:
        response = JsonResponse({"OK": "false"})
    return response


def logout_view(request):
    logout(request)
    return redirect("/")


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
    response = JsonResponse({'qty': product_qty, "OK": "true"})
    return response


