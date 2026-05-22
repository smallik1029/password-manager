import argparse
from cli.commands import cmd_init, cmd_add, cmd_get, cmd_list, cmd_delete


def main():
    parser = argparse.ArgumentParser(description="Local password manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Create a new vault")
    subparsers.add_parser("add", help="Add a new entry")
    subparsers.add_parser("list", help="List all entries")

    get_parser = subparsers.add_parser("get", help="Get an entry")
    get_parser.add_argument("site", help="Site name")

    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("site", help="Site name")

    args = parser.parse_args()

    if args.command == "init":
        cmd_init()
    elif args.command == "add":
        cmd_add()
    elif args.command == "get":
        cmd_get(args.site)
    elif args.command == "list":
        cmd_list()
    elif args.command == "delete":
        cmd_delete(args.site)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()