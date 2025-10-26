def calculate_daily_calorie_target(goal, weight, height, age, sex):
    # Example implementation of the calorie calculation logic
    # This is a placeholder and should be replaced with actual logic
    if sex not in ['M', 'F']:
        return (0, "Exception: Giới tính không hợp lệ")
    
    if weight < 30 or weight > 300:
        return (0, "Exception: Cân nặng ngoài giới hạn")
    
    if height < 120 or height > 250:
        return (0, "Exception: Dữ liệu đầu vào ngoài giới hạn")
    
    if age < 0 or age > 100:
        return (0, "Exception: Dữ liệu đầu vào ngoài giới hạn")
    
    # Simple calorie calculation based on goal
    if goal == 'L':
        return (weight * 30, "Pass")
    elif goal == 'G':
        return (weight * 40, "Pass")
    elif goal == 'M':
        return (weight * 35, "Pass")
    
    return (0, "Exception: Mục tiêu không phù hợp")