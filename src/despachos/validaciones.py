"""Validaciones de entrada del modulo de despachos."""

from __future__ import annotations

import re

PATRON_CODIGO = re.compile(r"^PED-\d{6}$")
PATRON_SKU = re.compile(r"^[A-Z]{3}-\d{4}$")
PESO_MAXIMO_KG = 70.0


class ErrorValidacion(Exception):
    """La entrada no cumple con el formato esperado."""


def validar_codigo(codigo: str) -> str:
    if not codigo:
        raise ErrorValidacion("el codigo no puede estar vacio")
    if not PATRON_CODIGO.match(codigo):
        raise ErrorValidacion(f"codigo con formato invalido: {codigo}")
    return codigo


def validar_sku(sku: str) -> str:
    if not PATRON_SKU.match(sku or ""):
        raise ErrorValidacion(f"sku con formato invalido: {sku}")
    return sku


def validar_cantidad(cantidad: int) -> int:
    if not isinstance(cantidad, int):
        raise ErrorValidacion("la cantidad debe ser un entero")
    if cantidad <= 0:
        raise ErrorValidacion("la cantidad debe ser mayor a cero")
    return cantidad


def validar_peso(peso_kg: float) -> float:
    if peso_kg <= 0:
        raise ErrorValidacion("el peso debe ser mayor a cero")
    if peso_kg > PESO_MAXIMO_KG:
        raise ErrorValidacion(f"el peso excede el maximo de {PESO_MAXIMO_KG} kg")
    return peso_kg


def normalizar_cliente(nombre: str) -> str:
    limpio = (nombre or "").strip()
    if len(limpio) < 3:
        raise ErrorValidacion("el nombre del cliente es demasiado corto")
    return limpio.title()
