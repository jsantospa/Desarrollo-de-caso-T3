import pytest
from gestion_academica import (
    registrar_estudiante,
    matricular,
    calcular_promedio,
    obtener_estado,
)


def test_registrar_estudiante():
    assert registrar_estudiante("E001", "Ana Perez") is True


def test_estudiante_duplicado():
    registrar_estudiante("E002", "Luis Ramos")
    with pytest.raises(ValueError):
        registrar_estudiante("E002", "Luis Ramos")


def test_matricular():
    registrar_estudiante("E003", "Rosa Diaz")
    assert matricular("E003", "Matematica") == ["Matematica"]


def test_matricular_no_registrado():
    with pytest.raises(KeyError):
        matricular("E999", "Fisica")


def test_promedio():
    assert calcular_promedio([14, 16, 12]) == 14.0


def test_nota_invalida():
    with pytest.raises(ValueError):
        calcular_promedio([25, 10])


def test_estado():
    assert obtener_estado(14) == "Aprobado"
    assert obtener_estado(10) == "Desaprobado"