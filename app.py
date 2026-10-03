from flask import Flask, render_template

app = Flask(__name__)

# --- DADOS DOS ALUNOS (Extraídos do TAF de Diagnóstico - CFP BM 2026) ---
dados_alunos = [
    {
        "id": 1, "nome": "Amanda Lima", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 8.0, "APH": 10.0},
        "taf": {"Avaliativo": "Nota: 4,67 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 2, "nome": "Rebeca", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 4,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 3, "nome": "Cassio", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 8,83 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 4, "nome": "Ramos", 
        "materias": {"Combate a Incêndio": 10.0, "Salvamento Terrestre": 9.5, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 5, "nome": "Daniel", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 7,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 6, "nome": "Brito", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,00 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 7, "nome": "Lucyvan", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,67 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 8, "nome": "Kaylane", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 7,75 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 9, "nome": "Barros", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 5,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 10, "nome": "Frederico", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,62 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 11, "nome": "Marcelo", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.5},
        "taf": {"Avaliativo": "Desistiu", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 12, "nome": "Adryel", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 8,08 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 13, "nome": "Débora", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 10.0, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 14, "nome": "Karen", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,54 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 15, "nome": "Rosário", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 8.5, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,12 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 16, "nome": "Flávio", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,12 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 17, "nome": "Garcia", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,58 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 18, "nome": "Dara Nicole", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.5, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 5,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 19, "nome": "Queiroz", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 8,67 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 20, "nome": "Bezerra", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,04 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 21, "nome": "Eduardo", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 22, "nome": "Larissa", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 23, "nome": "Kelly", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.0, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,29 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 24, "nome": "Gabriel", 
        "materias": {"Combate a Incêndio": 6.5, "Salvamento Terrestre": 6.0, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 5,54 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 25, "nome": "Soares", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 26, "nome": "Lanna Melissa", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 7,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 27, "nome": "Raisa", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.5, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 5,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 28, "nome": "Peterson", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 9.5, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 29, "nome": "Machado", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.5, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 30, "nome": "Heloisa", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 8,91 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 31, "nome": "Emilio", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,45 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 32, "nome": "Maciel", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 33, "nome": "Robison", 
        "materias": {"Combate a Incêndio": 6.5, "Salvamento Terrestre": 6.0, "APH": 6.5},
        "taf": {"Avaliativo": "Nota: 6,33 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 34, "nome": "Silveira", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.0, "APH": 7.0},
        "taf": {"Avaliativo": "Nota: 7,00 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 35, "nome": "Marcos Paulo", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,08 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 36, "nome": "Alexandre", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,29 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 37, "nome": "Nikson", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 7.0},
        "taf": {"Avaliativo": "Nota: 6,91 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 38, "nome": "De Miranda", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 5,00 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 39, "nome": "Rayla", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,62 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 40, "nome": "Antônio", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,33 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 41, "nome": "Naiana", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 6,12 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 42, "nome": "Calandrine", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,29 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 43, "nome": "Carlos Maia", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,20 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 44, "nome": "Waléria", 
        "materias": {"Combate a Incêndio": 4.0, "Salvamento Terrestre": 4.0, "APH": 4.5},
        "taf": {"Avaliativo": "Nota: 2,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 45, "nome": "Laila", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,70 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 46, "nome": "Cleyton", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,33 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 47, "nome": "Barreto", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,83 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 48, "nome": "Rafaelly", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,54 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 49, "nome": "Paiva", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.5, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 6,70 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 50, "nome": "Tarciso", 
        "materias": {"Combate a Incêndio": 6.5, "Salvamento Terrestre": 7.0, "APH": 6.5},
        "taf": {"Avaliativo": "Nota: 6,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 51, "nome": "Correa", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,00 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 52, "nome": "Viana", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,04 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 53, "nome": "Araújo", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,45 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 54, "nome": "Caio Gomes", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,33 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 55, "nome": "Isabela", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 8.0, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,87 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 56, "nome": "João Pedro", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,08 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 57, "nome": "Clara", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,08 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 58, "nome": "Rafael", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,08 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 59, "nome": "Laranjeira", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.5, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 60, "nome": "Thayane", 
        "materias": {"Combate a Incêndio": 5.5, "Salvamento Terrestre": 6.0, "APH": 5.5},
        "taf": {"Avaliativo": "Nota: 5,37 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 61, "nome": "Thainar", 
        "materias": {"Combate a Incêndio": 4.5, "Salvamento Terrestre": 4.5, "APH": 4.5},
        "taf": {"Avaliativo": "Nota: 4,16 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 62, "nome": "Visgueira", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 9.5, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 63, "nome": "Rodrigo", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,95 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 64, "nome": "Pontes", 
        "materias": {"Combate a Incêndio": 9.5, "Salvamento Terrestre": 9.5, "APH": 9.5},
        "taf": {"Avaliativo": "Nota: 9,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 65, "nome": "Amanda", 
        "materias": {"Combate a Incêndio": 6.5, "Salvamento Terrestre": 6.5, "APH": 6.5},
        "taf": {"Avaliativo": "Nota: 6,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 66, "nome": "De Sousa", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.0, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 8,91 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 67, "nome": "Thiago", 
        "materias": {"Combate a Incêndio": 7.5, "Salvamento Terrestre": 7.5, "APH": 7.5},
        "taf": {"Avaliativo": "Nota: 7,29 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 68, "nome": "De Mendonça", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.5, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,50 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 69, "nome": "Wesley", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 8.5, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,54 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 70, "nome": "Cristhian", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 7,95 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 71, "nome": "Raul", 
        "materias": {"Combate a Incêndio": 7.0, "Salvamento Terrestre": 7.0, "APH": 7.0},
        "taf": {"Avaliativo": "Nota: 6,91 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 72, "nome": "Yuri", 
        "materias": {"Combate a Incêndio": 9.0, "Salvamento Terrestre": 9.5, "APH": 9.0},
        "taf": {"Avaliativo": "Nota: 9,16 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 73, "nome": "Ivan", 
        "materias": {"Combate a Incêndio": 6.5, "Salvamento Terrestre": 6.5, "APH": 6.5},
        "taf": {"Avaliativo": "Nota: 6,41 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 74, "nome": "Jaila", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.0},
        "taf": {"Avaliativo": "ADM", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 75, "nome": "Sampaio", 
        "materias": {"Combate a Incêndio": 6.0, "Salvamento Terrestre": 6.0, "APH": 6.0},
        "taf": {"Avaliativo": "Nota: 6,16 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 76, "nome": "Beatriz", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.5, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,25 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 77, "nome": "Felipe Dias", 
        "materias": {"Combate a Incêndio": 8.0, "Salvamento Terrestre": 8.0, "APH": 8.0},
        "taf": {"Avaliativo": "Nota: 8,16 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
    },
    {
        "id": 78, "nome": "Cunha", 
        "materias": {"Combate a Incêndio": 8.5, "Salvamento Terrestre": 9.0, "APH": 8.5},
        "taf": {"Avaliativo": "Nota: 8,67 (Apto)", "TAF 1": "Pendente", "TAF 2": "Pendente", "TAF 3": "Pendente"}
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
