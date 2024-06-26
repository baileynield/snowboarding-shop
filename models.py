from enum import Enum
from pydantic import BaseModel


class Brand(Enum):
    NITRO = "Nitro"
    SALOMAN = "Saloman"
    BURTON = "Burton"

class Board(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand