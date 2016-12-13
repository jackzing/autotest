called = []
def setup_module(module):
     module.called[:] = ["init"]

def test_init_base():
     from app.base.config import Config
     config = Config()
     config.initBase()
     #print(config.conf("socks.type", "http"))
     assert "socks5" in config.conf("socks.type", "http")
