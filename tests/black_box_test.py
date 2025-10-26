import pytest
from src.function import calculate_daily_calorie_target
from src.constants import PASS, WARN, EXC_BMI_G, EXC_BMI_L, EXC_SEX, EXC_W, EXC_DATA

# --- A. BLACK BOX TEST CASES ---
# All calorie values are rounded to the nearest 10
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        ("R1_ExcBMI_Underweight", 'L', 53.46, 170, 30, 'M', 2210, EXC_BMI_L),
        ("R2_ExcBMI_Obese", 'G', 86.70, 170, 30, 'M', 3720, EXC_BMI_G),
        ("R3_ExcBMI_And_WarnAge_Old", 'L', 53.46, 170, 65, 'M', 1940, EXC_BMI_L),
        ("R4_ExcBMI_And_WarnAge_Young", 'G', 86.70, 170, 18, 'M', 3810, EXC_BMI_G),
        ("R5_WarnAge_Young", 'L', 70, 170, 17, 'M', 2220, WARN),
        ("R6_WarnAge_Old", 'G', 70, 170, 66, 'M', 2840, WARN),
        ("R7_R11_Pass_L", 'L', 70, 170, 30, 'M', 2060, PASS),
        ("R8_R12_Pass_G", 'G', 70, 170, 30, 'M', 3060, PASS),
        ("R9_Pass_M", 'M', 70, 170, 30, 'M', 2560, PASS),
        ("R10_WarnAge_Old_M", 'M', 70, 170, 65, 'M', 2280, WARN),
    ],
    ids=[
        "R1_L_ExcBMI", "R2_G_ExcBMI", "R3_L_ExcBMI_AgeWarn", "R4_G_ExcBMI_AgeWarn",
        "R5_L_WarnAge", "R6_G_WarnAge", "R7_Pass_L", "R8_Pass_G", "R9_Pass_M", "R10_WarnAge_M"
    ]
)
def test_decision_table_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output

# --- B. BOUNDARY TEST CASES ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        ("I1_BMI_L_Equal", 'L', 53.46, 170, 30, 'M', 2210, EXC_BMI_L),
        ("I2_BMI_L_Minus", 'L', 53.45, 170, 30, 'M', 2210, EXC_BMI_L),
        ("I3_BMI_G_Minus", 'G', 86.69, 170, 30, 'M', 3720, PASS),
        ("I4_BMI_G_Equal", 'G', 86.70, 170, 30, 'M', 3720, EXC_BMI_G),
        ("I5_BMI_G_Plus", 'G', 86.71, 170, 30, 'M', 3720, EXC_BMI_G),
        ("I6_Age_18", 'M', 70, 170, 18, 'M', 2710, WARN),
        ("I7_Age_19", 'M', 70, 170, 19, 'M', 2710, PASS),
        ("I8_Age_65", 'L', 70, 170, 65, 'M', 1780, WARN),
        ("I9_Age_66", 'L', 70, 170, 66, 'M', 1780, WARN),
        ("I10_Age_64", 'L', 70, 170, 64, 'M', 1790, PASS),
        ("I13_Input_Boundary_Weight", 'M', 30.0, 170, 30, 'M', 2010, PASS),
    ]
)
def test_boundary_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output

# --- C. INPUT EXCEPTION TEST CASES ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_Msg",
    [
        ("I11_Input_Error_Sex", 'G', 70, 170, 30, 'Z', EXC_SEX),
        ("I12_Input_Error_Weight", 'M', 29.9, 170, 30, 'M', EXC_W),
        ("Input_Error_Weight_Upper", 'M', 200.1, 170, 30, 'M', EXC_W),
        ("Input_Error_Height_Lower", 'M', 70, 119.9, 30, 'M', EXC_DATA),
        ("Input_Error_Height_Upper", 'M', 70, 230.1, 30, 'M', EXC_DATA),
        ("Input_Error_Age_Lower", 'M', 70, 170, 0, 'M', EXC_DATA),
        ("Input_Error_Age_Upper", 'M', 70, 170, 101, 'M', EXC_DATA),
    ]
)
def test_input_exceptions(name, goal, weight, height, age, sex, expected_Msg):
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (0, expected_Msg)
    assert actual_output == expected_output

# --- D. CONTROL FLOW CLASSIFICATION (SỬA LẠI LOGIC TEST) ---
# ... (Phần này có thể xóa nếu bạn đã có control_flow_test.py riêng)
# ... (Tôi sẽ bỏ qua phần này để tránh trùng lặp với file control_flow_test.py)