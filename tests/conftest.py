import sys
import os

# Thêm thư mục gốc (TESTING_PRACTICE) vào đường dẫn hệ thống
# để Python có thể tìm thấy thư mục 'src'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)