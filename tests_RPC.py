import pytest
from SolutionDebug3 import roche_papier_ciseau

# Arrange
@pytest.mark.parametrize("j1, j2, resultat_attendu", [
    ("roche", "ciseau", "joueur 1 gagne avec roche"),
    ("roche", "papier", "joueur 2 gagne avec papier"),
    ("Roche", "Papier", "joueur 2 gagne avec papier"),
    ("allo", "", None)
])
def test_rpc(j1, j2, resultat_attendu):
    # Act
    resultat = roche_papier_ciseau(j1, j2)
    # Assert
    assert resultat == resultat_attendu