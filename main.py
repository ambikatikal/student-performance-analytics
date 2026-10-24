import pandas as pd
from functions import calculate_student_results, display_summary

def main():
    try:
        df = pd.read_csv("students.csv")
        df = calculate_student_results(df)
        display_summary(df)
        df.to_csv("student_results.csv", index=False)
        print("Results saved to student_results.csv")
    except FileNotFoundError:
        print("Error: students.csv was not found.")
    except (ValueError, KeyError) as error:
        print("Error processing student data:", error)

if __name__ == "__main__":
    main()