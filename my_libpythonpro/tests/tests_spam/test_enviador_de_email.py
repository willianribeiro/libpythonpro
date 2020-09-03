import pytest

from my_libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['remetente_1@email.com.br', 'remetente_2@email.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'destinatario@email.com.br',
        'Assunto do e-mail',
        'Corpo do e-mail'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'remetente']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'destinatario@email.com.br',
            'Assunto do e-mail',
            'Corpo do e-mail'
        )
