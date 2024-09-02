from lambda_handler.lambda_handler import lambda_handler

def test_hello():
    
    assert lambda_handler(None, None) == "hoge"
