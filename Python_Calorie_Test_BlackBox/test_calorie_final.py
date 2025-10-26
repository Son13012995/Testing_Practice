import unittest
from function import calculate_daily_calorie_target

class TestCalorieTarget(unittest.TestCase):

    def setUp(self):
        # Thiết lập các thông báo chuẩn hóa để so sánh
        self.PASS = "Pass"
        self.WARN = "Warning: Tham khảo ý kiến bác sĩ"
        self.EX_BMI_L = "Exception: Mục tiêu không phù hợp"
        self.EX_BMI_G = "Exception: Cần tham khảo bác sĩ"
        self.EX_INPUT_SEX = "Exception: Giới tính không hợp lệ"
        self.EX_INPUT_W = "Exception: Cân nặng ngoài giới hạn"

    # ----------------------------------------------------------------------
    # A. TEST CASE BẢNG QUYẾT ĐỊNH (R1 - R12)
    # ----------------------------------------------------------------------

    # R1: L, BMI<=18.5, A<65 (Exc BMI) - C_actual = 1751
    def test_R1_ExcBMI_Underweight(self):
        self.assertEqual(calculate_daily_calorie_target('L', 53.46, 170, 30, 'M'),
                         (1751, self.EX_BMI_L))

    # R2: G, BMI>=30, A<65 (Exc BMI) - C_actual = 3266
    def test_R2_ExcBMI_Obese(self):
        self.assertEqual(calculate_daily_calorie_target('G', 86.70, 170, 30, 'M'),
                         (3266, self.EX_BMI_G))

    # R3: L, BMI<=18.5, A>=65 (Exc BMI & Warn Age - Exc Ưu tiên) - C_actual = 1480
    def test_R3_ExcBMI_And_WarnAge(self):
        self.assertEqual(calculate_daily_calorie_target('L', 53.46, 170, 65, 'M'),
                         (1480, self.EX_BMI_L)) 
                         
    # R4: G, BMI>=30, A<=18 (Exc BMI & Warn Age - Exc Ưu tiên) - C_actual = 3359
    def test_R4_ExcBMI_And_WarnAge(self):
        self.assertEqual(calculate_daily_calorie_target('G', 86.70, 170, 18, 'M'),
                         (3359, self.EX_BMI_G)) 

    # R5: L, BMI>18.5, A<=18 (Pass & Warn Age) - C_actual = 2108
    def test_R5_WarnAge_Young(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 17, 'M'),
                         (2108, self.WARN))

    # R6: G, BMI<30, A>=65 (Pass & Warn Age) - C_actual = 2728
    def test_R6_WarnAge_Old(self):
        self.assertEqual(calculate_daily_calorie_target('G', 70, 170, 66, 'M'),
                         (2728, self.WARN))

    # R7: L, BMI>18.5, A>18/A<65 (Pass) - C_actual = 2007
    def test_R7_Pass_Normal(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 30, 'M'),
                         (2007, self.PASS))

    # R8: G, BMI<30, A>18/A<65 (Pass) - C_actual = 3007
    def test_R8_Pass_Normal(self):
        self.assertEqual(calculate_daily_calorie_target('G', 70, 170, 30, 'M'),
                         (3007, self.PASS))

    # R9: M, BMI Normal, A Normal (Pass) - C_actual = 2507
    def test_R9_Pass_Normal(self):
        self.assertEqual(calculate_daily_calorie_target('M', 70, 170, 30, 'M'),
                         (2507, self.PASS))
                         
    # R10: M, A>=65 (Warn Age) - C_actual = 2236
    def test_R10_WarnAge_Old(self):
        self.assertEqual(calculate_daily_calorie_target('M', 70, 170, 65, 'M'),
                         (2236, self.WARN))
                         
    # R11: L, BMI Normal, A Normal (Pass) - C_actual = 2007 (Trùng R7)
    def test_R11_Pass_Normal(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 30, 'M'),
                         (2007, self.PASS))

    # R12: G, BMI Normal, A Normal (Pass) - C_actual = 3007 (Trùng R8)
    def test_R12_Pass_Normal(self):
        self.assertEqual(calculate_daily_calorie_target('G', 70, 170, 30, 'M'),
                         (3007, self.PASS))

    # ----------------------------------------------------------------------
    # B. TEST CASE KIỂM THỬ BIÊN (I1 - I13)
    # ----------------------------------------------------------------------

    # I1: L, BMI = 18.50 (Biên dưới) -> Exc. C_actual = 1751
    def test_I1_Boundary_BMI_L_Equal(self):
        self.assertEqual(calculate_daily_calorie_target('L', 53.46, 170, 30, 'M'),
                         (1751, self.EX_BMI_L))

    # I2: L, BMI < 18.50 (Biên dưới -) -> Exc. C_actual = 1751
    def test_I2_Boundary_BMI_L_Minus(self):
        self.assertEqual(calculate_daily_calorie_target('L', 53.45, 170, 30, 'M'),
                         (1751, self.EX_BMI_L))

    # I3: G, BMI < 30.00 (Biên trên -) -> Pass. C_actual = 3266
    def test_I3_Boundary_BMI_G_Minus(self):
        self.assertEqual(calculate_daily_calorie_target('G', 86.69, 170, 30, 'M'),
                         (3266, self.PASS))

    # I4: G, BMI = 30.00 (Biên trên) -> Exc. C_actual = 3266
    def test_I4_Boundary_BMI_G_Equal(self):
        self.assertEqual(calculate_daily_calorie_target('G', 86.70, 170, 30, 'M'),
                         (3266, self.EX_BMI_G))

    # I5: G, BMI > 30.00 (Biên trên +) -> Exc. C_actual = 3266
    def test_I5_Boundary_BMI_G_Plus(self):
        self.assertEqual(calculate_daily_calorie_target('G', 86.71, 170, 30, 'M'),
                         (3266, self.EX_BMI_G))

    # I6: M, A = 18 (Biên Tuổi) -> Warn. C_actual = 2600
    def test_I6_Boundary_Age_18(self):
        self.assertEqual(calculate_daily_calorie_target('M', 70, 170, 18, 'M'),
                         (2600, self.WARN))

    # I7: M, A = 19 (Biên Tuổi +) -> Pass. C_actual = 2592
    def test_I7_Boundary_Age_19(self):
        self.assertEqual(calculate_daily_calorie_target('M', 70, 170, 19, 'M'),
                         (2592, self.PASS))

    # I8: L, A = 65 (Biên Tuổi) -> Warn. C_actual = 1736
    def test_I8_Boundary_Age_65(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 65, 'M'),
                         (1736, self.WARN))

    # I9: L, A = 66 (Biên Tuổi +) -> Warn. C_actual = 1728
    def test_I9_Boundary_Age_66(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 66, 'M'),
                         (1728, self.WARN))

    # I10: L, A = 64 (Biên Tuổi -) -> Pass. C_actual = 1744
    def test_I10_Boundary_Age_64(self):
        self.assertEqual(calculate_daily_calorie_target('L', 70, 170, 64, 'M'),
                         (1744, self.PASS))
                         
    # I11: G=G, S=Z (Lỗi Giới tính Input)
    def test_I11_Input_Error_Sex(self):
        self.assertEqual(calculate_daily_calorie_target('G', 70, 170, 30, 'Z'),
                         (0, self.EX_INPUT_SEX)) 
                         
    # I12: M, W=29.9 (Lỗi Cân nặng Input)
    def test_I12_Input_Error_Weight(self):
        self.assertEqual(calculate_daily_calorie_target('M', 29.9, 170, 30, 'M'),
                         (0, self.EX_INPUT_W))

    # I13: M, W=30.0 (Biên Cân nặng Input) -> Pass. C_actual = 1887
    def test_I13_Input_Boundary_Weight(self):
        self.assertEqual(calculate_daily_calorie_target('M', 30.0, 170, 30, 'M'),
                         (1887, self.PASS))