from sqlalchemy import create_engine, Column, Integer, String, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def infor_banco():
    USUARIO = 'root'
    SENHA = 'samsunggbte342'
    HOST = 'localhost'
    BANCO = 'apibd'
    PORT = 3306
    conn = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'
    engine = create_engine(conn, echo=False)
    return engine

def conect_banco():
    Session = sessionmaker(bind=infor_banco())
    return Session()


class Pessoa(Base):
    __tablename__ = 'CADASTRO'
    id = Column(Integer, primary_key=True)
    Nome_Produto = Column(String(20))
    Categoria = Column(String(20))

Base.metadata.create_all(infor_banco())