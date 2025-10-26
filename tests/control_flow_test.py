import pytest
# Import từ thư mục src/ theo cấu trúc dự án của bạn
from src.function import calculate_daily_calorie_target 

# --- Định nghĩa Hằng số Thông báo ---
# Đảm bảo các hằng số này khớp với giá trị trả về trong file function.py
class Messages:
    PASS = "Pass"
    WARN = "Warning: Tham khảo ý kiến bác sĩ"
    EXC_GOAL = "Exception: Mục tiêu không hợp lệ"
    EXC_SEX = "Exception: Giới tính không hợp lệ"
    EXC_W = "Exception: Cân nặng ngoài giới hạn"
    EXC_DATA = "Exception: Dữ liệu đầu vào ngoài giới hạn"
    EXC_BMI_L = "Exception: Mục tiêu không phù hợp"
    EXC_BMI_G = "Exception: Cần tham khảo bác sĩ"

# --- Dữ liệu Kiểm thử Luồng Điều khiển (Control Flow Test Cases) ---
# Tôi sẽ ước tính giá trị Calorie (C) dự kiến dựa trên các giả định tiêu chuẩn
# và logic làm tròn/ghi đè trong file function.py của bạn.
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # TC-1: Invalid Goal (Node 2 -> 3)
        ('TC-1', 'X', 70, 170, 30, 'M', 0, Messages.EXC_GOAL),
        
        # TC-2: Invalid Sex (Node 4 -> 5)
        ('TC-2', 'M', 70, 170, 30, 'Z', 0, Messages.EXC_SEX),
        
        # TC-3: Invalid Weight (W=25.0, Node 7 -> 8, W < 30.0)
        ('TC-3', 'M', 25.0, 170, 30, 'M', 0, Messages.EXC_W),
        
        # TC-4: Invalid Height (H=110.0, Node 7 -> 9, H < 120.0)
        ('TC-4', 'M', 70, 110.0, 30, 'M', 0, Messages.EXC_DATA),
        
        # TC-5: Pass (Normal M) - BMR=1618.75, TDEE=2507 -> C=2507 (làm tròn)
        ('TC-5', 'M', 70, 170, 30, 'M', 2507, Messages.PASS), 
        
        # TC-6: BMI Exception (L, BMI=16.5) - BMI < 18.5 (Node 21 -> 22).
        # BMR(48, 170, 30, F)=1283.5; TDEE=1989.4; L=1489.4 -> C=1409
        ('TC-6', 'L', 48, 170, 30, 'F', 1409, Messages.EXC_BMI_L),
        
        # TC-7: BMI Exception (G, BMI=34.6) - BMI >= 30.0 (Node 23 -> 24).
        # BMR(100, 170, 30, M)=1955; TDEE=3030.25; G=3472
        ('TC-7', 'G', 100, 170, 30, 'M', 3472, Messages.EXC_BMI_G),
        
        # TC-8: Age Warning (A=70) - A >= 65 (Node 25 -> 26).
        # BMR(70, 170, 70, F)=1251.75; TDEE=1940.21; M=1940
        ('TC-8', 'M', 70, 170, 70, 'F', 1940, Messages.WARN), 
        
        # TC-9: Pass (Normal F) - BMR(65, 170, 30, F)=1398.75; TDEE=2168.06; L=1672
        ('TC-9', 'L', 65, 170, 30, 'F', 1672, Messages.PASS),
        
        # TC-10: Pass (Normal G) - BMR=1618.75, TDEE=2507; G=3007
        ('TC-10', 'G', 70, 170, 30, 'M', 3007, Messages.PASS), 
    ]
)
def test_control_flow_cases(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """
    Kiểm thử các trường hợp luồng điều khiển chính theo CFG.
    """
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    
    assert actual_output == expected_output, f"[{tc_id}] Test failed. Expected {expected_output}, got {actual_output}"