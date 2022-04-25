from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum as Enum_, IntEnum

from models.user_models import User


class Enum(Enum_):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class GemTypes(str, Enum):
    DIAMOND = 'DIAMOND'
    RUBY = 'RUBY'
    EMERALD = 'EMERALD'


class GemClarity(IntEnum):
    SI = 1
    VS = 2
    VVS = 3
    FL = 4


class GemColor(str, Enum):
    D = 'D'
    E = 'E'
    G = 'G'
    F = 'F'
    H = 'H'
    I = 'I'


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    size: float = 1
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None
    gem: Optional['Gem'] = Relationship(back_populates='gem_properties')


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float
    available: bool = True
    gem_type: GemTypes = GemTypes.DIAMOND
    gem_properties_id: Optional[int] = Field(default=None, foreign_key='gemproperties.id')
    gem_properties: Optional[GemProperties] = Relationship(back_populates='gem')
    seller_id: Optional[int] = Field(default=None, foreign_key='user.id')
    seller: Optional[User] = Relationship()


class GemPatch(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    price:  Optional[float] = 1000
    available:  Optional[bool] = True
    gem_type:  Optional[GemTypes] = GemTypes.DIAMOND

    gem_properties_id: Optional[int] = Field(default=None, foreign_key='gemproperties.id')
    gem_properties: Optional[GemProperties] = Relationship(back_populates='gem')