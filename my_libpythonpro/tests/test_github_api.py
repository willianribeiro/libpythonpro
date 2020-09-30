from unittest.mock import Mock

import pytest

from my_libpythonpro import github_api


@pytest.fixture()
def avatar_url(mocker):
    # mock api
    url = 'https://avatars1.githubusercontent.com/u/3102551?v=4'
    json_mock = {
        'login': 'willianribeiro',
        'id': 3102551,
        'node_id': 'MDQ6VXNlcjMxMDI1NTE=',
        'avatar_url': url
    }
    response_mock = Mock()
    response_mock.json.return_value = json_mock
    get_mock = mocker.patch('my_libpythonpro.github_api.requests.get')
    get_mock.return_value = response_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('willianribeiro')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    expected_url = 'https://avatars3.githubusercontent.com/u/3457115?v=4'
    assert expected_url == url
