# %%
import pandas as pd 

# %% [markdown]
# * Carregamento dos Dados (últimas 22 temporadas - Brasileirão)

# %%
df = pd.read_csv(r"BestBrazilianTeam\data\brasileirao.csv")

df

# %%
df["percentual_vitorias"] = df["won"] / df["played"]*100
df["media_gols_marcados"] = df["goals"] / df["played"]
df["media_gols_sofridos"] = df["goals_taken"] / df["played"]

#Visualizar dados
df

# %% [markdown]
# * Analisando os mariores campeoes da historia... quais as caracteristicas dos campeoes? Há um padrao? Quem é o maior vencedor dos ultimos anos?

# %%
# Filtrar dataset com os campeoes de cada ano
filtro_campeoes = df["place"] == 1

# aplicar filtro ao dataset
df_campeoes = df[filtro_campeoes]

#Visualizando dados
df_campeoes

# %%
# Descobrindo o maior campeão dos ultimos anos
df_campeoes["team"].mode()

# %%
df_campeoes.groupby("team")["place"].count().sort_values(ascending=False)

# %%
# Analisando estatisticas e padroes dos campeões

df_campeoes.describe()

# %%
# Qual foi o time com maior percentual de vitorias
indice_maior_campeao = df_campeoes["percentual_vitorias"].idxmax()

df_campeoes.loc[indice_maior_campeao]

# %%
# Qual foi o time com a melhor defesa
indice_maior_defesa = df_campeoes["media_gols_sofridos"].idxmin()

df_campeoes.loc[indice_maior_defesa]


