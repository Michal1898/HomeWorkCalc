import re
from threading import Thread, active_count
import requests

results = {}


def send_calculation(operation,
                     first_number,
                     second_number,
                     identifier):
    if operation == "add":
        math_oper = "+"
    elif operation == "sub":
        math_oper = "-"
    else:
        math_oper = "*"
    print(f"Thread {identifier} :  {first_number}{math_oper}{second_number} byla poslána na server.")
    print("Čekání na server.")

    server_path = "https://calc.wmwmw.cz/api/" + operation + "/"
    result = requests.post(server_path, json={"first": first_number, "second": second_number}).json()
    result = result["result"]
    results[identifier] = result
    print(f"Výsledek {identifier} je {result}")


if __name__ == "__main__":
    thread_no = 0
    count_methods = {"add", "sub", "mul"}
    program_end = False
    while not program_end:
        repeat_fun_insertion = True
        while repeat_fun_insertion:
            inserted_string = input("Zadej: typ operace,a,b ")
            pattern = r"([a-z]{3})\,([+]+\d+|[-]+\d+|\d+)\,([+]+\d+|[-]+\d+|\d+)"
            match = re.fullmatch(pattern, inserted_string)

            if match:
                repeat_fun_insertion = True
                math_oper = match.group(1)
                if math_oper in count_methods:
                    a = int(match.group(2))
                    b = int(match.group(3))
                    thread_no += 1
                    repeat_fun_insertion = False

        thread_ident = "#" + str(thread_no)
        print(thread_ident)
        # noinspection SyntaxError
        Thread(target=send_calculation, args=(math_oper, a, b, thread_ident)).start()

        program_end = input("Ukončit program?").lower()
        if program_end == "ano" or program_end == "a":
            program_end = True
        else:
            program_end = False

    print("Program bude ukončen.")
    print("Ukončují se thready.")
    while active_count() > 1:
        pass
    print("Všechny thready ukončeny.")
    print(results)
    print("hotovo")
