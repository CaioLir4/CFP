from flask import Flask, render_template

app = Flask(__name__)

# --- DADOS FICTÍCIOS (Estáticos) ---
dados_alunos = [
    {"nome": "Sd Al BM Silva", "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 8.0, "APH": 10.0}},
    {"nome": "Sd Al BM Costa", "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 9.5}},
    {"nome": "Sd Al BM Oliveira", "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.5, "APH": 9.0}}
]

dados_financeiro = {
    "saldo_atual": 2550.00,
    "gastos": [
        {"missao": "Compra de materiais de asseio", "valor": 300.00},
        {"missao": "Bandeira do Pelotão", "valor": 150.00},
        {"missao": "Manutenção de Equipamentos", "valor": 450.00}
    ]
}

dados_horas = [
    {"materia": "Combate a Incêndio", "realizadas": 40, "total": 120},
    {"materia": "Salvamento Terrestre", "realizadas": 20, "total": 80},
    {"materia": "Atendimento Pré-Hospitalar (APH)", "realizadas": 60, "total": 100},
    {"materia": "Legislação BM", "realizadas": 30, "total": 40}
]

# --- ROTAS ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alunos')
def alunos():
    return render_template('alunos.html', alunos=dados_alunos)

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html', financeiro=dados_financeiro)

@app.route('/horas')
def horas_aulas():
    return render_template('horas_aulas.html', horas=dados_horas)

if __name__ == '__main__':
    app.run(debug=True)
