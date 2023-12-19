NO_UPPER = [
    'mysql", "mojsql", "root", "zrodlo'
]

DICT = [
    ("help", "pomoc"),  # basic commands
    ("create", "tworzyc"),
    ("create", "utworzyc"),  # ALTERNATIVE
    ("create", "stworzyc"),  # ALTERNATIVE
    ("drop", "upuszczac"),
    ("alter", "zmieniac"),
    ("insert", "wstawiac"),
    ("update", "aktualizacja"),
    ("update", "aktualizowac"),  # ALTERNATIVE
    ("delete", "usuwac"),
    ("select", "wybierac"),
    ("grant", "nadawac"),
    ("revoke", "uniewaznic"),
    ("replace", "zastepowac"),
    ("exit", "wyjscie"),
    ("desc", "opis"),
    ("use", "uzywac"),

    ("current_user", "aktualny_uzytkownik"),  # functions
    ("count", "liczyc"),
    ("ucase", "dlitery"),
    ("lcase", "mlitery"),
    ("round", "okragly"),
    ("substr", "podtekst"),
    ("position", "pozycja"),
    ("truncate", "sciety"),
    ("truncate", "obciac"),  # ALTERNATIVE
    ("replace", "zastepowac"),
    ("cast", "rzucac"),
    ("convert", "konwertowac"),
    ("min", "min"),
    ("max", "maks"),
    ("sum", "suma"),
    ("avg", "sr"),
    ("floor", "podloga"),
    ("floor", "dol"),  # ALTERNATIVE
    ("ceil", "sufit"),
    ("ceil", "gora"),  # ALTERNATIVE
    ("truncate", "sciety"),
    ("substr")
    ("power", "moc"),
    ("current_date", "aktualny_data"),
    ("current_time", "aktualny_czas"),

    ("show", "pokazywac"),  # DDL
    ("tables", "tabele"),
    ("databases", "bazy_danych"),
    ("database", "baza_danych"),
    ("if", "jesli"),
    ("if", "jezeli"),  # ALTERNATIVE
    ("not", "nie"),
    ("exists", "istnieje"),
    ("exist", "istniec"),
    ("ignore", "ignorowac"),
    ("like", "lubic"),
    ("table", "tabela"),
    ("column", "kolumna"),
    ("as", "jak"),
    ("index", "indeks"),
    ("key", "klucz"),
    ("primary", "podstawowy"),
    ("add", "dodawac"),
    ("constraint", "ograniczenie"),
    ("unique", "unikalny"),
    ("fulltext", "pelny_tekst"),
    ("spatial", "przestrzenny"),
    ("visible", "widoczny"),
    ("invisible", "niewidzialny"),
    ("invisible", "niewidoczny"),  # ALTERNATIVE
    ("auto_increment", "auto_przyrost"),
    ("comment", "comentarz"),
    ("collate", "zestawiac"),
    ("collate", "zestawic"),  # ALTERNATIVE
    ("column_format", "format_kolumny"),
    ("column_format", "kolumna_format"),  # ATLERNATIVE
    ("fixed", "naprawiony"),
    ("default", "domyslny"),
    ("engine_attribute", "silnik_atrybut"),
    ("engine_attribute", "atrybut_silnika"),  # ALTERNATIVE
    ("secondary_engine_attribute", "wtorny_silnik_atrybut"),
    ("secondary_engine_attribute", "atrybut_drugiego_silnika"),  # ALTERNATIVE
    ("storage", "magazyn"),
    ("disk", "dysk"),
    ("memory", "pamiec"),
    ("generated", "wygenerowany"),
    ("always", "zawsze"),
    ("virtual", "wirtualny"),
    ("null", "zero"),
    ("null", "nic"),  # ALTERNATIVE
    ("stored", "przechowywany"),
    ("check", "sprawdzac"),
    ("enforced", "wymuszony"),
    ("references", "bibliografia"),
    ("references", "odnosi_sie"),  # ALTERNATIVE
    ("references", "odniesienia"),  # ALTERNATIVE
    ("match", "mecz"),
    ("partial", "czesciowy"),
    ("simple", "prosty"),
    ("on", "na"),
    ("dynamic", "dynamiczny"),
    ("restrict", "ograniczac"),
    ("cascade", "kaskada"),
    ("set", "ustawiac"),
    ("set", "ustawic"),  # ALTERNATIVE
    ("no", "brak"),
    ("action", "dzialanie"),
    ("partition", "przegroda"),
    ("by", "przez"),
    ("linear", "liniowy"),
    ("hash", "hasz"),
    ("algorithm", "algorytm"),
    ("values", "wartosci"),
    ("data", "dane"),
    ("load", "zaladowac"),
    ("load", "zaladowywac"),  # ALTERNATIVE
    ("local", "lokalny"),
    ("infile", "wplik"),
    ("infile", "wnetrzny_plik"),  # ALTERNATIVE
    ("fields", "pola"),
    ("ternimated", "terminowany"),
    ("terminated", "zakonczony"),  # ALTERNATIVE
    ("lines", "linie"),
    ("into", "w_do"),
    ("outfile", "zplik"),
    ("outfile", "zewnetrzny_plik"),  # ALTERNATIVE
    ("from", "z"),
    ("in", "w"),
    ("character", "postac"),
    ("where", "gdzie"),
    ("schema", "schemat"),
    ("function", "funkcjonowac"),
    ("function", "funkcja"),  # ALTERNATIVE
    ("event", "wydarzenie"),
    ("definer", "definitor"),
    ("schedule", "harmonogram"),
    ("enable", "wlaczyc"),
    ("disable", "wylaczyc"),
    ("interval", "interwal"),
    ("do", "zrobic"),
    ("year", "rok"),
    ("quarter", "kwartal"),
    ("month", "miesiac"),
    ("hour", "godzina"),
    ("minute", "minuta"),
    ("second", "drugi"),
    ("week", "tydzien"),
    ("competition", "konkurs"),
    ("preserve", "utrzymywac"),
    ("starts", "zaczyna"),
    ("ends", "konczy"),
    ("procedure", "procedura"),
    ("returns", "zwraca"),
    ("returns", "zwroty"),  # ALTERNATIVE
    ("language", "jezyk"),
    ("server", "serwer"),
    ("wrapper", "obwoluta"),
    ("trigger", "spust"),
    ("for", "dla"),
    ("each", "kazdy"),
    ("row", "wiersz"),
    ("rename", "przemianowac"),
    ("to", "do"),
    ("encryption", "szyfrowanie"),
    ("read", "czytac"),
    ("only", "tylko"),
    ("completion", "ukonczenie"),
    ("contains", "zawiera"),
    ("modifies", "modyfikuje"),
    ("options", "opcje"),
    ("first", "prierszy"),
    ("after", "po"),
    ("change", "zmiana"),
    ("change", "przemieniac"),  # ALTERNATIVE
    ("lock", "zamek"),
    ("modify", "modyfikowac"),
    ("order", "zamowienie"),
    ("validation", "walidacja"),
    ("with", "z"),
    ("without", "bez"),
    ("foreign", "zagraniczny"),
    ("temporary", "tymczasowy"),
    ("tinyint", "malutkicalk"),
    ("boolean", "logiczny"),
    ("smallint", "malycalk"),
    ("mediumint", "srednicalk"),
    ("int", "calk"),
    ("integer", "calkowity"),
    ("bigint", "duzycalk"),
    ("blob", "kropla"),
    ("decimal", "dziesietny"),
    ("numeric", "numeryczny"),
    ("bit", "fragment"),
    ("float", "platforma"),
    ("double", "podwojnie"),
    ("real", "prawdziwy"),
    ("date", "data"),
    ("datetime", "datagodzina"),
    ("timestamp", "znak_czasu"),
    ("time", "czas"),
    ("char", "znak"),
    ("varchar", "zmienznak"),
    ("binary", "dwojkowy"),
    ("varbinary", "zmienny_dwojkowy"),
    ("enum", "wyliczenie"),
    ("text", "tekst"),

    ("having", "majacy"),  # DQL
    ("group", "grupa"),
    ("limit", "limit"),
    ("join", "dolaczyc"),
    ("join", "zlaczyc"),  # ALTERNATIVE
    ("join", "zlaczenie"),  # ALTERNATIVE
    ("inner", "wewnetrzny"),
    ("left", "lewy"),
    ("right", "prawidlowy"),
    ("right", "prawy"),  # ALTERNATIVE
    ("full", "pelny"),

    ('call', 'dzwonic'),  # DML
    ('low_priority', 'niski_priorytet'),
    ('quick', 'szybki'),
    ('ignore', 'ignorowac'),
    ('except', 'oprocz'),
    ('except', 'wyjatek'),  # ALTERNATIVE
    ('distinct', 'odrebny'),
    ('handler', 'treser'),
    ('open', 'otwierac'),
    ('close', 'zamykac'),
    ('import', 'importowac'),
    ('import', 'import'),  # ALTERNATIVE
    ('delayed', 'opozniony'),
    ('high_priority', 'wysoki_priorytet'),
    ('value', 'wartosc'),
    ('duplicate', 'duplikowac'),
    ('intersect', 'przecinac'),
    ('straight_join', 'prosto_dolaczyc'),
    ('distinctrow', 'odrebnywiersz'),
    ('offset', 'zrownowazyc'),
    ('union', 'unia'),

    ("privileges", "przywileje"),  # DCL

    ("commit", "popelniac"),  # TCL
    ("rollback", "wycofanie"),

    ("error", "blad"),  # outputs
    ("query", "zapytanie"),
    ("unknown", "nieznany"),
    ("you", "ty"),
    ("have", "posiadac"),
    ("an", "jakis"),
    ("your", "twoj"),
    ("syntax", "skladnia"),
    ("the", "ten"),
    ("manual", "reczny"),
    ("that", "ktory"),
    ("corresponds", "odpowiada"),
    ("MariaDB", "MarysiaBD"),
    ("version", "wersja"),
    ("near", "blisko"),
    ("at", "na"),
    ("line", "linia"),
    ("changed", "zmieniony"),
    ("enpty", "pusty"),
    ("affected", "dotkniety"),
    ("extra", "dodatkowy"),
    ("warning", "ostrzezenie"),
    ("warnings", "ostrzezenia"),
    ("incorrect", "bledny"),
    ("level", "poziom"),
    ("code", "kod"),
    ("message", "wiadomosc"),
    ("doesn't", "nie"),
    ("incorrectly", "nieprawidlowo"),
    ("formed", "uformowany"),
    ("of", "z"),
    ("is", "jest"),
    ("entry", "wejscie"),
    ("can't", "nie mozna"),
    ("connect", "laczyc"),
]

