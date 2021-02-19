import requests
from threading import Thread
from json import loads

results={}
def send_calculation (operation,
                      first_number,
                      second_number,
                      identifier):

    if (operation=="add"):
        math_op="+"
    elif (operation=="sub"):
        math_op="-"
    else:
        math_op = "*"
    print(f"Thread {identifier} :  {first_number}{math_op}{second_number} byla poslana na server.")
    print("Cekani na server.")

    server_path="https://calc.wmwmw.cz/api/"+operation+"/"
    result=requests.post(server_path, json={"first": first_number, "second": second_number}).json()
    result=result["result"]
    results[identifier]=result
    print((f"Vysledek {identifier} je {result}"))

count_methods= {"add","sub","mul"}
math_op=""
while math_op not in count_methods:
    math_op=input("Zadej matematickou operaci: ").lower()
a=b=0.0
while not isinstance(a, int):
    a=int(input("Zadej hodnotu operandu a: "))
    print(type(a))
while not isinstance(b, int):
    b=int(input("Zadej hodnotu operandu b: "))


t1 = Thread(target=send_calculation, args=("add", 3, 5, "#1"))
t2 = Thread(target=send_calculation, args=("sub", 13,7, "#2"))
t3 = Thread(target=send_calculation, args=("mul", 13,7, "#3"))

# spouštíme vlákna
t3.start()
t2.start()
t1.start()
# čekáme na ně
t1.join()
print(f"soucet hotov: {results}")
t2.join()
print(f"rozdil hotov: {results}")
t3.join()
print(f"soucin hotov: {results}")
print(results)
# a nakonec...
print("hotovo")