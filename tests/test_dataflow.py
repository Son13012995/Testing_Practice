import pytest
from src.function import calculate_daily_calorie_target
from src.constants import (
    PASS, WARN, EXC_BMI_G, EXC_BMI_L, 
    EXC_GOAL, EXC_SEX, EXC_W, EXC_DATA
)

# Test cases with calorie values rounded to the nearest 10
# Duplicate test cases removed
@pytest.mark.parametrize(
    "goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # --- Pass cases ---
        ('M', 70, 170, 30, 'M', 2560, PASS),
        ('L', 70, 170, 30, 'M', 2060, PASS),
        ('M', 70, 170, 30, 'F', 2300, PASS),
        ('G', 70, 170, 30, 'M', 3060, PASS),
        
        # --- Warning cases ---
        ('M', 70, 170, 17, 'M', 2720, WARN),  # Age 17 < AGE_MIN (19)

        # --- BMI Exception cases ---
        ('L', 50, 170, 30, 'M', 2080, EXC_BMI_L),
        ('G', 100, 170, 30, 'M', 3950, EXC_BMI_G),
        
        # --- Input Exception cases ---
        ('X', 70, 170, 30, 'M', 0, EXC_GOAL),
        ('M', 70, 170, 30, 'X', 0, EXC_SEX),
        ('M', 200.1, 170, 30, 'M', 0, EXC_W),  # Assuming WEIGHT_MAX = 200
    ]
)
def test_dataflow_scenarios(goal, weight, height, age, sex, expected_C, expected_Msg):
    """Kiểm thử các kịch bản dataflow đã được tính toán lại."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output