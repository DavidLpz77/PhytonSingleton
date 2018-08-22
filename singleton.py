class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance
class Juegos(Singleton):
	nombre = u""
		
a = Juegos()
b = Juegos()
 
a.nombre = u"Mario"
b.nombre = u"Zelda"
print (a.nombre, b.nombre) # Gorrion Gorrion
