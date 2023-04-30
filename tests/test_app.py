def test_app_is_created(app):
    assert app.name == "gymanager.app"

def test_config_is_loaded(config):
    assert config["DEBUG"] is 1

def test_request_returns_404(client):
    assert client.get("/").status_code == 404