'''
table_option: {
    AUTOEXTEND_SIZE [=] value
  | AUTO_INCREMENT [=] value
  | AVG_ROW_LENGTH [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | CONNECTION [=] 'connect_string'
  | {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTION [=] {'Y' | 'N'}
  | ENGINE [=] engine_name
  | ENGINE_ATTRIBUTE [=] 'string'
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] value
  | MAX_ROWS [=] value
  | MIN_ROWS [=] value
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | START TRANSACTION 
  | SECONDARY_ENGINE_ATTRIBUTE [=] 'string'
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value
  | tablespace_option
  | UNION [=] (tbl_name[,tbl_name]...)
}'''


def trip(text):
    start = 0
    end = 0
    for i, v in enumerate(text):
        if v in 'abcdefghijklmnopqrstuvwxyz':
            start = i
            break
    for i, v in enumerate(text[::-1]):
        if v in 'abcdefghijklmnopqrstuvwxyz':
            end = len(text) - i
            break
    return text[:start], text[start:end], text[end:]


def replace(value: str, from_, to):
    start, value, end = trip(value)

    for i in DICT:
        if value in '\a\v\f\r\t\b\n':
            return start + value + end
        if value == i[from_]:
            new = i[to]
            if new not in NO_UPPER:
                new = new.upper()
            return start + new + end
    return start + value + end


