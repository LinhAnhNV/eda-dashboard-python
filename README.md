# EDA Dashboard - Titanic
Phân tích dữ liệu khám phá (EDA) trên dataset Titanic — dùng Pandas để xử lý dữ liệu, Matplotlib và Seaborn để trực quan hóa, scikit-learn để load dataset.
Bắt đầu từ việc khảo sát sơ bộ, mở rộng dần qua từng loại biểu đồ. Viết từng bước, phân tích từng kết quả — không dùng notebook, không template có sẵn.

> An exploratory data analysis project on the Titanic dataset. Built step by step, chart by chart.

---

## Nội dung phân tích / Analysis

- Khảo sát sơ bộ — shape, kiểu dữ liệu, missing values, thống kê mô tả
- Phân phối tuổi hành khách — histogram + KDE
- Tỉ lệ sống sót theo giới tính — countplot, barplot
- Giá vé theo hạng vé — boxplot, phát hiện outlier
- Tương quan giữa các biến số — heatmap
- Tổng quan đa biến — pairplot theo sống/chết
- Kết luận — nhận xét từng yếu tố ảnh hưởng đến tỉ lệ sống sót

---

## Biểu đồ / Charts

| # | Loại | Nội dung |
|---|------|----------|
| 1 | Countplot | Tỉ lệ sống sót theo giới tính |
| 2 | Histogram | Phân phối tuổi hành khách |
| 3 | Boxplot | Giá vé theo hạng vé |
| 4 | Heatmap | Tương quan giữa các biến số |
| 5 | Barplot | Tỉ lệ sống sót theo giới tính |
| 6 | Pairplot | Tổng quan đa biến (age, fare, pclass) |

---

## Cấu trúc / Structure

```
eda-dashboard-python/
├── main.py       # Load data, vẽ biểu đồ, kết luận
└── README.md
```

---

## Yêu cầu / Requirements

- Python >= 3.11
- pandas
- matplotlib
- seaborn
- scikit-learn

---

## Cài đặt & Chạy / Setup & Run

```bash
# Clone repo
git clone https://github.com/LinhAnhNV/eda-dashboard-python.git
cd eda-dashboard-python

# Cài thư viện
pip install pandas matplotlib seaborn scikit-learn

# Chạy
python main.py
```

---

## Kết luận / Findings

| Yếu tố | Nhận xét |
|--------|----------|
| Giới tính | Phụ nữ có tỉ lệ sống sót cao hơn đáng kể — ưu tiên cứu hộ phụ nữ và trẻ em |
| Hạng vé | Hạng 1 sống sót nhiều hơn hạng 3 — tương quan âm giữa pclass và survived |
| Giá vé | Tương quan dương với sống sót — hành khách trả cao hơn có lợi thế hơn |
| Tuổi | Hành khách trẻ có tỉ lệ sống sót cao hơn |
| Deck | Thiếu 77% dữ liệu — không đủ tin cậy để phân tích |

---

## Tác giả / Author

**Nguyễn Văn Linh Anh**  
Sinh viên CNTT — ĐH Công Thương TP.HCM (HUIT)  
Củ Chi, TP.HCM · 2025