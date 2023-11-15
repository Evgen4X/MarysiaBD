from converter import parse
import mysql.connector
import sys
import time


def join(iterable, sep, from_=None, to=None):
    text = ''
    for i, v in enumerate(iterable):
        if from_ == None or to == None:
            text += str(v)
        else:
            text += parse(str(v), from_, to)
        if i != 0 and i != len(iterable):
            text += str(sep)
    return text


def print_table(args, from_=None, to=None):
    max_len = 0
    for line in args:
        LEN = len(line)
        if isinstance(line, tuple):
            for el in line:
                max_len = max(max_len, len(str(el)))
        else:
            max_len = max(max_len, len(str(line)))
    DEC = 3 * (LEN - 1) + 1
    max_len = max_len * LEN + DEC
    print("+", "-" * max_len, "+", sep="", end="\n|")
    for el in args[0]:
        if from_ == None or to == None:
            print(str(el).center((max_len - DEC) // LEN), end=" | ")
        else:
            print(parse(el, from_, to), end=" | ")
    print("\n+", "-" * max_len, "+", sep="")
    for line in args[1:]:
        print("|", end="")
        for text in line:
            if from_ == None or to == None:
                print(str(text).center((max_len - DEC) // LEN), end=" | ")
            else:
                print(parse(text, from_, to), end=" | ")
        print()
    print("+", "-" * max_len, "+", sep="")


def run_interpreter(command):
    global cursor, connection
    sql_code = parse(command, 1, 0)
    print(f"PARSED: {sql_code}")
    try:
        cursor.execute(sql_code.strip())
        output = cursor.fetchall()
        connection.commit()
    except Exception as ex:
        print("Blad", parse(str(ex), 0, 1).lower())
        return cursor.fetchwarnings(), False
    if len(output) == 0:
        return cursor.fetchwarnings(), True
    if len(output) == 1:
        if isinstance(output[0], tuple):
            print_table(get_title(command) + output)
        return cursor.fetchwarnings(), True
    print_table(get_title(command) + output)
    return cursor.fetchwarnings(), True


def input_command(database) -> str:
    command = input(f"MarysiaBD[{database}] ").lower()
    if command == '':
        return ''
    if command.startswith('--'):
        return ''
    if command.startswith('/*'):
        while command[-2:] != '*/':
            command += input("    /*> ")
        return ""
    while command[-1] != ';' and fr"{command[-1]}" != '\\g':
        command = command + ' ' + input("    -> ").lower()
    return command


def get_title(command: str):
    if command.startswith("pokazywac") or command.startswith("wybierac"):
        if command.find("z tabela") != -1:
            return []
        return [tuple(command.replace(';', '').split()[1:]), ]
    if command.startswith("opis"):
        return [('field', 'type', 'null', 'key', 'default', 'extra')]
    return [command]


cursor = None
connection = None
'''
Your MariaDB connection id is 33
Server version: 10.4.28-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
'''


def main():
    global cursor, connection
    user, password, host, database = sys.argv[1:]
    try:
        connection = mysql.connector.connect(user=user, password=password,
                                             host=host, database=database)
    except Exception as ex:
        print("Blad", parse(str(ex), 0, 1))
        return
    VERSION = connection._server_version
    print(f'''
Witaj w monitorze MarysiBD. Polecenia koncza sie przez ; lub \g.

Twoj identyfikator polaczenia z MarysiaBD to {connection.connection_id}
Wersja servera: {VERSION[0]}.{VERSION[1]}.{VERSION[2]}-MariaDB
''')
    cursor = connection.cursor()
    command = ""
    while command != "wyjscie;":
        if command.strip():
            start = time.time()
            warnings, success = run_interpreter(command)
            if warnings == None:
                print("0 ostrzezen")
            else:
                print(len(warnings), "ostrzezenia")
            if success:
                print(f"\nZapytanie OK ({time.time() - start:.2f} sec)")
            else:
                print()
        command = input_command(connection.database)
    connection.close()


if __name__ == "__main__":
    main()
