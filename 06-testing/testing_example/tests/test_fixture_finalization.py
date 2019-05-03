import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    import smtplib
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    print("\nSMTP SETUP")
    yield smtp_connection  # provide the fixture value
    print("\nSMTP TEARDOWN")
    smtp_connection.close()

def test_foo(smtp_connection):
    assert True 
def test_bar(smtp_connection):
    assert True 
def test_baz(smtp_connection):
    assert True 
