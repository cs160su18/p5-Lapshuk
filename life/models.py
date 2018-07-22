from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
  
class Item(models.Model):
  total_quantity = models.IntegerField()
  description = models.CharField(max_length=100)
  product_id = models.CharField(max_length=14)
  size = models.CharField(max_length=4)
  
  def getQuantity(self):
    return self.total_quantity;
  
  def __str__(self):
    return "\nTotal Quantity: " + str(self.total_quantity) + "\nDescription: " + self.description + "\nProduct Id: " + self.product_id

  
  
class Person(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20) 
  user_id = models.IntegerField()
  
  def getFirstName(self):
    return self.first_name;
  def getLastName(self):
    return self.first_name;
  def getUserId(self):
    return self.user_id;
  
  def __str__(self):
    return "\nFirst Name: " + self.first_name + "\nLast Name: " + self.last_name + "\nUser ID: " + str(self.user_id)
  
  
  
class Cart(models.Model):
  product_id = models.CharField(max_length=14)
  user_id = models.IntegerField()
  quantity = models.IntegerField()
  
  def __str__(self):
    return "Person's ID: " + str(self.user_id) + "\nProduct_id" + str(self.product_id) + "\nQuantity:" + str(self.quantity)


  
    
