import getpass
from vault.manager import VaultManager
from vault.store import vault_exists
from cli.commands import cmd_add, cmd_get, cmd_list, cmd_delete, cmd_update, GREEN, RED, RESET

def unlock_vault() -> VaultManager | None:
    if not vault_exists():
        print(f"No vault found. Creating a new one.")
        password = getpass.getpass("Create master password: ")
        confirm = getpass.getpass("Confirm master password: ")
        if password != confirm:
            print(f"{RED}Passwords do not match.{RESET}")
            return None
        vm = VaultManager(password)
        print(f"{GREEN}Vault created.{RESET}\n")
        return vm
    else:
        try:
            return VaultManager(getpass.getpass("Master password: "))
        except ValueError:
            print(f"{RED}Wrong master password.{RESET}")
            return None

def main():
    vm = unlock_vault()
    if vm is None:
        return

    print(f"{GREEN}Vault unlocked.{RESET} Commands: add, get <site>, list, delete <site>, update <site>, exit\n")

    while True:
        raw = input("> ").strip()
        if not raw:
            continue

        parts = raw.split(maxsplit=1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None

        if command == "exit":
            break
        elif command == "add":
            cmd_add(vm)
        elif command == "list":
            cmd_list(vm)
        elif command == "get":
            if arg:
                cmd_get(vm, arg)
            else:
                print(f"{RED}Usage:{RESET} get <site>")
        elif command == "delete":
            if arg:
                cmd_delete(vm, arg)
            else:
                print(f"{RED}Usage:{RESET} delete <site>")
        elif command == "update":
            if arg:
                cmd_update(vm, arg)
            else: 
                print(f"{RED}Usage:{RESET} update <site>")
        else:
            print(f"{RED}Unknown command.{RESET} Commands: add, get <site>, list, delete <site>, update <site>, exit")

if __name__ == "__main__":
    main()