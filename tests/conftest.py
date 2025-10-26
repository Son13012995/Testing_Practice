import os
import sys

# Thêm project root (thư mục chứa src/) vào đầu sys.path để import 'src' hoạt động
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)