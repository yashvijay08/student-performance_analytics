from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from src.analytics import load_student_data, calculate_student_metrics, get_subject_averages

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "students.csv"

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Student Performance Analytics")
st.caption("A beginner-friendly Python data analytics project using sample student records.")

@st.cache_data
def get_data(path: str):
    return load_student_data(path)

try:
    raw_df = get_data(str(DATA_FILE))
    df = calculate_student_metrics(raw_df)
except Exception as exc:
    st.error(f"Could not load the dataset: {exc}")
    st.info("Check that data/students.csv exists and follows the expected column format.")
    st.stop()

with st.sidebar:
    st.header("Filters")
    all_classes = ["All"] + sorted(df["class"].dropna().astype(str).unique().tolist())
    selected_class = st.selectbox("Class / Section", all_classes)
    min_attendance = st.slider("Minimum attendance (%)", 0, 100, 0, 5)
    st.markdown("---")
    st.caption("This repository uses fictional sample data. Do not upload private student records.")

filtered = df.copy()
if selected_class != "All":
    filtered = filtered[filtered["class"].astype(str) == selected_class]
filtered = filtered[filtered["attendance"] >= min_attendance]

if filtered.empty:
    st.warning("No students match these filters. Try changing the filters in the sidebar.")
    st.stop()

average_percentage = filtered["percentage"].mean()
average_attendance = filtered["attendance"].mean()
top_student = filtered.sort_values("percentage", ascending=False).iloc[0]
students_count = len(filtered)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", f"{students_count}")
c2.metric("Average percentage", f"{average_percentage:.1f}%")
c3.metric("Average attendance", f"{average_attendance:.1f}%")
c4.metric("Top score", f"{top_student['percentage']:.1f}%", help=str(top_student["name"]))

st.subheader("Student records")
search = st.text_input("Search by student name or ID", placeholder="e.g. Asha or S1001")
shown = filtered.copy()
if search.strip():
    needle = search.strip().lower()
    shown = shown[
        shown["name"].astype(str).str.lower().str.contains(needle, na=False)
        | shown["student_id"].astype(str).str.lower().str.contains(needle, na=False)
    ]

display_cols = ["student_id", "name", "class", "maths", "science", "english", "attendance", "total", "percentage", "grade"]
st.dataframe(
    shown[display_cols].rename(columns={
        "student_id": "Student ID",
        "name": "Name",
        "class": "Class",
        "maths": "Maths",
        "science": "Science",
        "english": "English",
        "attendance": "Attendance (%)",
        "total": "Total (out of 300)",
        "percentage": "Percentage (%)",
        "grade": "Grade",
    }),
    use_container_width=True,
    hide_index=True,
)

csv_bytes = shown[display_cols].to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download filtered data as CSV", data=csv_bytes,
                   file_name="student_performance_report.csv", mime="text/csv")

left, right = st.columns(2)
with left:
    st.subheader("Average marks by subject")
    subject_avg = get_subject_averages(filtered)
    fig, ax = plt.subplots()
    ax.bar(subject_avg.index, subject_avg.values)
    ax.set_ylabel("Average marks (out of 100)")
    ax.set_ylim(0, 100)
    ax.set_title("Subject-wise class average")
    ax.grid(axis="y", alpha=0.25)
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Grade distribution")
    grade_order = ["A", "B", "C", "D", "F"]
    grade_counts = filtered["grade"].value_counts().reindex(grade_order, fill_value=0)
    fig, ax = plt.subplots()
    ax.bar(grade_counts.index, grade_counts.values)
    ax.set_ylabel("Number of students")
    ax.set_title("Students by grade")
    ax.grid(axis="y", alpha=0.25)
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Attendance vs percentage")
fig, ax = plt.subplots()
ax.scatter(filtered["attendance"], filtered["percentage"])
ax.set_xlabel("Attendance (%)")
ax.set_ylabel("Percentage (%)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("Attendance and academic performance")
ax.grid(alpha=0.25)
st.pyplot(fig)
plt.close(fig)

st.subheader("Quick insights")
subject_avg = get_subject_averages(filtered)
best_subject = subject_avg.idxmax()
needs_attention = subject_avg.idxmin()
st.markdown(
    f"- **Highest average subject:** {best_subject} ({subject_avg[best_subject]:.1f}/100)\n"
    f"- **Lowest average subject:** {needs_attention} ({subject_avg[needs_attention]:.1f}/100)\n"
    f"- **Highest-performing student in the filtered group:** {top_student['name']} ({top_student['percentage']:.1f}%)"
)

st.markdown("---")
st.caption("Built with Python, Pandas, Matplotlib, and Streamlit • Educational project with fictional data.")
