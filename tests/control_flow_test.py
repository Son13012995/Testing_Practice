import pytest
from src.function import calculate_daily_calorie_target
from src.constants import (
    PASS, WARN, EXC_BMI_G, EXC_BMI_L, 
    EXC_GOAL, EXC_SEX, EXC_W, EXC_DATA
)

# Test cases with calorie values rounded to the nearest 10
cases = [
    # Input, Expected Cal, Expected Msg
    (('X', 70, 170, 30, 'M'), 0, EXC_GOAL),
    (('M', 70, 170, 30, 'Z'), 0, EXC_SEX),
    (('M', 25.0, 170, 30, 'M'), 0, EXC_W),
    (('M', 70, 110.0, 30, 'M'), 0, EXC_DATA),
    (('M', 70, 170, 30, 'M'), 2560, PASS),
    (('L', 48, 170, 30, 'F'), 1630, EXC_BMI_L),
    (('G', 100, 170, 30, 'M'), 3950, EXC_BMI_G),
    (('M', 70, 170, 70, 'F'), 1990, WARN),  # Age 70 > AGE_MAX (64)
    (('L', 65, 170, 30, 'F'), 1800, PASS),
    (('G', 70, 170, 30, 'M'), 3060, PASS),
]

@pytest.mark.parametrize("inputs, expected_cal, expected_msg", cases)
def test_control_flow_scenarios(inputs, expected_cal, expected_msg):
    """
    Kiểm tra các luồng chính dựa trên ca kiểm thử được cung cấp.
    """
    # Tách tuple inputs
    goal, weight, height, age, sex = inputs
    
    actual_cal, actual_msg = calculate_daily_calorie_target(goal, weight, height, age, sex)
    
    assert (actual_cal, actual_msg) == (expected_cal, expected_msg)