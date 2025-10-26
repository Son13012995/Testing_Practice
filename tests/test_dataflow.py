import pytest
from function import calculate_daily_calorie_target

# Định nghĩa hằng số
class Messages:
    PASS = "Pass"
    WARN = "Warning: Tham khảo ý kiến bác sĩ"
    EXC_GOAL = "Exception: Mục tiêu không hợp lệ"
    EXC_SEX = "Exception: Giới tính không hợp lệ"
    EXC_W = "Exception: Cân nặng ngoài giới hạn"
    EXC_DATA = "Exception: Dữ liệu đầu vào ngoài giới hạn"
    EXC_BMI_L = "Exception: Mục tiêu không phù hợp"
    EXC_BMI_G = "Exception: Cần tham khảo bác sĩ"

# Sử dụng tham số hóa (parameterization) để gom các test case lại
# Pytest sẽ chạy hàm test_main_scenarios với mỗi bộ dữ liệu trong danh sách.
@pytest.mark.parametrize(
    "goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # --- Rủi ro/Chính (R-cases) ---
        # R1: BMI-G Exception (Node 23(T) -> 24) | G, BMI>=30.0
        ('G', 100, 170, 30, 'M', 3558, Messages.EXC_BMI_G),
        # R2: BMI-L Exception (Node 21(T) -> 22) | L, BMI<=18.5
        ('L', 50, 170, 30, 'M', 1327, Messages.EXC_BMI_L),
        # R3: Age Warning - Young (Node 25(T) -> 26) | M, A=17
        ('M', 70, 170, 17, 'M', 2108, Messages.WARN),
        # R4: Age Warning - Old (Node 25(T) -> 26) | M, A=65
        ('M', 70, 170, 65, 'M', 1845, Messages.WARN),
        # R5: Pass - Goal L (Node 25(F) -> 27)
        ('L', 70, 170, 30, 'M', 1608, Messages.PASS),
        # R6: Pass - Goal M (Node 25(F) -> 27)
        ('M', 70, 170, 30, 'F', 1913, Messages.PASS),
        # R7: Pass - Goal G (Node 25(F) -> 27)
        ('G', 70, 170, 30, 'M', 2608, Messages.PASS),
    ]
)
def test_main_scenarios(goal, weight, height, age, sex, expected_C, expected_Msg):
    """Kiểm thử các kịch bản Pass, Warning, và BMI Exception."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    
    # Pytest sử dụng lệnh 'assert' đơn giản thay vì self.assertEqual
    assert actual_output == expected_output


# --- Exception Cases (theo CFG: Node 3, 5, 8, 9) ---
@pytest.mark.parametrize(
    "goal, weight, height, age, sex, expected_Msg",
    [
        # E1: Goal Exception (Node 2(T) -> 3)
        ('X', 70, 170, 30, 'M', Messages.EXC_GOAL),
        # E2: Sex Exception (Node 4(T) -> 5)
        ('M', 70, 170, 30, 'X', Messages.EXC_SEX),
        # E3: Weight Exception (Node 7(T) -> 8) - W > 200
        ('M', 201, 170, 30, 'M', Messages.EXC_W),
        # E4: Data Exception (Node 7(T) -> 9) - H < 120
        ('M', 70, 119, 30, 'M', Messages.EXC_DATA),
        # E5: Data Exception (Node 7(T) -> 9) - A > 100
        ('M', 70, 170, 101, 'M', Messages.EXC_DATA),
    ]
)
def test_input_exceptions(goal, weight, height, age, sex, expected_Msg):
    """Kiểm thử các trường hợp ngoại lệ về dữ liệu đầu vào."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (0, expected_Msg)
    
    # Tất cả các Exception đầu vào trả về C = 0
    assert actual_output == expected_output