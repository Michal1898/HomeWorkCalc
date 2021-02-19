import requests
from threading import Thread
from json import loads

results={}
def send_calculation (operation,
                      first_number,
                      second_number,
                      identifier):
    server_path="https://calc.wmwmw.cz/api/"+operation+"/"
    print (server_path, operation)
    result=requests.post(server_path, json={"first": first_number, "second": second_number}).json()
    result=result["result"]
    results[identifier]=result


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