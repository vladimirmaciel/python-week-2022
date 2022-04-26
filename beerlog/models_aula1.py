# from dataclasses import dataclass
from sqlmodel import SQLModel


@dataclass  # é uma função que utiliza o padrao decorator, ela altera o comportamento da classe Beer, injentando novos metodos e atributos que não foram definidos
class Beer:
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brewdog = Beer(name="Bewdog", style="NEIPA", flavor=6, image=8, cost=8)
