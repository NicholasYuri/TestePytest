from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from calculadora import soma


class TesteCalculadora():
    
    def test_soma_positivos():
        resultado = soma(5, 5)
        assert resultado == 10

    def test_soma_negativos():
        resultado = soma(-5, -5)
        assert resultado == -10

    def test_soma_zero():
        resultado = soma(5, 0)
        assert resultado == 5

def executar_teste():
    resultados = []

    try:
        TesteCalculadora.test_soma_positivos
        resultados.append("test_soma_positivo: OK")
    except AssertionError:
        resultados.append("test_soma_positivo: ERRO")

    try:
        TesteCalculadora.test_soma_negativos
        resultados.append("test_soma_negativos: OK")
    except AssertionError:
        resultados.append("test_soma_negativos: ERRO")

    try:
        TesteCalculadora.test_soma_zero
        resultados.append("test_soma_zero: OK")
    except AssertionError:
        resultados.append("test_soma_zero: ERRO")

    return resultados

def gerar_relatorio(resultados):
    relatorio = canvas.Canvas("Relatório.pdf", pagesize= A4) # canvas cria um pagina em branco
    relatorio.drawString(200, 750, "RELATORIO TESTE CALCULADORA") # texto do relatório e seus eixo x, y

    y = 720
    for linha in resultados:
        relatorio.drawString(100, y, linha)
        y -= 20


    relatorio.save()

    print("Relatório gerado com sucesso!")
    
if __name__ == '__main__':
    resultados = executar_teste()
    gerar_relatorio(resultados)




