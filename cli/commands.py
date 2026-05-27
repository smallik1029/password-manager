import getpass
import pyperclip
from vault.manager import VaultManager

# color constants
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def cmd_add(vm: VaultManager) -> None:
    while not (site := input("Site: ").strip()):
        print(f"{RED}Site cannot be empty.{RESET}")
    while not (username := input("Username: ").strip()):
        print(f"{RED}Username cannot be empty.{RESET}")
    while not (password := getpass.getpass("Password: ")):
        print(f"{RED}Password cannot be empty.{RESET}")
    vm.add(site, username, password)
    print(f"Entry for {GREEN}{site}{RESET} saved.")


def cmd_get(vm: VaultManager, site: str) -> None:
    entry = vm.get(site)
    if entry:
        pyperclip.copy(entry.password)
        print(f"Site:     {GREEN}{entry.site}{RESET}")
        print(f"Username: {GREEN}{entry.username}{RESET}")
        print(f"Password: {GREEN}copied to clipboard{RESET}")
        print(f"Created:  {GREEN}{entry.created_at}{RESET}")
    else:
        print(f"{RED}No entry found for {site}.{RESET}")

def cmd_list(vm: VaultManager) -> None:
    entries = vm.list_entries()
    if entries:
        for site in entries:
            print(f"  - {GREEN}{site}{RESET}")
    else:
        print(f"{RED}No entries in vault.{RESET}")

def cmd_delete(vm: VaultManager, site: str) -> None:
    if vm.get(site):
        vm.delete(site)
        print(f"Entry for {GREEN}{site}{RESET} deleted.")
    else:
        print(f"{RED}No entry found for {site}.{RESET}")    

def cmd_update(vm: VaultManager, site: str) -> None:
    if not vm.get(site):
        print(f"{RED}No entry found for {site}{RESET}.")
        return
    while not (username := input("New username: ").strip()):
        print(f"{RED}Username cannot be empty.{RESET}")
    while not (password := getpass.getpass("New password: ")):
        print(f"{RED}Password cannot be empty.{RESET}")
    vm.update(site, username, password)
    print(f"Entry for {GREEN}{site}{RESET} successfully updated.")