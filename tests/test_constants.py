import pytest
from Python_Calorie.src.constants import *

def test_constants():
    assert PASS == "Pass"
    assert WARN == "Warning: Tham khảo ý kiến bác sĩ"
    assert EX_BMI_L == "Exception: Mục tiêu không phù hợp"
    assert EX_BMI_G == "Exception: Cần tham khảo bác sĩ"
    assert EX_INPUT_SEX == "Exception: Giới tính không hợp lệ"
    assert EX_INPUT_W == "Exception: Cân nặng ngoài giới hạn"
    assert EX_INPUT_DATA == "Exception: Dữ liệu đầu vào ngoài giới hạn"