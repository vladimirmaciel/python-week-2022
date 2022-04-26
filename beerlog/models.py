from datetime import datetime
from statistics import mean
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel, select


# herda do SQLModel, passando agora ser uma calsse de um ORM
class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


# brewdog = Beer(name="Brewdog", style="NEIPA", flavor=5, image=8, cost=8)
# cerva = Beer(name="Skol", style="trigo", flavor=2, image=3, cost=9)

# try:
#     brewdog = Beer(name="Brewdog", style="NEIPA", flavor=8, image=6, cost=8)
# except RuntimeError:
#     print("Zica de mais!!")
