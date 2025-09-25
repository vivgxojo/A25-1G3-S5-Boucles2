import pytest
from mots_passes import verifier_mot_de_passe  # adapter au nom de ton fichier

def test_trop_court():
    # Arrange
    mdp = "abc"
    # Act
    result = verifier_mot_de_passe(mdp)
    # Assert
    assert result is False

def test_sans_majuscule():
    mdp = "abcdefg1"
    result = verifier_mot_de_passe(mdp)
    assert result is False

def test_sans_chiffre():
    mdp = "Abcdefgh"
    result = verifier_mot_de_passe(mdp)
    assert result is False

def test_mot_de_passe_valide():
    mdp = "Abcdefg1"
    result = verifier_mot_de_passe(mdp)
    assert result is True
