from typing import Optional
import os

def verify_password(username: str, password: str) -> bool:
    """
    验证用户密码是否正确
    
    Args:
        username: 用户名
        password: 密码
    
    Returns:
        bool: 验证成功返回 True，否则返回 False
    """
    # 实际项目中应从环境变量或配置文件读取
    VALID_USERNAME = "admin"
    VALID_PASSWORD = "123456"
    
    return username == VALID_USERNAME and password == VALID_PASSWORD