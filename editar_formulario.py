from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Função para recuperar dados do banco de dados
def recuperar_dados_do_banco():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1253',
            database='tcc'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT frase_inicial, frase_sec, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3, img_logo, img_pr1, img_pr2, img_pr3, img_bg, img_sec FROM formulario")
        dados = cursor.fetchone()  # Supondo que você deseja apenas um registro
        connection.close()
        return dados
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o banco de dados: {err}")
        return None

# Rota para renderizar o HTML com as informações do banco de dados
@app.route('/visualizar_informacoes')
def visualizar_informacoes():
    dados = recuperar_dados_do_banco()
    
    if dados:
        return render_template('index.html', dados=dados)
    else:
        return "Dados não encontrados."

if __name__ == '__main__':
    app.run()