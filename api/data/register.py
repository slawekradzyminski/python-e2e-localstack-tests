from dataclasses import dataclass, asdict
from typing import List


@dataclass
class RegisterRequestDto:
    username: str
    password: str
    email: str
    firstName: str
    lastName: str
    roles: List[str]

    def to_dict(self):
        return asdict(self)
