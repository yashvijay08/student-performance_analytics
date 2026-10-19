# Student Performance Analytics 📊

A beginner-friendly Python data analytics dashboard that explores fictional student marks and attendance records.

**Built with:** Python · Pandas · Matplotlib · Streamlit

## Features

- View student records in an interactive table
- Filter by class and minimum attendance
- Search by student name or ID
- Calculate total marks, percentage, and grade
- Visualize subject averages and grade distribution
- Explore attendance versus percentage
- Download filtered records as a CSV report
- Show quick insights about subject averages and top performance

## Preview

The dashboard includes summary metrics, a searchable data table, charts, and filters. After running it locally, you can add your own screenshot to `screenshots/` and embed it here:

```markdown
![Dashboard screenshot](screenshots/dashboard.png)
```

## Project structure

```text
student-performance-analytics/
├── data/
│   └── students.csv
├── src/
│   ├── __init__.py
│   └── analytics.py
├── screenshots/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally

### 1. Install Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/). During installation on Windows, select **Add Python to PATH**.

### 2. Download or clone this repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-analytics
```

If you downloaded the ZIP from this project package, extract it and open the extracted folder in VS Code.

### 3. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the dashboard

```bash
python -m streamlit run main.py
```

Streamlit will print a local URL, usually `http://localhost:8501`, which you can open in your browser.

## Dataset

`data/students.csv` contains fictional example records. The expected columns are:

- `student_id`
- `name`
- `class`
- `maths`
- `science`
- `english`
- `attendance`

Marks and attendance must be numbers between 0 and 100. Do not publish real student personal information.

## Grade calculation

| Percentage | Grade |
|---:|:---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| Below 60 | F |

These are illustrative rules for this project, not official school grading standards.

## Learning outcomes

- Reading and validating CSV data
- Using Python functions and modules
- Basic data analysis with Pandas
- Creating charts with Matplotlib
- Building an interactive dashboard with Streamlit
- Organizing a small GitHub project

## Limitations

- The sample dataset is fictional and small.
- Grades use the simple rules defined above.
- The dashboard is for learning and demonstration, not official academic evaluation.

## Future improvements

- Upload a custom CSV from the dashboard
- Add more subjects and configurable grade bands
- Export a PDF report
- Add unit tests
- Deploy the dashboard publicly

## Author

**Vijay Kumar**  
BS Computer Science and Data Analytics, IIT Patna

This is an educational portfolio project. Update this section with your GitHub profile link after publishing the repository.
