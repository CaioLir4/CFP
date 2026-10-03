from flask import Flask, render_template

app = Flask(__name__)

# --- DADOS DOS ALUNOS COM ÍNDICES DO TAF DETALHADOS ---
dados_alunos = [
    {
        "id": 1, "nome": "Amanda Lima", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 8.0, "APH": 10.0},
        "taf": {
            "Avaliativo": {"nota": 4.67, "situacao": "Apto", "corrida": "2.400m", "flexao": "32", "abdominal": "40"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 2, "nome": "Rebeca", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 9.5},
        "taf": {
            "Avaliativo": {"nota": 4.50, "situacao": "Apto", "corrida": "2.350m", "flexao": "30", "abdominal": "38"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 3, "nome": "Cassio", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {
            "Avaliativo": {"nota": 8.83, "situacao": "Apto", "corrida": "2.800m", "flexao": "45", "abdominal": "52"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 4, "nome": "Ramos", 
        "materias": {"Combate a Incêndio": 10.0, "Salvamento Terrestre": 9.5, "APH": 8.5},
        "taf": {
            "Avaliativo": {"nota": 8.87, "situacao": "Apto", "corrida": "2.850m", "flexao": "46", "abdominal": "50"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 5, "nome": "Daniel", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 9.0},
        "taf": {
            "Avaliativo": {"nota": 7.87, "situacao": "Apto", "corrida": "2.600m", "flexao": "38", "abdominal": "42"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 6, "nome": "Brito", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {
            "Avaliativo": {"nota": 8.00, "situacao": "Apto", "corrida": "2.650m", "flexao": "40", "abdominal": "44"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 7, "nome": "Lucyvan", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {
            "Avaliativo": {"nota": 7.67, "situacao": "Apto", "corrida": "2.550m", "flexao": "36", "abdominal": "40"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 8, "nome": "Kaylane", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {
            "Avaliativo": {"nota": 7.75, "situacao": "Apto", "corrida": "2.500m", "flexao": "35", "abdominal": "41"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 9, "nome": "Barros", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 8.0},
        "taf": {
            "Avaliativo": {"nota": 5.50, "situacao": "Apto", "corrida": "2.400m", "flexao": "30", "abdominal": "35"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 10, "nome": "Frederico", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {
            "Avaliativo": {"nota": 8.62, "situacao": "Apto", "corrida": "2.750m", "flexao": "44", "abdominal": "48"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 11, "nome": "Marcelo", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.5},
        "taf": {
            "Avaliativo": {"nota": 0, "situacao": "Desistiu", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 12, "nome": "Adryel", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.0, "APH": 9.0},
        "taf": {
            "Avaliativo": {"nota": 8.08, "situacao": "Apto", "corrida": "2.650m", "flexao": "39", "abdominal": "43"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 13, "nome": "Débora", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 10.0, "APH": 9.5},
        "taf": {
            "Avaliativo": {"nota": 9.87, "situacao": "Apto", "corrida": "3.000m", "flexao": "50", "abdominal": "58"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 14, "nome": "Karen", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {
            "Avaliativo": {"nota": 9.54, "situacao": "Apto", "corrida": "2.950m", "flexao": "48", "abdominal": "55"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
    },
    {
        "id": 15, "nome": "Rosário", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.5},
        "taf": {
            "Avaliativo": {"nota": 9.12, "situacao": "Apto", "corrida": "2.900m", "flexao": "46", "abdominal": "53"},
            "TAF 1": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 2": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"},
            "TAF 3": {"nota": "-", "situacao": "Pendente", "corrida": "-", "flexao": "-", "abdominal": "-"}
        }
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
    {"data": "02/10/2026", "titulo": "Instrução de Salvamento em Altura", "texto": "Levar material de descensão na próxima segunda-feira."},
    {"data": "30/09/2026", "titulo": "Aferição de Uniforme", "texto": "Ocorrerá inspeção rigorosa do uniforme 4ºA."}
]

dados_missoes = [
    {"data": "01/10/2026", "descricao": "Prevenção no Estádio Municipal - Jogo da final."},
    {"data": "28/09/2026", "descricao": "Simulado de Evacuação de Emergência em Escola Estadual."}
]

def calcular_media(materias):
    if not materias:
        return 0
    return sum(materias.values()) / len(materias.values())

@app.route('/')
def index():
    total_horas_curso = sum([h['total'] for h in dados_horas])
    horas_cumpridas_curso = sum([h['realizadas'] for h in dados_horas])
    progresso_geral = (horas_cumpridas_curso / total_horas_curso * 100) if total_horas_curso > 0 else 0

    alunos_ranking = []
    for aluno in dados_alunos:
        media = calcular_media(aluno['materias'])
        aluno_copy = aluno.copy()
        aluno_copy['media'] = round(media, 2)
        alunos_ranking.append(aluno_copy)
    
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
    return render_template('horas_aulas.html', horas=dados_horas)

if __name__ == '__main__':
    app.run(debug=True)
