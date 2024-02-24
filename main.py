import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# URL da API do IBGE
url = "https://servicodados.ibge.gov.br/api/v3/agregados/1209/periodos/1991|2000|2010|2022/variaveis/1000606?localidades=N1[all]&classificacao=58[1143,1144,3299,3301"

# Fazendo a requisição à API
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrai os dados do JSON da resposta
    data = response.json()

    # Processa os dados conforme necessário
    # (Assumindo que os dados estão no formato esperado)

    # Exemplo: Obtendo os valores de cada variável
    titulo = data[0]["variavel"]
    grp1 = data[0]["resultados"][0]["series"][0]["serie"]
    n_grp1 = data[0]["resultados"][0]["classificacoes"][0]["categoria"]["1143"]

    grp2 = data[0]["resultados"][1]["series"][0]["serie"]
    n_grp2 = data[0]["resultados"][1]["classificacoes"][0]["categoria"]["1144"]

    # Exemplo: Criando um gráfico de barras
    anos = list(grp1.keys())
    var1 = list(grp1.values())
    var2 = list(grp2.values())

    def porcentagem_formatter(x, _):
        return f"{x:.0%}"

    plt.plot(anos, var1, label=f"{n_grp1}")
    plt.plot(anos, var2, label=f"{n_grp2}", linestyle='dotted',  alpha=0.7)

    plt.xlabel("Ano")
    plt.ylabel("Valor (%)")

    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0%}"))

    plt.title(f"{titulo}")
    plt.legend()
    plt.show()

else:
    print(f"Erro ao acessar a API. Código de status: {response.status_code}")
