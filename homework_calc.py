import requests
from threading import Thread, active_count
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

thread_no=0
count_methods= {"add","sub","mul"}
program_end=False
while not program_end:
    math_op = ""
    while math_op not in count_methods:
        math_op=input("Zadej matematickou operaci: ").lower()
    a=b=0.0
    while not isinstance(a, int):
        a=int(input("Zadej hodnotu operandu a: "))
    while not isinstance(b, int):
        b=int(input("Zadej hodnotu operandu b: "))
    thread_no+=1

    thread_ident="#"+str(thread_no)
    print(thread_ident)
    Thread(target=send_calculation, args=(math_op, a, b, thread_ident)).start()

    program_end=input("Ukoncit program?").lower()
    if program_end=="ano" or program_end=="a":
        program_end==True
    else:
        program_end=False

print("Program bude ukoncen.")
print("Ukoncuji se Thready.")
while(active_count()>1):
    pass
print("Vsechny thready ukonceny.")
print(results)
print("hotovo")