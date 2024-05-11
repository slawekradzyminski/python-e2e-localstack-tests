from dataclasses import dataclass, asdict
from typing import List
from enum import Enum


class Role(Enum):
    ROLE_ADMIN = "ROLE_ADMIN"
    ROLE_CLIENT = "ROLE_CLIENT"


@dataclass
class LoginRequestDto:
    username: str
    password: str

    def to_dict(self):
        return asdict(self)


@dataclass
class LoginResponseDto:
    username: str
    token: str
    email: str
    firstName: str
    lastName: str
    roles: List[Role]
    
    def to_dict(self):
        return asdict(self)
