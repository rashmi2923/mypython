#Inheritance
class parent:
  def function(self):
    print("i am good")
class child(parent):
  def function(self):
    print("i am beautiful")
obj=child()
obj.function()    
