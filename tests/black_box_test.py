import pytest
from src.function import calculate_daily_calorie_target

# Define constants for easier use
class Messages:
    PASS = "Pass"
    WARN = "Warning: Consult a doctor"
    EX_BMI_L = "Exception: Target not suitable"
    EX_BMI_G = "Exception: Consult a doctor"
    EX_INPUT_SEX = "Exception: Invalid gender"
    EX_INPUT_W = "Exception: Weight out of range"
    EX_INPUT_DATA = "Exception: Input data out of range"

# --- A. BLACK BOX TEST CASES ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        ("R1_ExcBMI_Underweight", 'L', 53.46, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        ("R2_ExcBMI_Obese", 'G', 86.70, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        ("R3_ExcBMI_And_WarnAge_Old", 'L', 53.46, 170, 65, 'M', 1480, Messages.EX_BMI_L),
        ("R4_ExcBMI_And_WarnAge_Young", 'G', 86.70, 170, 18, 'M', 3359, Messages.EX_BMI_G),
        ("R5_WarnAge_Young", 'L', 70, 170, 17, 'M', 2108, Messages.WARN),
        ("R6_WarnAge_Old", 'G', 70, 170, 66, 'M', 2728, Messages.WARN),
        ("R7_R11_Pass_L", 'L', 70, 170, 30, 'M', 2007, Messages.PASS),
        ("R8_R12_Pass_G", 'G', 70, 170, 30, 'M', 3007, Messages.PASS),
        ("R9_Pass_M", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        ("R10_WarnAge_Old_M", 'M', 70, 170, 65, 'M', 2236, Messages.WARN),
    ],
    ids=[
        "R1_L_ExcBMI", "R2_G_ExcBMI", "R3_L_ExcBMI_AgeWarn", "R4_G_ExcBMI_AgeWarn",
        "R5_L_WarnAge", "R6_G_WarnAge", "R7_Pass_L", "R8_Pass_G", "R9_Pass_M", "R10_WarnAge_M"
    ]
)
def test_decision_table_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test according to the Decision Table (Including scenarios R)."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output

# --- B. BOUNDARY TEST CASES ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        ("I1_BMI_L_Equal", 'L', 53.46, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        ("I2_BMI_L_Minus", 'L', 53.45, 170, 30, 'M', 1751, Messages.EX_BMI_L),
        ("I3_BMI_G_Minus", 'G', 86.69, 170, 30, 'M', 3266, Messages.PASS),
        ("I4_BMI_G_Equal", 'G', 86.70, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        ("I5_BMI_G_Plus", 'G', 86.71, 170, 30, 'M', 3266, Messages.EX_BMI_G),
        ("I6_Age_18", 'M', 70, 170, 18, 'M', 2600, Messages.WARN),
        ("I7_Age_19", 'M', 70, 170, 19, 'M', 2592, Messages.PASS),
        ("I8_Age_65", 'L', 70, 170, 65, 'M', 1736, Messages.WARN),
        ("I9_Age_66", 'L', 70, 170, 66, 'M', 1728, Messages.WARN),
        ("I10_Age_64", 'L', 70, 170, 64, 'M', 1744, Messages.PASS),
        ("I13_Input_Boundary_Weight", 'M', 30.0, 170, 30, 'M', 1887, Messages.PASS),
    ]
)
def test_boundary_scenarios(name, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test boundary scenarios (BMI, Age, Weight)."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output

# --- C. INPUT EXCEPTION TEST CASES ---
@pytest.mark.parametrize(
    "name, goal, weight, height, age, sex, expected_Msg",
    [
        ("I11_Input_Error_Sex", 'G', 70, 170, 30, 'Z', Messages.EX_INPUT_SEX),
        ("I12_Input_Error_Weight", 'M', 29.9, 170, 30, 'M', Messages.EX_INPUT_W),
        ("Input_Error_Height_Lower", 'M', 70, 119, 30, 'M', Messages.EX_INPUT_DATA),
        ("Input_Error_Age_Upper", 'M', 70, 170, 101, 'M', Messages.EX_INPUT_DATA),
    ]
)
def test_input_exceptions(name, goal, weight, height, age, sex, expected_Msg):
    """Test input exception cases."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (0, expected_Msg)
    assert actual_output == expected_output