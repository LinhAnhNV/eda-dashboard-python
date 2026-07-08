# 📊 EDA Dashboard

Dashboard phân tích dữ liệu khám phá (EDA) tương tác, xây dựng bằng **Streamlit**, dùng **Pandas** xử lý dữ liệu, **Matplotlib** và **Seaborn** để trực quan hóa. Cho phép chuyển đổi giữa 2 dataset **Titanic** và **Iris**, với bộ lọc trực tiếp trên sidebar.

> An interactive EDA dashboard built with Streamlit, letting users explore the Titanic and Iris datasets with live filters.

---

## Tính năng / Features

- 🔀 Chuyển đổi giữa 2 dataset: Titanic (phân tích sống sót) và Iris (phân loại loài hoa)
- 🎛️ Bộ lọc tương tác trên sidebar (giới tính, hạng vé, khoảng tuổi cho Titanic; loài hoa cho Iris)
- 📈 6 loại biểu đồ mỗi dataset: countplot, histogram, boxplot, barplot, heatmap tương quan
- 🧮 Thống kê tổng quan (shape, missing values, describe) cập nhật theo bộ lọc

---

## Biểu đồ / Charts (Titanic)

| # | Loại | Nội dung |
|---|------|----------|
| 1 | Countplot | Tỉ lệ sống sót theo giới tính |
| 2 | Histogram | Phân phối tuổi hành khách |
| 3 | Countplot | Phân phối hạng vé |
| 4 | Boxplot | Giá vé theo hạng vé |
| 5 | Barplot | Tỉ lệ sống sót trung bình theo giới tính |
| 6 | Heatmap | Tương quan giữa các biến số |

## Biểu đồ / Charts (Iris)

| # | Loại | Nội dung |
|---|------|----------|
| 1 | Histogram | Phân phối chiều dài cánh hoa theo loài |
| 2 | Scatterplot | Sepal length vs Sepal width |
| 3 | Boxplot | Đặc trưng theo loài |
| 4 | Heatmap | Tương quan giữa các biến số |

---

## Cấu trúc / Structure

eda-dashboard-python/
├── app.py             # Streamlit app (entry point)
├── requirements.txt
└── README.md

---

## Cài đặt & Chạy / Setup & Run

```bash
git clone https://github.com/LinhAnhNV/eda-dashboard-python.git
cd eda-dashboard-python
pip install -r requirements.txt
streamlit run app.py
```

App sẽ tự mở ở `http://localhost:8501`.

---

## Kết luận / Findings (Titanic)

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
Củ Chi, TP.HCM · 2026