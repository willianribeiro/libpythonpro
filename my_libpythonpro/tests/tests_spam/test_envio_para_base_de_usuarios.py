from unittest.mock import Mock

import pytest

from my_libpythonpro.spam.main import EnviadorDeSpam
from my_libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Usuario Um', email='usuario_um@email.com.br'),
            Usuario(nome='Usuario Dois', email='usuario_dois@email.com.br')
        ],
        [
            Usuario(nome='Usuario Um', email='usuario_um@email.com.br'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente@email.com.br',
        'Assunto do e-mail',
        'Corpo do e-mail'
    )
    assert len(sessao.listar()) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Usuario Um', email='usuario_um@email.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente@email.com.br',
        'Assunto do e-mail',
        'Corpo do e-mail'
    )
    enviador.enviar.assert_called_once_with(
        'remetente@email.com.br',
        'usuario_um@email.com.br',
        'Assunto do e-mail',
        'Corpo do e-mail'
    )
