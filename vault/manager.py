import json
from vault.store import save_vault, load_vault, load_salt, vault_exists
from crypto.kdf import generate_salt, derive_key
from models.entry import VaultEntry


class VaultManager:
    def __init__(self, password: str):
        if vault_exists():
            self.salt = load_salt()
            self.key = derive_key(password, self.salt)
            self.vault = load_vault(self.key)
        else:
            self.salt = generate_salt()
            self.key = derive_key(password, self.salt)
            self.vault = {}
            save_vault(self.vault, self.key, self.salt)

    def add(self, site: str, username: str, password: str) -> None:
        self.vault[site] = VaultEntry(site, username, password).to_dict()
        save_vault(self.vault, self.key, self.salt)

    def get(self, site: str) -> VaultEntry | None:
        entry = self.vault.get(site)
        return VaultEntry.from_dict(entry) if entry else None

    def list_entries(self) -> list[str]:
        return list(self.vault.keys())

    def delete(self, site: str) -> None:
        if site in self.vault:
            del self.vault[site]
            save_vault(self.vault, self.key, self.salt)