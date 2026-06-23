import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Cấu hình trang
st.set_page_config(
    page_title="Báo cáo ứng dụng AI Agent trong CS",
    page_icon="🤖",
    layout="wide",
)

st.title("📊 Phân Tích & Khuyến Nghị Ứng Dụng AI Agent trong Khoa Học Máy Tính")
st.markdown(
    "*Báo cáo phân tích mức độ khả thi khi chuyển giao các tác vụ IT cho AI Agent*"
)


# 2. Đọc file dữ liệu đã xử lý từ Colab
@st.cache_data
def load_data():
    return pd.read_csv("cs_tasks_analyzed.csv")


df = load_data()

# 3. Thanh điều hướng bên trái (Sidebar)
st.sidebar.header("Bộ lọc phân tích")
job_list = ["Tất cả ngành CS"] + list(df["Occupation (O*NET-SOC Title)"].unique())
selected_job = st.sidebar.selectbox("Chọn một vị trí cụ thể:", job_list)

if selected_job != "Tất cả ngành CS":
    df_filtered = df[df["Occupation (O*NET-SOC Title)"] == selected_job]
else:
    df_filtered = df

# 4. CHIA 3 TABS KHOA HỌC
tab1, tab2, tab3 = st.tabs(
    ["📌 Ma trận cơ hội", "📋 Dữ liệu chi tiết", "💡 Khuyến nghị chiến lược"]
)

with tab1:
    st.subheader(
        "Ma Trận Tự Động Hóa (Automation Opportunity Matrix)"
    )
    st.write(
        "Góc trên bên phải (Quadrant 1) là vùng **Lý tưởng**: Nơi con người rất muốn thoát khỏi công việc đó, và AI đã đủ thông minh để đảm nhận."
    )

    fig = px.scatter(
        df_filtered,
        x="Automation Capacity Rating",
        y="Automation Desire Rating",
        size="Agent_Feasibility_Score",
        color="Human Agency Scale Rating",
        hover_name="Task",
        hover_data=["Occupation (O*NET-SOC Title)"],
        labels={
            "Automation Capacity Rating": "Điểm năng lực của AI (1-5)",
            "Automation Desire Rating": "Mong muốn tự động hóa của KS (1-5)",
            "Human Agency Scale Rating": "Yêu cầu kiểm soát của con người",
        },
    )

    # Vẽ 2 đường ngắm trung bình ở mốc 3.0
    fig.add_vline(
        x=3.0, line_dash="dash", line_color="red", annotation_text="Năng lực TB"
    )
    fig.add_hline(
        y=3.0,
        line_dash="dash",
        line_color="red",
        annotation_text="Mong muốn TB",
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader(f"Danh sách tác vụ: {selected_job}")
    st.dataframe(
        df_filtered[
            [
                "Occupation (O*NET-SOC Title)",
                "Task",
                "Automation Desire Rating",
                "Automation Capacity Rating",
                "Human Agency Scale Rating",
                "Agent_Feasibility_Score",
            ]
        ],
        use_container_width=True,
    )

with tab3:
    st.subheader("🚀 Đề xuất Top 3 AI Agent nên được phát triển trước")

    # Lấy 3 tác vụ có điểm khả thi cao nhất
    top_3 = df_filtered.sort_values(
        by="Agent_Feasibility_Score", ascending=False
    ).head(3)

    for idx, row in top_3.iterrows():
        with st.expander(
            f"⚡ ĐỀ XUẤT #{idx+1}: {row['Task'][:65]}... (Điểm: {row['Agent_Feasibility_Score']}/5.0)"
        ):
            st.markdown(f"**Vị trí:** `{row['Occupation (O*NET-SOC Title)']}`")
            st.markdown(f"**Chi tiết tác vụ:** *{row['Task']}*")

            c1, c2, c3 = st.columns(3)
            c1.metric(
                "Khao khát của con người",
                f"{row['Automation Desire Rating']}/5.0",
            )
            c2.metric("Chuyên gia AI đánh giá", f"{row['Automation Capacity Rating']}/5.0")
            c3.metric(
                "Độ nhạy cảm (Agency)", f"{row['Human Agency Scale Rating']}/5.0"
            )

            st.info(
                "**Phân tích AI Agent:** Tác vụ này có tính lặp lại cao. Nên thiết lập **Autonomous background Agent** (Agent chạy ngầm) tự động kích hoạt khi có trigger, con người chỉ đóng vai trò 'Human-in-the-loop' để bấm nút Approve cuối cùng."
            )