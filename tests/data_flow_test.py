import pytest
from src.function import calculate_daily_calorie_target

# --- Định nghĩa Hằng số ---
class Messages:
    PASS = "Pass"
    WARN = "Warning: Tham khảo ý kiến bác sĩ"
    EXC_GOAL = "Exception: Mục tiêu không hợp lệ"
    EXC_SEX = "Exception: Giới tính không hợp lệ"
    EXC_W = "Exception: Cân nặng ngoài giới hạn"
    EXC_BMI_L = "Exception: Mục tiêu không phù hợp"
    EXC_BMI_G = "Exception: Cần tham khảo bác sĩ"

# --- TEST CASE CHO BIẾN goal ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # goal: I→2 (p-use, F), path: 1→2→4→⋯→27
        ("G1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # goal: I→2 (p-use, T), path: 1→2→3→Exit
        ("G2", 'X', 70, 170, 30, 'M', 0, Messages.EXC_GOAL),
        
        # goal: I→15 (p-use, T), path: 1→⋯→15→17→⋯→27
        ("G3", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # goal: I→16 (p-use, T), path: 1→⋯→15→16→18→⋯→27
        ("G4", 'L', 70, 170, 30, 'M', 2007, Messages.PASS),
        
        # goal: I→23 (p-use, F), path: 1→⋯→23→25→27
        ("G5", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # goal: I→21 (p-use, F), path: 1→⋯→21→23→25→27
        ("G6", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
    ]
)
def test_goal_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến goal"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN sex ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # sex: I→4 (p-use, F), path: 1→2→4→7→⋯→27
        ("S1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # sex: I→4 (p-use, T), path: 1→2→4→5→Exit
        ("S2", 'M', 70, 170, 30, 'X', 0, Messages.EXC_SEX),
        
        # sex: I→11 (p-use, T), path: 1→⋯→11→12→14→⋯→27
        ("S3", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
    ]
)
def test_sex_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến sex"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN weight ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # weight: I→7 (p-use, F), path: 1→⋯→7→10→⋯→27
        ("W1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # weight: I→7 (c-use, W≤200, T), path: 1→⋯→7→8→Exit
        ("W2", 'M', 201, 170, 30, 'M', 0, Messages.EXC_W),
        
        # weight: I→10 (c-use), path: 1→⋯→10→11→⋯→27
        ("W3", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # weight: I→12 (c-use), path: 1→⋯→12→14→⋯→27
        ("W4", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # weight: I→13 (c-use), path: 1→⋯→11→13→14→⋯→27
        ("W5", 'M', 70, 170, 30, 'F', 2250, Messages.PASS),
    ]
)
def test_weight_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến weight"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN age ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # age: I→7 (p-use, F), path: 1→⋯→7→10→⋯→27
        ("A1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # age: I→25 (p-use, F), path: 1→⋯→25→27
        ("A2", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # age: I→25 (p-use, T), path: 1→⋯→25→26→Exit
        ("A3", 'M', 70, 170, 17, 'M', 2608, Messages.WARN),
    ]
)
def test_age_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến age"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN bmr ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # bmr: 12→14 (c-use), path: 1→⋯→12→14→⋯→27
        ("B1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # bmr: 13→14 (c-use), path: 1→⋯→13→14→⋯→27
        ("B2", 'M', 70, 170, 30, 'F', 2250, Messages.PASS),
    ]
)
def test_bmr_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến bmr"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN tdee ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # tdee: 14→17 (c-use), path: 1→⋯→14→15→17→⋯→27
        ("T1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # tdee: 14→18 (c-use), path: 1→⋯→14→15→16→18→⋯→27
        ("T2", 'L', 70, 170, 30, 'M', 2007, Messages.PASS),
        
        # tdee: 14→19 (c-use), path: 1→⋯→14→15→16→19→⋯→27
        ("T3", 'G', 70, 170, 30, 'M', 3007, Messages.PASS),
    ]
)
def test_tdee_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến tdee"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"

# --- TEST CASE CHO BIẾN C ---
@pytest.mark.parametrize(
    "tc_id, goal, weight, height, age, sex, expected_C, expected_Msg",
    [
        # C: 20→21 (p-use, F), path: 1→⋯→21→23→25→27
        ("C1", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # C: 20→23 (p-use, F), path: 1→⋯→23→25→27
        ("C2", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # C: 20→25 (p-use, F), path: 1→⋯→25→27
        ("C3", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # C: 20→27 (c-use), path: 1→⋯→27
        ("C4", 'M', 70, 170, 30, 'M', 2507, Messages.PASS),
        
        # C: 20→21 (p-use, T), path: 1→⋯→21→22→Exit
        ("C5", 'L', 50, 170, 30, 'M', 1697, Messages.EXC_BMI_L),
        
        # C: 20→23 (p-use, T), path: 1→⋯→23→24→Exit
        ("C6", 'G', 100, 170, 30, 'M', 3472, Messages.EXC_BMI_G),
        
        # C: 20→25 (p-use, T), path: 1→⋯→25→26→Exit
        ("C7", 'M', 70, 170, 17, 'M', 2608, Messages.WARN),
    ]
)
def test_C_du_pairs(tc_id, goal, weight, height, age, sex, expected_C, expected_Msg):
    """Test các du-pair cho biến C"""
    actual_output = calculate_daily_calorie_target(goal, weight, height, age, sex)
    expected_output = (expected_C, expected_Msg)
    assert actual_output == expected_output, f"[{tc_id}] Test failed"