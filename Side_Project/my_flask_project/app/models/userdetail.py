from models import user

class UserDetail:
    def __init__(self, fullname, age, user: user.User):
        self.fullname = fullname
        self.age = age  # Trong thực tế nên mã hóa mật khẩu!
        self.user = user  # Tham chiếu tới đối tượng Use
