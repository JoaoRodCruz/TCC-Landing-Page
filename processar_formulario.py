from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1253',
            database='tcc'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o banco de dados: {err}")
        return None

@app.route('/tcc', methods=['GET', 'POST'])
def processar_formulario():
    if request.method == 'POST':
        frase_inicial = request.form['frase-inicial']
        frase_secundaria = request.form['frase-secundaria']
        sobre_empresa = request.form['sobre_empresa']
        sobre_produto = request.form['sobre_produto']
        produto1 = request.form['produto1']
        preco1 = request.form['preco1']
        produto2 = request.form['produto2']
        preco2 = request.form['preco2']
        produto3 = request.form['produto3']
        preco3 = request.form['preco3']
        logo = request.form['logo']
        imagem_produto1 = request.form['imagem-produto1']
        imagem_produto2 = request.form['imagem-produto2']
        imagem_produto3 = request.form['imagem-produto3']
        imagem_bg = request.form['imagem-bg']
        imagem_sec = request.form['imagem-sec']


        conn = conectar_bd()

        if conn:
            cursor = conn.cursor()

            insert_query = "INSERT INTO formulario (frase_inicial, frase_sec, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3, img_logo, img_pr1, img_pr2, img_pr3, img_bg, img_sec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (frase_inicial, frase_secundaria, sobre_empresa, sobre_produto, produto1, preco1, produto2, preco2, produto3, preco3, logo, imagem_produto1, imagem_produto2, imagem_produto3, imagem_bg, imagem_sec))

            conn.commit()
            conn.close()

            return "Dados inseridos com sucesso!"

        return "Erro no envio do formulário."
    else:
        # Retornar um formulário HTML para preenchimento
        return render_template('forms.html')

if __name__ == '__main__':
    app.run()
