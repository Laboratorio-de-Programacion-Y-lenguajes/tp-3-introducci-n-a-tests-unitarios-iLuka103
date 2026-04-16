"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)

@pytest.mark.parametrize ("a, expected",[

    (0, 0.0),
    (3, 1.7320508075688772),
    (-3, 0)

])

def test_parametrizeSqrt(a, expected):
    if (a < 0):
        with pytest.raises(ValueError):
            sqrt(a)
    else: 
        assert sqrt(a) == expected