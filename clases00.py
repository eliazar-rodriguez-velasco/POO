class Hello:
	def __init__(self):            
		pass                       # paso bien , todo listo 

	def add (self,number1,number2):
		return number1+number2
	def div (self,number1,number2):
		return number1/number2
object = Hello()                   #instancia=objeto
print("add", object.add(5,6))
