from dataclasses import dataclass, asdict
from typing import List


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
    roles: List[str]
    
    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_json(cls, data):
        return cls(**data)