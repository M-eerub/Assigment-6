# step 16 (Function Decorators)

def log(func):
  def wrapper():
    print("Function is being called")
    return func()
  return wrapper
@log
def says():
  print("Hello")
says()

