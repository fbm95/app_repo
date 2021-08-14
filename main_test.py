import pytest

import main


@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()


def test_greetings(client):
    r = client.get("/greetings")

    assert r.data.decode() == "HHello!"
    assert r.status_code == 200
