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

@app.route('/processar_formulario', methods=['GET', 'POST'])
def processar_formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        conn = conectar_bd()

        if conn:
            cursor = conn.cursor()

            insert_query = "INSERT INTO tabela_exemplo (nome, email) VALUES (%s, %s)"
            cursor.execute(insert_query, (nome, email))

            conn.commit()
            conn.close()

            return "Dados inseridos com sucesso!"

        return "Erro no envio do formulário."
    else:
        # Retornar um formulário HTML para preenchimento
        return render_template('formulario.html')

if __name__ == '__main__':
    app.run()
