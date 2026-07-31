import pytest

from despachos.tarifas import (
    Envio,
    ZonaDesconocida,
    aplica_envio_gratis,
    calcular,
    costo_peso,
    factor_zona,
)


def test_factor_zona_conocida():
    assert factor_zona("lima_metropolitana") == 1.00


def test_factor_zona_desconocida():
    with pytest.raises(ZonaDesconocida):
        factor_zona("antartida")


def test_costo_peso_positivo():
    assert costo_peso(5) == 9.00


def test_costo_peso_cero():
    assert costo_peso(0) == 0.0


def test_calculo_zona_cercana():
    envio = Envio(zona="lima_metropolitana", peso_kg=2, valor_declarado=100.0)
    assert calcular(envio) == 16.10


def test_envio_gratis_por_valor():
    envio = Envio(zona="lima_metropolitana", peso_kg=2, valor_declarado=300.0)
    assert aplica_envio_gratis(envio) is True
    assert calcular(envio) == 0.0


def test_sin_envio_gratis_en_zona_alejada():
    envio = Envio(zona="selva", peso_kg=2, valor_declarado=300.0)
    assert aplica_envio_gratis(envio) is False


def test_sin_envio_gratis_si_es_urgente():
    envio = Envio(zona="lima_metropolitana", peso_kg=2, valor_declarado=300.0, urgente=True)
    assert aplica_envio_gratis(envio) is False
