# 🤖 Phân Tích & Khuyến Nghị Ứng Dụng AI Agent Trong Khoa Học Máy Tính (CS/IT)

Một ứng dụng dữ liệu tương tác (Interactive Dashboard) được xây dựng bằng Streamlit nhằm phân tích và đề xuất các tác vụ trong lĩnh vực Khoa học Máy tính nên được tự động hóa bởi AI Agent. 

Dự án sử dụng phương pháp đối chiếu chéo giữa **mong muốn của người lao động** và **năng lực thực tế của AI (đánh giá bởi chuyên gia)** để tìm ra "điểm chạm lý tưởng" trong việc chuyển giao công việc.

---

## 🎯 Mục Tiêu Dự Án
* **Khai thác dữ liệu O*NET:** Phân tích các đầu việc (Tasks) đặc thù của nhóm ngành IT/CS.
* **Đo lường mức độ khả thi (Agent Feasibility Score):** Xây dựng công thức tính toán độ phù hợp của từng tác vụ dựa trên khát khao tự động hóa của con người và giới hạn năng lực công nghệ.
* **Hỗ trợ ra quyết định:** Cung cấp các khuyến nghị chiến lược (Top 3 AI Agents) kèm theo cảnh báo về mức độ kiểm soát của con người (Human Agency).

---

## 📊 Giao Diện Ứng Dụng (Live Demo)

### 1. Ma Trận Cơ Hội (Opportunity Matrix)
Biểu đồ phân tán (Scatter Plot) giúp nhận diện nhanh các tác vụ nằm ở góc "Lý tưởng" (Năng lực AI cao & Con người mong muốn cao).

<img width="1366" height="768" alt="Screenshot 2026-06-25 131658" src="https://github.com/user-attachments/assets/b2113ce6-3272-4309-baea-b469a60e69e3" />


### 2. Bảng Dữ Liệu Phân Tích (Data Insights)
Hiển thị chi tiết các thông số đầu vào sau quá trình làm sạch và gộp dữ liệu (ETL).



### 3. Khuyến Nghị Trí Tuệ Nhân Tạo (AI Recommendations)
Đề xuất các AI Agent tiềm năng nhất dưới dạng Background Agent hoặc Human-in-the-loop dựa trên chỉ số nhạy cảm của tác vụ.

<img width="1366" height="768" alt="Screenshot 2026-06-25 131809" src="https://github.com/user-attachments/assets/73978e62-d5f3-4912-89e6-86d20c6db341" />


---

## 🛠️ Công Nghệ & Thư Viện Sử Dụng
Dự án được xây dựng hoàn toàn bằng ngôn ngữ **Python**, ứng dụng các thư viện chuẩn trong Khoa học dữ liệu:
* `pandas`: Xử lý, làm sạch và tổng hợp dữ liệu từ 4 tập file CSV độc lập.
* `plotly`: Trực quan hóa dữ liệu bằng các biểu đồ tương tác cao.
* `streamlit`: Thiết kế giao diện người dùng (UI) và triển khai ứng dụng Web.

---

## ⚙️ Hướng Dẫn Cài Đặt & Khởi Chạy
Để chạy ứng dụng trên máy tính cá nhân (Local Machine), vui lòng làm theo các bước sau:

**Bước 1: Clone kho lưu trữ này về máy**
```bash
git clone [https://github.com/Tên-Tài-Khoản-Của-Bạn/Tên-Repo-Của-Bạn.git](https://github.com/Tên-Tài-Khoản-Của-Bạn/Tên-Repo-Của-Bạn.git)
cd Tên-Repo-Của-Bạn
