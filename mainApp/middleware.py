from .basket import Basket

class BasketMiddleWare():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # self.session = request.session

        # basket = self.session.get('basket')
        # if 'basket' not in request.session:
        #     basket = self.session['basket'] = Basket()

        response = self.get_response(request)
        return response