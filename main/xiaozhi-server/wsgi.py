import sys
import os

# 确保项目根目录在 Python 路径中
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.http_server import create_app

# 创建 WSGI 应用
application = create_app() 