from sqlalchemy.orm import joinedload
from sqlmodel import Session, select
from .models import Pessoa, engine, Book


def create_pessoas(idade: int, nome: str):
    person = Pessoa(nome = nome, idade = idade)    
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
    return person

def create_books(titulo: str, pessoa_id:int):
    book = Book(titulo=titulo, pessoa_id=pessoa_id)    
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
    return book

def get_pessoas(id:int=None,idade:int = None, limit:int = None):
    query = select(Pessoa)
    if id:
        query = query.where(Pessoa.id == id)
    if idade:
        query = query.where(Pessoa.idade == idade)
    if limit:
        query= query.limit(limit)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
        
    return result

def get_books():
    query = select(Book).options(joinedload('*'))
    
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()    
    return result



def update_pessoas( id:int ,nome:str,idade:int): 
   with Session(engine) as session:
    query = select(Pessoa)
    if id:
     query = query.where(Pessoa.id == id)
    result = session.exec(query)

    pessoa_up = result.one()

    pessoa_up.nome=nome
    pessoa_up.idade =idade

    session.add(pessoa_up)
    session.commit()   
    session.refresh(pessoa_up) 
    

    return pessoa_up


def delete_pessoas(id:int): 
   with Session(engine) as session:
    query = select(Pessoa)

    if id:
     query = query.where(Pessoa.id == id)

     result = session.exec(query)

     pessoa_id = result.one()

     session.delete(pessoa_id)

     session.commit()    

    result = 'Deletado com sucesso'

    return result


     









    
   
        
      
    

  
   
    
