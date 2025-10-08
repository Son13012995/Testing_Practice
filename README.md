## Calorie Target Calculation and Evaluation System Testing Practice

---

**Tính toán và Đánh giá Mục tiêu Calo Hàng ngày**.

### 1. Mô tả Bài toán (Problem Description)

[cite_start]Chương trình này được thiết kế để tính toán lượng **Calo Mục tiêu (C)** cần tiêu thụ mỗi ngày dựa trên thông tin cá nhân và **Mục tiêu Thể chất (G)** của người dùng[cite: 11].

[cite_start]Đầu ra của chương trình phải là **số Calo Mục tiêu** (dựa trên TDEE) hoặc một **thông báo/cảnh báo/exception cụ thể** khi các điều kiện đặc biệt xảy ra[cite: 12].

---

### 2. Đầu vào (Inputs)

[cite_start]Chương trình yêu cầu người dùng cung cấp các thông tin sau[cite: 14]:

| Biến số | Mô tả | Phạm vi hợp lệ (Giới hạn Input) | Lưu ý |
| :--- | :--- | :--- | :--- |
| **G** | Mục tiêu (Goal) | M (Duy trì), L (Giảm cân), G (Tăng cân) | [cite_start]Bắt buộc chọn 1 trong 3[cite: 14]. |
| **W** | Cân nặng (Weight) | $30.0 \text{ kg} \le W \le 200.0 \text{ kg}$ | [cite_start]Số thực[cite: 14]. |
| **H** | Chiều cao (Height) | $120.0 \text{ cm} \le H \le 230.0 \text{ cm}$ | [cite_start]Số thực[cite: 14]. |
| **A** | Độ tuổi (Age) | $1 \text{ tuổi} \le A \le 100 \text{ tuổi}$ | [cite_start]Số nguyên[cite: 14]. |
| **S** | Giới tính (Sex) | M (Nam) hoặc F (Nữ) | [cite_start]Bắt buộc[cite: 14]. |

---

### 3. Công thức Tính toán (Calculation Formulas)

[cite_start]Chương trình sử dụng công thức **Harris-Benedict cải tiến** (giả định Mức độ Vận động vừa phải)[cite: 18].

#### 3.1. Công thức BMR

* [cite_start]**Nam (M):** [cite: 16]
    $$BMR = (10 \times W) + (6.25 \times H) - (5 \times A) + 5$$
* [cite_start]**Nữ (F):** [cite: 17]
    $$BMR = (10 \times W) + (6.25 \times H) - (5 \times A) - 161$$

#### 3.2. Công thức TDEE và Calo Mục tiêu (C)

1.  [cite_start]**TDEE (Tổng năng lượng tiêu hao hằng ngày):** [cite: 18]
    $$TDEE = BMR \times 1.55$$
2.  **Calo Mục tiêu (C):** Được tính dựa trên TDEE và Mục tiêu ($G$):
    * $G = \text{M (Duy trì)}: C = TDEE$
    * $G = \text{L (Giảm cân)}: C = TDEE - 500$
    * $G = \text{G (Tăng cân)}: C = TDEE + 500$

---

### 4. Quy tắc Đầu ra & Xử lý Ngoại lệ (Output & Exception Handling)

[cite_start]Calo Mục tiêu (C) cuối cùng và thông báo đầu ra được điều chỉnh theo các quy tắc sau[cite: 20]:

| Điều kiện | Mục tiêu (G) | Quy tắc tính Calo Mục tiêu (C) | Kết quả Output |
| :--- | :--- | :--- | :--- |
| **Trường hợp 1 (Tuổi)** | Bất kỳ | $C=TDEE\pm 500$ (theo G) | [cite_start]$C$ và **Cảnh báo:** "Tham khảo ý kiến bác sĩ" (Nếu $A \le 18$ hoặc $A \ge 65$)[cite: 20]. |
| **Trường hợp 2 (Giảm cân nguy hiểm)** | $G = \text{L (Giảm cân)} \text{ VÀ } \text{BMI} < 18.5$ | $C=TDEE-500$ | [cite_start]**Exception:** "Mục tiêu không phù hợp" (Giảm calo nguy hiểm)[cite: 20]. |
| **Trường hợp 3 (Tăng cân béo phì)** | $G = \text{G (Tăng cân)} \text{ VÀ } \text{BMI} \ge 30$ | $C=TDEE+500$ | [cite_start]**Exception:** "Cần tham khảo bác sĩ" (Không nên tự ý tăng cân khi béo phì)[cite: 20]. |
| **Trường hợp 4 (Bình thường)** | Khác (Bình thường) | $C$ (theo $G$) | [cite_start]$C$ (Pass)[cite: 20]. |

---

