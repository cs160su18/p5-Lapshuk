from django.shortcuts import render
from django.core import serializers
from life.models import *
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'life/index.html')
  
def scan(request):
    return render(request, 'life/scan.html')
  
def item(request):
    return render(request, 'life/item.html')
    
def stock(request):
    return render(request, 'life/stock.html')
   
  
def item_details(request):  
    
    item = Item.objects.filter(product_id=request.GET.get('id'))
    if len(item) > 0:
      item = serializers.serialize('json',item)
      return HttpResponse(item, content_type="application/json")
    else:
      return HttpResponse("")
      
      

def cart(request):
    return render(request, 'life/cart.html')    
  
def cart_details(request):
    cart_items  = Cart.objects.filter(user_id=request.GET.get('user_id'))
    if len(cart_items) > 0:
      cart_items = serializers.serialize('json', cart_items)
      return HttpResponse(cart_items, content_type="application/json")
    else:
      return HttpResponse("") 
    
def add_to_cart(request):
  product_id = request.GET.get('product_id')
  user_id = request.GET.get('user_id')
  quantity = request.GET.get('quantity')
  #decrease the total quantity of the item
  item = Item.objects.get(product_id=product_id)
  if item.total_quantity == 0:
    return HttpResponse("")
  item.total_quantity=item.getQuantity()-1
  item.save()
  #adding to cart for current user
  o = Cart(product_id=product_id,user_id=user_id,quantity=quantity)
  o.save()
  return HttpResponse("") 
    
def user_details_by_id(request):
    user  = Person.objects.filter(user_id=request.GET.get('user_id'))
    if len(user) > 0:
      user = serializers.serialize('json', user) 
      return HttpResponse(user, content_type="application/json")
    else:
      return HttpResponse("") 
    
    
def add_stock(request):
  total_quantity = int(request.GET.get('total_quantity'))
  description = request.GET.get('description')
  product_id = request.GET.get('product_id')
  size = request.GET.get('size')
  Item(total_quantity=total_quantity, description=description,product_id=product_id,size=size).save()
  return HttpResponse("") 
  
  
    
  

  
  