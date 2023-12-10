from converter import parse
import mysql.connector
import sys
import time


class Titled_table:
    def __init__(self, values, border_side='|', border_top='-', border_cross='+', border_all=False, border_title_size=1, print_nones=True):
        self.values = values
        self.rows = len(values)
        self.cols = 0
        self.lengths = list()
        self.max_col_len = 0
        self.cols = len(max(*values, key=lambda x: len(x)))
        self.lengths = [0] * self.cols
        for i_r, row in enumerate(values):
            for i_v, value in enumerate(row):
                if value == None and not print_nones:
                    value = ''
                    values[i_r][i_v] = ''
                self.lengths[i_v] = max(self.lengths[i_v], len(str(value)))

        self.__border_length = max(len(border_cross), len(border_side))
        self.border_side = border_side.center(self.__border_length)
        self.border_top = border_top[0]
        self.border_cross = border_cross.center(self.__border_length)
        self.border_all = border_all
        self.border_title_size = border_title_size
        self.print_nones = print_nones

    def __str__(self):
        border_line = '\n' + self.border_cross
        for length in self.lengths:
            border_line = border_line + self.border_top * length + self.border_cross
        text = border_line
        for i_row, row in enumerate(self.values):
            text = text + '\n' + self.border_side
            for i_col in range(self.cols):
                if i_col < len(row):
                    col = row[i_col]
                else:
                    col = ''
                text = text + \
                    str(col).center(self.lengths[i_col]) + self.border_side
            if i_row == 0:
                text = text + border_line * self.border_title_size
            elif self.border_all:
                text = text + border_line
        if not self.border_all:
            text = text + border_line
        return text


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
    '''max_len = 0
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
    print("+", "-" * max_len, "+", sep="")'''
    table = Titled_table(args)
    print(table)


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
        print("Pusty zestaw")
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
        if command.find('*') != -1:
            names = command.split()
            names = names[1:names.index("z")]
            return [names]
        elif command.find(" z ") != -1:
            tbl_name = command.split()
            tbl_name = tbl_name[tbl_name.index('z') + 1]
            if tbl_name.endswith(';'):
                tbl_name = tbl_name[:-1]
            COMMAND = f"select column_name from information_schema.columns where table_name = '{tbl_name}'"
            global cursor, connection
            try:
                cursor.execute(COMMAND)
                output = cursor.fetchall()
                connection.commit()
            except Exception as ex:
                print("Blad", parse(str(ex), 0, 1).lower())
                return cursor.fetchwarnings(), False
            else:
                new_output = [i[0] for i in output]
                return [new_output]

        return [tuple(command.replace(';', '').split()[1:]), ]
    if command.startswith("opis"):
        return [('field', 'type', 'null', 'key', 'default', 'extra')]
    return [command]


cursor = None
connection = None


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
