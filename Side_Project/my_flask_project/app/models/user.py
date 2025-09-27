class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password # Trong thực tế nên mã hóa mật khẩu!
        self.email = email
