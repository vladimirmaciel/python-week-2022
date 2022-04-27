alguns comandos utilizados para realizar a aula 1 

- para inserir na base de dados 

In [11]: with Session(engine)as session:
    ...:     beer = Beer(name="Two Chefs",style="QPA", flavor = 5, image=6, cost=6)
    ...:     session.add(beer)
    ...:     session.commit()
    ...:     results = session.exec(select(Beer))
    ...:     for beer in results:
    ...:         print(beer.name)



from sqlmodel import select
from beerlog.database import engine
from beerlog.models import Beer
    

with Session(engine)as session:
    sql = select(Beer)
    results = session.exec(sql)
    for beer in results:
        print(beer.name)


para rodar a API
uvicorn beerlog.api:api --reload