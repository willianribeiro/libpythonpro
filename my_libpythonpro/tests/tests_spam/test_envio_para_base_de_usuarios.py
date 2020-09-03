from my_libpythonpro.spam.main import EnviadorDeSpam
from my_libpythonpro.spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'remetente@email.com.br',
        'Assunto do e-mail',
        'Corpo do e-mail'
    )
