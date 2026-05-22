import getpass
from vault.manager import VaultManager


def cmd_add(vm: VaultManager) -> None:
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    vm.add(site, username, password)
    print(f"Entry for {site} saved.")


def cmd_get(vm: VaultManager, site: str) -> None:
    entry = vm.get(site)
    if entry:
        print(f"Site:     {entry.site}")
        print(f"Username: {entry.username}")
        print(f"Password: {entry.password}")
        print(f"Created:  {entry.created_at}")
    else:
        print(f"No entry found for {site}.")


def cmd_list(vm: VaultManager) -> None:
    entries = vm.list_entries()
    if entries:
        for site in entries:
            print(f"  - {site}")
    else:
        print("No entries in vault.")


def cmd_delete(vm: VaultManager, site: str) -> None:
    if vm.get(site):
        vm.delete(site)
        print(f"Entry for {site} deleted.")
    else:
        print(f"No entry found for {site}.")