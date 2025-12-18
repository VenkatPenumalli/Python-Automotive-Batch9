def StdScore(marks):
    Total_Score = sum(marks)
    Percentage = ((Total_Score/500)*100)
    if Percentage >= 90:
        Grade = "A,Pass"
    elif Percentage >= 75:
        Grade = "B,Pass"
    elif Percentage >= 60:
        Grade = "C,Pass" 
    elif Percentage >= 40:
        Grade = "D,Pass"
    else:
        Grade = "Fail"
    print(f"Total Score :: {Total_Score}\n",
          f"Percentage :: {Percentage}\n",
          f"Grade = {Grade}\n")

marks = list(map(int,input("Enter the marks of 5 Subjects:: ").split()))
StdScore(marks)