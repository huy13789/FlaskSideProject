from models import user

class Account:
    def __init__(self, username, password, user: user.User):
        self.username = username
        self.password = password  # Trong thực tế nên mã hóa mật khẩu!
        self.user = user  # Tham chiếu tới đối tượng Use
