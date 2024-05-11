from dataclasses import dataclass, asdict
from typing import List

@dataclass
class UserDetails:
    username: str
    email: str
    firstName: str
    lastName: str
    roles: List[str]
    id: int

    def to_dict(self):
        return asdict(self)
