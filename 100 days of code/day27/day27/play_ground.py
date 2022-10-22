def sm(*arg):
	x = 0
	for i in arg:
		x += i
	return x


# print(sm(1, 2, 3))
# kwargs is dictionary_type
def caculate(n, **kwargs):
	print(kwargs)


caculate(6, add="son")


class Car:
	def __init__(self, **kwargs):
		self.make = kwargs.get("make")
		self.model = kwargs.get("model")


my_car = Car(make="sondeptrai")
print(my_car.make)
