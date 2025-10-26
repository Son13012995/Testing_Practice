import math

def calculate_daily_calorie_target(goal, weight, height, age, sex):
    """
    Tính toán Calo Mục tiêu hàng ngày (C) và trả về thông báo hành động.
    Input: goal (M/L/G), weight (kg), height (cm), age (năm), sex (M/F).
    Output: (Calorie_Target_C, Message)
    """

    # --- 1. Kiểm tra Giới hạn Input (Exception ưu tiên cao nhất) ---
    
    # Kiểm tra Giới tính, Mục tiêu
    if goal not in ['M', 'L', 'G']:
        return 0, "Exception: Mục tiêu không hợp lệ"
    if sex not in ['M', 'F']:
        return 0, "Exception: Giới tính không hợp lệ"
    
    # Kiểm tra Phạm vi Dữ liệu (W, H, A)
    if not (30.0 <= weight <= 200.0 and 120.0 <= height <= 230.0 and 1 <= age <= 100):
        if not (30.0 <= weight <= 200.0):
            return 0, "Exception: Cân nặng ngoài giới hạn"
        return 0, "Exception: Dữ liệu đầu vào ngoài giới hạn"

    # --- 2. Tính BMI, BMR, TDEE ---
    
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)

    # Tính BMR (Mifflin-St Jeor)
    if sex == 'M':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else: # sex == 'F'
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        
    # Tính TDEE (Hệ số hoạt động Trung bình: 1.55)
    tdee = bmr * 1.55

    # --- 3. Tính Calo Mục tiêu (C) ---
    
    if goal == 'M':
        target_calorie = tdee
    elif goal == 'L':
        target_calorie = tdee - 500
    else: # goal == 'G'
        target_calorie = tdee + 500
        
    # Làm tròn Calo mục tiêu về số nguyên
    C = round(target_calorie)

    # --- 4. Logic Exception/Warning (Kiểm tra Ưu tiên) ---

    # Priority 1: BMI Exception (Mục tiêu không an toàn)
    if (goal == 'L' and bmi <= 18.5):
        # Trả về C đã tính toán kèm thông báo lỗi
        return C, "Exception: Mục tiêu không phù hợp"
    elif (goal == 'G' and bmi >= 30.0):
        # Trả về C đã tính toán kèm thông báo lỗi
        return C, "Exception: Cần tham khảo bác sĩ"

    # Priority 2: Age Warning
    if age <= 18 or age >= 65:
        # Trả về C đã tính toán kèm cảnh báo
        return C, "Warning: Tham khảo ý kiến bác sĩ"

    # Priority 3: Pass
    return C, "Pass"