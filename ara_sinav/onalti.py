class a:
   a = b = None
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __str__(self):
      return self.a+self.b

b = a("3", "5")
print(b)
