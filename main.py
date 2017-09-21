from time import sleep
import requests
from random import randint

MIN = -27654321
MAX = 27654321

def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def dev(a,b):
    return a / b

def pow(a,b):
    return a ** b

def calc_tester(fn_name, operator, max_req):
    print('Testing funcion: {0}'.format(fn_name))
    timeout = 60/max_req
    was_error = False
    
    for i in range(max_req):
        a = randint(MIN, MAX) 
        b = randint(MIN, MAX)
        res = operator(a,b)
        r = requests.get("http://127.0.0.1:8080/{0}/{1}/{2}/".format(fn_name, a, b))
        
        if r.status_code != 200:
            print("{0}: error in response. Args: {1}, {2}".format(fn_name, a, b))
            was_error = True
            continue

        if r.text != str(res):
            print("{0}: error in answer. Args: {1}, {2}".format(fn_name, a, b))
            was_error = True

        sleep(timeout)

    # r = requests.get("http://127.0.0.1:8080/{0}/{1}/{2}/".format(fn_name, MAX + 1, MIN - 1))
    # if r.status_code != 400:
    #     was_error = True
    #     print("{0}: error: expected status code 400 with args: {1}, {2}".format(fn_name, MAX + 1, MIN - 1))

    if not was_error:
        print('{0} function is ok'.format(fn_name))
    else:
        print('{0} function was executed with errors'.format(fn_name))



r = requests.get("http://127.0.0.1:8080/fff/abc/abc/")
if r.status_code != 404:
    print("error in request = /fff/abc/abc/")


calc_tester("sum", sum, 5000)
calc_tester("sub", sub, 3000)
calc_tester("mul", mul, 2000)
calc_tester("dev", dev, 2000)
calc_tester("pow", pow, 2000)


