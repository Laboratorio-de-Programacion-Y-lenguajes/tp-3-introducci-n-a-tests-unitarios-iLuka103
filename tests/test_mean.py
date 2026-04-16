"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

@pytest.mark.parametrize("lista, expected", [

    ([5], 5),
    ([-1, -10, -5, -4, -15], -7),
    ([1.5, 2.5, 2.7, 3.10, 5.11], 2.982)

])

def test_parametrizeMean(lista, expected):
    assert mean(lista) == expected

def test_listavacia():
    with pytest.raises(ValueError):
        mean([])