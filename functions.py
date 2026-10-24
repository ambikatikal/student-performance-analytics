import numpy as np
import pandas as pd


def calculate_student_results(df):
    subjects = ["Maths", "Science", "English"]

    df["Total_Marks"] = df[subjects].sum(axis=1)
    df["Average_Marks"] = np.mean(df[subjects].to_numpy(), axis=1)

    def calculate_grade(average):
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 35:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Average_Marks"].apply(calculate_grade)

    df["Result"] = np.where(
        (df[subjects].min(axis=1) >= 35) & (df["Attendance"] >= 75),
        "Pass",
        "Fail"
    )

    return df


def display_summary(df):
    subjects = ["Maths", "Science", "English"]

    print("\n========== STUDENT PERFORMANCE ANALYTICS ==========")
    print("\nSTUDENT RESULTS")
    print(df.to_string(index=False))

    print("\nCLASS STATISTICS")
    print("Total Students:", len(df))
    print("Class Average:", round(df["Average_Marks"].mean(), 2))
    print("Highest Average:", round(df["Average_Marks"].max(), 2))
    print("Lowest Average:", round(df["Average_Marks"].min(), 2))

    print("\nPASS/FAIL SUMMARY")
    print(df["Result"].value_counts().to_string())

    print("\nGRADE SUMMARY")
    print(df["Grade"].value_counts().sort_index().to_string())

    print("\nSUBJECT-WISE PERFORMANCE")
    for subject in subjects:
        print(
            subject,
            "- Average:", round(df[subject].mean(), 2),
            "| Highest:", df[subject].max(),
            "| Lowest:", df[subject].min()
        )

    print("\nTOP 3 PERFORMERS")
    top_students = df.nlargest(3, "Average_Marks")
    print(
        top_students[
            ["Student_ID", "Name", "Average_Marks", "Grade"]
        ].to_string(index=False)
    )