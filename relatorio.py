import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet

arquivos = {
    "10 usuários": "results_10_stats.csv",
    "50 usuários": "results_50_stats.csv",
    "100 usuários": "results_100_stats.csv"
}

#Metricas
dados = []

for carga, arquivo in arquivos.items():

    df = pd.read_csv(arquivo)

    linha = df[df["Name"] == "Aggregated"].iloc[0]

    dados.append({
        "Carga": carga,
        "Tempo Médio": linha["Average Response Time"],
        "P90": linha["90%"],
        "P95": linha["95%"],
        "Req/s": linha["Requests/s"]
    })

resultado = pd.DataFrame(dados)

#Grafico
plt.figure()

plt.bar(
    resultado["Carga"],
    resultado["Tempo Médio"]
)

plt.title("Tempo Médio de Resposta")

plt.ylabel("ms")

plt.tight_layout()

plt.savefig("tempo_medio.png")

plt.close()

#Grafico P95
plt.figure()

plt.bar(
    resultado["Carga"],
    resultado["P95"]
)

plt.title("Percentil 95")

plt.ylabel("ms")

plt.tight_layout()

plt.savefig("p95.png")

plt.close()

#Grafico P90
plt.figure()

plt.bar(
    resultado["Carga"],
    resultado["P90"]
)

plt.title("Percentil 90")

plt.ylabel("ms")

plt.tight_layout()

plt.savefig("p90.png")

plt.close()

#Grafico Throughput
plt.figure()

plt.bar(
    resultado["Carga"],
    resultado["Req/s"]
)

plt.title("Throughput")

plt.ylabel("Req/s")

plt.tight_layout()

plt.savefig("throughput.png")

plt.close()

#Pdf
doc = SimpleDocTemplate(
    "relatorio.pdf"
)

styles = getSampleStyleSheet()

conteudo = []

#Titulo
conteudo.append(
    Paragraph(
        "Relatório de Performance - DummyJSON",
        styles["Title"]
    )
)

conteudo.append(
    Spacer(1, 12)
)

conteudo.append(
    Paragraph(
        "Este relatório apresenta os resultados dos testes de performance realizados na API DummyJSON utilizando a ferramenta Locust.",
        styles["BodyText"]
    )
)

conteudo.append(
    Spacer(1, 12)
)

#Tabela Textual
for _, linha in resultado.iterrows():

    texto = (
    f"Carga: {linha['Carga']}<br/>"
    f"Tempo Médio: {linha['Tempo Médio']} ms<br/>"
    f"P90: {linha['P90']} ms<br/>"
    f"P95: {linha['P95']} ms<br/>"
    f"Throughput: {linha['Req/s']} req/s<br/><br/>"
)

    conteudo.append(
        Paragraph(
            texto,
            styles["BodyText"]
        )
    )

#Inserindo Grafico
conteudo.append(PageBreak())

conteudo.append(
    Paragraph(
        "Gráficos",
        styles["Heading1"]
    )
)

conteudo.append(
    Image(
        "tempo_medio.png",
        width=400,
        height=250
    )
)

conteudo.append(
    Image(
        "p95.png",
        width=400,
        height=250
    )
)

conteudo.append(
    Image(
        "p90.png",
        width=400,
        height=250
    )
)

conteudo.append(
    Image(
        "throughput.png",
        width=400,
        height=250
    )
)

#Finil Pdf
doc.build(conteudo)

print("Relatório gerado com sucesso!")