def parse(text: str, from_: int, to: int) -> str:
    new_text = ""
    for line in text.splitlines():
        first = False
        for word in line.lower().split():
            if first:
                new_text = new_text + " "
            first = True
            if word.startswith("%") and word.endswith("%"):
                new_text = new_text + word[1:-1]
            else:
                new_text = new_text + replace(word, from_, to)
        new_text += '\n'
    return new_text


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python MarysiaBD <file.bd>")
        sys.exit(1)

    import subprocess

    input_file = sys.argv[1]

    with open(input_file, "r") as file:
        host = file.readline()[2:].strip()
        user = file.readline()[2:].strip()
        password = file.readline()[2:].strip()

    print(f"HOST: {host}")
    print(f"USER: {user}")
    print(f"PASSWORD: {password}")

    with open(input_file, "r") as file:
        bd_code = file.read()

    sql_code = parse(bd_code, 1, 0)

    with open("temp_file.sql", "w") as f:
        f.write(sql_code)

    try:
        output = subprocess.run(
            ["mysql", f"--host={host}", "--execute", f"source temp_file.sql"], stdout=subprocess.PIPE, text=True)
        output = parse(output, 0, 1)
        print(output)
    except Exception as ex:
        print(ex)
        print("Please, make sure to enter your SQL host in the first line, username in the 2nd and password in the 3rd useing SQL comment. E.g.:\n--localhost\n--root\n--qwerty1234")


if __name__ == "__main__":
    main()
