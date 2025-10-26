# File này chứa tất cả các thông báo và hằng số
# Thông báo đầu ra chuẩn
PASS = "Pass"
WARN = "Warning: Consult a doctor"
EXC_BMI_L = "Exception: Target not suitable"  # For underweight trying to lose
EXC_BMI_G = "Exception: Consult a doctor"     # For obese trying to gain
EXC_GOAL = "Exception: Invalid goal"
EXC_SEX = "Exception: Invalid gender"
EXC_W = "Exception: Weight out of range"
EXC_DATA = "Exception: Input data out of range"

# Thresholds from problem description
BMI_LOW = 18.5       # Underweight threshold
BMI_HIGH = 30.0      # Obesity threshold
AGE_MIN = 18         # Age warning threshold lower
AGE_MAX = 65         # Age warning threshold upper
WEIGHT_MIN = 30.0    # Minimum allowed weight
WEIGHT_MAX = 200.0   # Maximum allowed weight
HEIGHT_MIN = 120.0   # Minimum allowed height
HEIGHT_MAX = 230.0   # Maximum allowed height
AGE_MAX_LIMIT = 100  # Maximum allowed age