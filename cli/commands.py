import getpass
from vault.manager import VaultManager
from vault.store import vault_exists


def get_master_password() -> str:
    return getpass.getpass("Master password: ")


def cmd_init():
    if vault_exists():
        print("Vault already exists.")
        return
    password = getpass.getpass("Create master password: ")
    confirm = getpass.getpass("Confirm master password: ")
    if password != confirm:
        print("Passwords do not match.")
        return
    VaultManager(password)
    print("Vault created.")


def cmd_add():
    try:
        vm = VaultManager(get_master_password())
    except ValueError:
        print("Wrong master password.")
        return
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    vm.add(site, username, password)
    print(f"Entry for {site} saved.")


def cmd_get(site: str):
    try:
        vm = VaultManager(get_master_password())
    except ValueError:
        print("Wrong master password.")
        return
    entry = vm.get(site)
    if entry:
        print(f"Site:     {entry.site}")
        print(f"Username: {entry.username}")
        print(f"Password: {entry.password}")
        print(f"Created:  {entry.created_at}")
    else:
        print(f"No entry found for {site}.")


def cmd_list():
    try:
        vm = VaultManager(get_master_password())
    except ValueError:
        print("Wrong master password.")
        return
    entries = vm.list_entries()
    if entries:
        for site in entries:
            print(f"  - {site}")
    else:
        print("No entries in vault.")


def cmd_delete(site: str):
    try:
        vm = VaultManager(get_master_password())
    except ValueError:
        print("Wrong master password.")
        return
    if vm.get(site):
        vm.delete(site)
        print(f"Entry for {site} deleted.")
    else:
        print(f"No entry found for {site}.")