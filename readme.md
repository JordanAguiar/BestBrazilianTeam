# 🏆 Análise dos Campeões do Brasileirão (2003–2025)

## 📌 Descrição do Projeto
Este projeto realiza uma **análise exploratória de dados (EDA)** sobre as **últimas 22 temporadas do Campeonato Brasileiro (Brasileirão)**, com foco em entender:

- Quem são os maiores campeões do período
- Quais padrões estatísticos os campeões apresentam
- Quais características mais se repetem em campanhas vencedoras

A análise utiliza dados históricos de desempenho das equipes, como pontos, vitórias, gols marcados e gols sofridos.

---

## 🎯 Objetivos
- Identificar os **maiores campeões do Brasileirão** desde 2003  
- Analisar padrões de desempenho dos times campeões  
- Avaliar métricas ofensivas e defensivas das campanhas vencedoras  
- Descobrir campanhas historicamente mais dominantes  

---

## 🗂️ Base de Dados
O dataset contém **470 registros** (temporadas completas de 2003 a 2025) e as seguintes colunas principais:

- `season` – Temporada
- `place` – Colocação final
- `team` – Time
- `points` – Pontos
- `played` – Jogos disputados
- `won`, `draw`, `loss` – Vitórias, empates e derrotas
- `goals` – Gols marcados
- `goals_taken` – Gols sofridos

### 🔢 Métricas Criadas
- `percentual_vitorias`
- `media_gols_marcados`
- `media_gols_sofridos`
- `goals_diff`

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Pandas** – análise e manipulação de dados

---

## 📊 Análises Realizadas

### 🔹 Identificação dos campeões
- Filtro das equipes campeãs (`place == 1`)
- Análise da frequência de títulos por clube

### 🔹 Maiores campeões (2003–2025)
- Corinthians, Flamengo e Palmeiras lideram o período com **4 títulos cada**

### 🔹 Estatísticas médias dos campeões
- Média de **~79 pontos** por título
- Média de **23 vitórias por temporada**
- Média de **~69 gols marcados**
- Campanhas campeãs costumam ter **menos de 1 gol sofrido por jogo**

### 🔹 Campanha mais dominante
- **Flamengo 2019**
  - 90 pontos
  - 73,6% de aproveitamento
  - 2,26 gols marcados por jogo

### 🔹 Melhor defesa entre os campeões
- **São Paulo 2007**
  - Apenas **0,5 gol sofrido por jogo**

---

## 📈 Principais Insights
- Times campeões apresentam **alto percentual de vitórias** e **defesas sólidas**
- Não é necessário ser o melhor ataque para ser campeão, mas sofrer poucos gols é recorrente
- Campanhas históricas combinam **eficiência ofensiva e consistência defensiva**

---

## ▶️ Como Executar o Projeto
1. Clone o repositório:
```bash
git clone https://github.com/JordanAguiar/BestBrazilianTeam.git
```
2. Instale as dependências:

```bash
pip install pandas
```

3. Execute o script ou notebook com o dataset CSV.
