import pytest

from despachos.pedidos import (
    Estado,
    Linea,
    Pedido,
    TransicionInvalida,
    agrupar_por_cliente,
    pedidos_abiertos,
)


def nuevo_pedido() -> Pedido:
    pedido = Pedido(codigo="PED-000101", cliente="Comercial Andina")
    pedido.agregar_linea(Linea(sku="ABC-1001", cantidad=2, precio_unitario=35.50))
    pedido.agregar_linea(Linea(sku="ABC-1002", cantidad=1, precio_unitario=12.00))
    return pedido


def test_subtotal_de_linea():
    assert Linea(sku="ABC-1001", cantidad=3, precio_unitario=10.10).subtotal() == 30.30


def test_total_del_pedido():
    assert nuevo_pedido().total() == 83.00


def test_unidades_del_pedido():
    assert nuevo_pedido().unidades() == 3


def test_transicion_valida():
    pedido = nuevo_pedido()
    pedido.cambiar_estado(Estado.PREPARADO)
    assert pedido.estado is Estado.PREPARADO


def test_transicion_invalida():
    pedido = nuevo_pedido()
    with pytest.raises(TransicionInvalida):
        pedido.cambiar_estado(Estado.ENTREGADO)


def test_no_se_agregan_lineas_a_pedido_preparado():
    pedido = nuevo_pedido()
    pedido.cambiar_estado(Estado.PREPARADO)
    with pytest.raises(TransicionInvalida):
        pedido.agregar_linea(Linea(sku="ABC-1003", cantidad=1, precio_unitario=5.00))


def test_pedido_entregado_esta_cerrado():
    pedido = nuevo_pedido()
    pedido.cambiar_estado(Estado.PREPARADO)
    pedido.cambiar_estado(Estado.DESPACHADO)
    pedido.cambiar_estado(Estado.ENTREGADO)
    assert pedido.esta_cerrado() is True


def test_agrupar_por_cliente():
    a = Pedido(codigo="PED-000101", cliente="Comercial Andina")
    b = Pedido(codigo="PED-000102", cliente="Comercial Andina")
    c = Pedido(codigo="PED-000103", cliente="Distribuidora Sur")
    agrupados = agrupar_por_cliente([a, b, c])
    assert len(agrupados["Comercial Andina"]) == 2
    assert len(agrupados["Distribuidora Sur"]) == 1


def test_pedidos_abiertos():
    abierto = Pedido(codigo="PED-000104", cliente="Comercial Andina")
    cerrado = Pedido(codigo="PED-000105", cliente="Comercial Andina")
    cerrado.cambiar_estado(Estado.ANULADO)
    assert pedidos_abiertos([abierto, cerrado]) == [abierto]
