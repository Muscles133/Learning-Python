import math



student_results = {
    "English": {"Dan": 80, "Harry": 70, "Jess": 95},
    "Math": {"Dan": 60, "Harry": 90, "Jess": 85},
    "Art": {"Dan": 70, "Harry": 70, "Jess": 75},
    "Science": {"Dan": 75, "Harry": 85, "Jess": 95},
    "History": {"Dan": 85, "Harry": 80, "Jess": 90}
}

# First, let's create empty sets for each student
dan_scores = set()
harry_scores = set()
jess_scores = set()

# Now, let's populate these sets with scores from all subjects
for subject_scores in student_results.values():
    dan_scores.add(subject_scores["Dan"])
    harry_scores.add(subject_scores["Harry"])
    jess_scores.add(subject_scores["Jess"])

# If you want to have all scores in one set, you can do:
all_scores = set()
for subject_scores in student_results.values():
    all_scores.update(subject_scores.values())

print(f"Unique scores: {all_scores}")



def grade_convert(score):
    
        if  score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"