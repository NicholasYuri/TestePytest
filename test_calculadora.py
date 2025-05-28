from calculadora import soma

def test_soma_positivos():
    resultado = soma(5, 5)
    assert resultado == 10

def test_soma_negativos():
    resultado = soma(-5, -5)
    assert resultado == -10

def test_soma_zero():
    resultado = soma(5, 0)
    assert resultado == 5

# Adicionar o teste de soma negativos
# Adicionar o teste de soma com 0 
# resultado do teste ser salvo .PDF

# Entregar dia 05/06