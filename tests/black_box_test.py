import pytest
from src.function import calculate_daily_calorie_target

# --- Định nghĩa Hằng số (Phải được định nghĩa nếu không có trong function.py) ---
class Messages:
    PASS = "Pass"
    WARN = "Warning: Tham khảo ý kiến bác sĩ"
    EX_BMI_L = "Exception: Mục tiêu không phù hợp"
    EX_BMI_G = "Exception: Cần tham khảo bác sĩ"
    EX_INPUT_SEX = "Exception: Giới tính không hợp lệ"
    EX_INPUT_W = "Exception: Cân nặng ngoài giới hạn"
    # Thêm hằng số chung cho các lỗi input khác
    EX_INPUT_DATA = "Exception: Dữ liệu đầu vào ngoài giới hạn" 


# --- A. TEST CASE BẢNG QUYẾT ĐỊNH (R1 - R12) ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # R1: L, BMI<=18.5, A<65 (Exc BMI) - C_actual = 1751
        ("R1_ExcBMI_Underweight", 'L', 53.46, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        # R2: G, BMI>=30, A<65 (Exc BMI) - C_actual = 3266
        ("R2_ExcBMI_Obese", 'G', 86.70, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        # R3: L, BMI<=18.5, A>=65 (Exc BMI Ưu tiên) - C_actual = 1480
        ("R3_ExcBMI_AgeWarn", 'L', 53.46, 170, 65, 'M', 1480, Messages.EX_BMI_L), 
        # R4: G, BMI>=30, A<=18 (Exc BMI Ưu tiên) - C_actual = 3359
        ("R4_ExcBMI_AgeWarn", 'G', 86.70, 170, 18, 'M', 3359, Messages.EX_BMI_G), 
        # R5: L, BMI>18.5, A<=18 (Pass & Warn Age) - C_actual = 2108
        ("R5_WarnAge_Young", 'L', 70, 170, 17, 'M', 2108, Messages.WARN),
        # R6: G, BMI<30, A>=65 (Pass & Warn Age) - C_actual = 2728
        ("R6_WarnAge_Old", 'G', 70, 170, 66, 'M', 2728, Messages.WARN),
        # R7/R11: L, BMI>18.5, A Normal (Pass) - C_actual = 2007
        ("R7_R11_Pass_L", 'L', 70, 170, 30, 'M', 2007, Messages.PASS),
        # R8/R12: G, BMI<30, A Normal (Pass) - C_actual = 3007
        ("R8_R12_Pass_G", 'G', 70, 170, 30, 'M', 3007, Messages.PASS),
        # R9: M, BMI Normal, A Normal (Pass) - C_actual = 2507
        ("R9_Pass_M", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        # R10: M, A>=65 (Warn Age) - C_actual = 2236
        ("R10_WarnAge_Old_M", 'M', 70, 170, 65, 'M', 2236, Messages.WARN),
    ]
)
def test_decision_table_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Kiểm thử theo Bảng Quyết định."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output


# --- B. TEST CASE KIỂM THỬ BIÊN (I1 - I13) VÀ NGOẠI LỆ INPUT ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # I1: L, BMI = 18.50 (Biên dưới) -> Exc. C_actual = 1751
        ("I1_BMI_L_Equal", 'L', 53.46, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        # I2: L, BMI < 18.50 (Biên dưới -) -> Exc. C_actual = 1751
        ("I2_BMI_L_Minus", 'L', 53.45, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        # I3: G, BMI < 30.00 (Biên trên -) -> Pass. C_actual = 3266
        ("I3_BMI_G_Minus", 'G', 86.69, 170, 30, 'M', 3266, Messages.PASS),
        # I4: G, BMI = 30.00 (Biên trên) -> Exc. C_actual = 3266
        ("I4_BMI_G_Equal", 'G', 86.70, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        # I5: G, BMI > 30.00 (Biên trên +) -> Exc. C_actual = 3266
        ("I5_BMI_G_Plus", 'G', 86.71, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        
        # I6: M, A = 18 (Biên Tuổi) -> Warn. C_actual = 2600
        ("I6_Age_18", 'M', 70, 170, 18, 'M', 2600, Messages.WARN),
        # I7: M, A = 19 (Biên Tuổi +) -> Pass. C_actual = 2592
        ("I7_Age_19", 'M', 70, 170, 19, 'M', 2592, Messages.PASS),
        # I8: L, A = 65 (Biên Tuổi) -> Warn. C_actual = 1736
        ("I8_Age_65", 'L', 70, 170, 65, 'M', 1736, Messages.WARN),
        # I10: L, A = 64 (Biên Tuổi -) -> Pass. C_actual = 1744
        ("I10_Age_64", 'L', 70, 170, 64, 'M', 1744, Messages.PASS),
        # I9: L, A = 66 (Biên Tuổi +) -> Warn. C_actual = 1728
        ("I9_Age_66", 'L', 70, 170, 66, 'M', 1728, Messages.WARN),

        # I13: M, W=30.0 (Biên Cân nặng Input) -> Pass. C_actual = 1887
        ("I13_Input_Boundary_Weight", 'M', 30.0, 170, 30, 'M', 1887, Messages.PASS),
    ]
)
def test_boundary_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Kiểm thử các kịch bản kiểm thử biên (BMI, Tuổi, Cân nặng)."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output

# --- TEST CASE NGOẠI LỆ INPUT (Phải trả về C=0) ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_Msg",
    [
        # I11: G=G, S=Z (Lỗi Giới tính Input)
        ("I11_Input_Error_Sex", 'G', 70, 170, 30, 'Z', Messages.EX_INPUT_SEX),
        # I12: M, W=29.9 (Lỗi Cân nặng Input)
        ("I12_Input_Error_Weight", 'M', 29.9, 170, 30, 'M', Messages.EX_INPUT_W),
        # Lỗi Input: Tuổi âm (Bị bắt bởi EXC_DATA trong hàm)
        ("I_Input_Error_Age_Negative", 'M', 70, 170, -1, 'M', Messages.EX_INPUT_DATA), 
        # Lỗi Input: Chiều cao ngoài giới hạn (H > 230)
        ("I_Input_Error_Height_Upper", 'M', 70, 231, 30, 'M', Messages.EX_INPUT_DATA),
    ]
)
def test_input_exceptions(name, goal, weight, height, age, sex, expected_Msg):
    """Kiểm thử các trường hợp ngoại lệ về dữ liệu đầu vào (C=0)."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (0, expected_Msg)
    assert actual_output == expected_output