# Student Performance Analytics System

## 1. Project Overview

The Student Performance Analytics System is a Python-based project that analyzes student marks and attendance. It calculates total marks, average marks, grades, and pass/fail results and identifies top-performing students.

## 2. Objectives

* Analyze student academic performance.
* Calculate total and average marks.
* Assign grades based on average marks.
* Determine pass/fail status using marks and attendance.
* Perform subject-wise analysis.
* Identify the top three performers.

## 3. Technologies Used

* Python
* NumPy
* Pandas

## 4. Dataset

The project uses `students.csv`, which contains 20 student records.

Dataset columns:

* Student_ID
* Name
* Department
* Maths
* Science
* English
* Attendance

## 5. Project Files

* `main.py` — Main program that loads the dataset and runs the analysis.
* `functions.py` — Functions for calculating results and displaying summaries.
* `students.csv` — Input dataset containing student details, marks, and attendance.
* `student_results.csv` — Generated output containing calculated results.
* `README.md` — Project description and instructions.

## 6. Features

* Calculates total marks and average marks.
* Assigns grades based on average marks.
* Determines pass/fail status.
* Displays class performance statistics.
* Displays grade distribution.
* Calculates subject-wise averages, highest marks, and lowest marks.
* Displays the top three performers.
* Saves processed results to `student_results.csv`.

## 7. Grade Criteria

* A: Average marks of 90 or above.
* B: Average marks of 75 to below 90.
* C: Average marks of 60 to below 75.
* D: Average marks of 35 to below 60.
* F: Average marks below 35.

## 8. Pass/Fail Criteria

A student passes when every subject mark is at least 35 and attendance is at least 75%. Otherwise, the student fails.

## 9. How to Run

1. Install Python.
2. Install the required libraries:
   `pip install pandas numpy`
3. Keep `main.py`, `functions.py`, and `students.csv` in the same folder.
4. Open a terminal in the project folder.
5. Run:
   `python main.py`

The program displays the analysis and saves the results in `student_results.csv`.

## 10. Expected Output

The program displays:

* Individual student results
* Total and average marks
* Grades and pass/fail status
* Class statistics
* Grade distribution
* Subject-wise performance
* Top three performers

## 11. Conclusion

The Student Performance Analytics System demonstrates how Python, NumPy, and Pandas can be used to organize, analyze, and summarize student academic data efficiently.
