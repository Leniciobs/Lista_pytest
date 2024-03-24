# validador_emails.py
import re

def validar_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    return False

# test_validador_emails.py
import pytest
from validar_email import validar_email

def test_validar_email():
    assert validar_email('example@example.com') == True
    assert validar_email('example@example.co.uk') == True
    assert validar_email('example123@example.co') == True

def test_invalidar_email():
    assert validar_email('example@example') == False
    assert validar_email('exampleexample.com') == False
    assert validar_email('example123.com') == False
