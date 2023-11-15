import argparse
import subprocess


def login(user, password, host, database):
    print(f"{user}@host={host if host else '<none>'}[db={database}]")
    subprocess.call(["python", "marysiabd.py", user, password, host, database])
    print("Czesc!")


def main():
    parser = argparse.ArgumentParser(description="MarysiaBD Interpreter")
    parser.add_argument('--user', '-u', dest='user', type=str, default="root",
                        help="Username will be used as mysql -u [username]. Default - \"root\"")
    parser.add_argument('--password', '-p', dest='password', type=str, default="",
                        help="Password will be used as mysql -p [password]. Default - \"\"")
    parser.add_argument("--host", dest="host", type=str, default="",
                        help="Host will be used as mysql -h [host]. Default = \"\"")
    parser.add_argument("--database", "-d", dest="database", default="",
                        help="Database will be used as mysql -u [user] [database]. Default = \"\"")
    args = parser.parse_args()
    # run_interpreter(args.input_file)
    login(args.user, args.password, args.host, args.database)


if __name__ == "__main__":
    main()
