import pytest
from Python_Calorie.src.function import calculate_daily_calorie_target
from Python_Calorie.tests.black_box_test import Messages

@pytest.mark.parametrize(
    "goal, weight, height, age, sex, expected_Msg",
    [
        ('X', 70, 170, 30, 'M', Messages.EX_INPUT_SEX),
        ('M', 70, 170, 30, 'Z', Messages.EX_INPUT_SEX),
        ('M', 25.0, 170, 30, 'M', Messages.EX_INPUT_W),
        ('M', 70, 110.0, 30, 'M', Messages.EX_INPUT_DATA),
        ('M', 70, 170, 30, 'M', Messages.PASS),
        ('L', 48, 170, 30, 'F', Messages.EX_INPUT_SEX),
        ('G', 100, 170, 30, 'M', Messages.EX_INPUT_DATA),
        ('M', 70, 170, 70, 'F', Messages.EX_INPUT_DATA),
        ('L', 65, 170, 30, 'F', Messages.EX_INPUT_SEX),
        ('G', 70, 170, 30, 'M', Messages.PASS),
    ]
)
def test_control_flow_scenarios(goal, weight, height, age, sex, expected_Msg):
    """Test various control flow scenarios."""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (0, expected_Msg) if 'Exception' in expected_Msg else (None, expected_Msg)
    assert actual_output == expected_output