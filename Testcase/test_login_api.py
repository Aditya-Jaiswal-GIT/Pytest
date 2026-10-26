from Method.LoginPage import LoginPage 

class TestLogin(LoginPage):
    def test_login_with_valid_credential(self):
        flag = super().valid_credential()
        assert flag is True
