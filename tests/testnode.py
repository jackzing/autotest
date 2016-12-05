called = []
def setup_module(module):
     module.called[:] = ["init"]

def test_equal():
    result = 3 + 2
    assert result == 5

def test_send_email():
    from app.base.email import send_email
    print(send_email())

