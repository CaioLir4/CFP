from flask import Flask, render_template

app = Flask(__name__)

# --- DADOS FICTÍCIOS (Estáticos) ---
dados_alunos = [
    {
        "id": 1, 
        "nome": "Sd Al BM Silva", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 8.0, "APH": 10.0},
        "taf": {"Avaliativo": "Apto (9.5)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 2, 
        "nome": "Sd Al BM Costa", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 9.5},
        "taf": {"Avaliativo": "Apto (8.5)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 3, 
        "nome": "Sd Al BM Oliveira", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {"Avaliativo": "Apto (8.0)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 4, 
        "nome": "Sd Al BM Santos", 
        "materias": {"Combate a Incêndio": 10.0, "Salvamento Terrestre": 9.5, "APH": 8.5},
        "taf": {"Avaliativo": "Apto (9.8)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    }
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

dados_avisos = [
    {"data": "02/10/2026", "titulo": "Instrução de Salvamento em Altura", "texto": "Levar material de descensão (freio 8, mosquetões e cordeletes) na próxima segunda-feira."},
    {"data": "30/09/2026", "titulo": "Aferição de Uniforme", "texto": "Ocorrerá inspeção rigorosa do uniforme 4ºA."}
]

dados_missoes = [
    {"data": "01/10/2026", "descricao": "Prevenção no Estádio Municipal - Jogo da final."},
    {"data": "28/09/2026", "descricao": "Simulado de Evacuação de Emergência em Escola Estadual."}
]

# --- FUNÇÕES AUXILIARES ---
def calcular_media(materias):
    if not materias:
        return 0
    return sum(materias.values()) / len(materias.values())

# --- ROTAS ---
@app.route('/')
def index():
    # Cálculo do progresso geral do curso
    total_horas_curso = sum([h['total'] for h in dados_horas])
    horas_cumpridas_curso = sum([h['realizadas'] for h in dados_horas])
    progresso_geral = (horas_cumpridas_curso / total_horas_curso * 100) if total_horas_curso > 0 else 0

    # Prepara o ranking de alunos
    alunos_ranking = []
    for aluno in dados_alunos:
        media = calcular_media(aluno['materias'])
        aluno_copy = aluno.copy()
        aluno_copy['media'] = round(media, 2)
        alunos_ranking.append(aluno_copy)
    
    # Ordena do maior para o menor
    alunos_ranking.sort(key=lambda x: x['media'], reverse=True)

    return render_template('index.html', 
                           progresso=progresso_geral,
                           horas=dados_horas,
                           ranking=alunos_ranking,
                           avisos=dados_avisos,
                           missoes=dados_missoes)

@app.route('/aluno/<int:aluno_id>')
def perfil_aluno(aluno_id):
    aluno = next((a for a in dados_alunos if a['id'] == aluno_id), None)
    if aluno:
        media = round(calcular_media(aluno['materias']), 2)
        return render_template('aluno_perfil.html', aluno=aluno, media=media)
    return "Aluno não encontrado", 404

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html', financeiro=dados_financeiro)

@app.route('/horas')
def horas_aulas():
    # Mantendo a rota antiga para quem quiser ver as horas isoladas
    return render_template('horas_aulas.html', horas=dados_horas)

if __name__ == '__main__':
    app.run(debug=True)
