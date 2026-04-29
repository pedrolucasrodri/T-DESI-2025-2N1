from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 2. A Fonte de Dados (Simulação de Banco de Dados)
    musicJ = [
        {
            'titulo': 'Indesculpavel',
            'artista': 'Fhop Music',
            'estilo': 'Rock',
            'fileName': 'indesculpavel.mp3',
            'duracao': '04:52'
        },
        {
            'titulo': 'Raise Hallelujah',
            'artista': 'Bethelm Music',
            'estilo': 'Worship',
            'fileName': 'raise.mp3',
            'duracao': '07:50'
        },
        {
            'titulo': 'Praise You Anywhere',
            'artista': 'Brandon Lake',
            'estilo': 'POP',
            'fileName': 'praise_any.mp3', 
            'duracao': '03:35'
        }
    ]
    
    # TESTE DE RESILIÊNCIA: 
    # Para testar o estado vazio, basta descomentar a linha abaixo antes de recarregar a página:
    # musicJ = []

    # 1. O Back-end (Passando a lista como injeção de contexto)
    return render_template('index.html', musicJ=musicJ)

if __name__ == '__main__':
    app.run(debug=True)