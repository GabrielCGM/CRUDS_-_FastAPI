from fastapi import FastAPI
from model import infor_banco, conect_banco, Pessoa

#Criando uma instância do FastAPI
app = FastAPI()

#Criando uma instância da conexão do BD para usar posteriormente
session = conect_banco()


# Cadastrar no BANCO DE DADOS
@app.post('/cadastrar')
def cadastrar_produto(nome_produt: str, categori: str):
    try:

        #Verificando se  exisite algum produto/categoria com os mesmos valores inseridos 
        y = session.query(Pessoa).filter_by(Nome_Produto=nome_produt, Categoria=categori).all()

        #True >>> ele não cadastra e retornar uma MSG
        if len(y) != 0:
            return 'Produto já cadastrado.'
        
        
        #False >>> ele cadastra o produto/categoria no BD
        else:

            x = Pessoa(Nome_Produto=nome_produt, Categoria=categori)
            session.add(x)
            session.commit()
            return f'Produto {nome_produt} cadastrado com sucesso.'
            
    except:
        return 'ERRO AO CADASTRAR.'

#Update
@app.post('/update')
def update_prod(nome_produt:str, nova_categ:str):
    try:
        #Verifica se o produto inserido existe no BD
        #X vai retornar uma lista vazia caso não encontre o nome do PRODUTO
        x = session.query(Pessoa).filter_by(Nome_Produto=nome_produt).all()
        
        if len(x) == 0:
            return 'PRODUTO NÃO ENCONTRADO.'
        
        #Se encontrar o PRODUTO no BD ele irá atualizar a categoria do mesmo para o valor inserido
        else:
            x[0].Categoria = nova_categ
            session.commit()
            return f'CATEGORIA DO PRODUTO {nome_produt} ATUALIZADA'
    except:
        return 'ERRO AO ATUALIZAR.'

#Deletar um produto no BD
@app.post('/deletar')
def del_prod(nome_produt):
    try:
        #Caso insira algum produto que não exista no BD ele irá retornar a msg 'PRODUTO NÂO ENCONTRADO'
        x = session.query(Pessoa).filter_by(Nome_Produto=nome_produt).all()
        if len(x) == 0:
            return 'PRODUTO NÃO ENCONTRADO.'
        
        #Se encontrar o produto no BD logo irá excluir o MESMO.
        else:
            x = session.query(Pessoa).filter_by(Nome_Produto=nome_produt).delete()
            session.commit()
            return f'PRODUTO {nome_produt} EXCLUÍDO COM SUCESSO.'
    except:
        return ' ERRO AO EXCLUIR. '

        