from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class VaultEntry:
    site: str
    username: str
    password: str
    created_at: str = field(default_factory=lambda: datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"))

    def to_dict(self) -> dict:
        return {
            "site": self.site,
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at,
        }
    
    @staticmethod
    def from_dict(data: dict) -> "VaultEntry":
        return VaultEntry(
            site=data["site"],
            username=data["username"],
            password=data["password"],
            created_at=data["created_at"],
        )