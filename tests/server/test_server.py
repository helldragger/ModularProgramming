import src.server.server as server


def test_start():
    result = server.on_init()
    assert result is None


def test_close():
    result = server.on_close()
    assert result is None
