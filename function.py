# def 関数名(引数) :
#    実効する処理文

def sayHello() :
    print("HelloWorld")

sayHello()

def sayHello(greeting) :
    print(greeting)

sayHello("Hello")

hello = sayHello

hello("Good Morning")

def average(arg01, arg02, arg03) :
    average = (arg01 + arg02 + arg03) / 3 
    return average


print(average(9, 4, 2))