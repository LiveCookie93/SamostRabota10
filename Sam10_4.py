from functools import wraps
#используем встроенный в Python декоратор @wraps.
#Этот декоратор копирует свойства __name__, __doc__ и другие из функции f()
# в функцию wrapper(), чтобы при отладке программы все выглядело так, будто wrapper() и есть функция f()

def hello_decorator(f):
    #создаем функцию
   @wraps(f)
   def wrapper(*args, **kwargs):
#Аргументы функции wrapper(): *args и **kwargs. Аргумент *args собирает позиционные аргументы, а **kwargs — именованные
       print('Hello from decorator!')
#В первой строке тела функции wrapper() в консоль выводится «Hello from decorator!» — единственный «побочный эффект»
       return f(*args, **kwargs)
#Например, в вызове: wrapper(1, ‘a’, x=5, y=None) значение args — кортеж (1, ‘a’),
# а kwargs — словарь {‘x’: 5, ‘y’: None}. Если позиционных аргументов при вызове функции нет, args — пустой,
# и если нет именованных аргументов, пустой — kwargs

   return wrapper
#В последней строке функции hello_decorator() возвращаем функцию-обертку wrapper().
# Так мы указываем, что нужно подставить на место декорируемой функции f(). Вызывать функцию wrapper() не нужно — возвращаем саму функцию

@hello_decorator
def sum2(a, b):
   return a + b

print(sum2(1,5))