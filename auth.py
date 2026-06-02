def login(username, password):
    """
    用户登录功能
    """
    if username == "admin" and password == "123456":
        return True
    return False