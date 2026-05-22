from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class VaultEntry:
    site: str
    username: str
    password: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
