def calculate_total_score(scores):
    return sum(scores.values())

def is_adult(age):
    return age >= 18

def calculate_score(name, age, gender, height, weight, scores):
    # Бізнес-логіка для розрахунку загального рейтингу
    total_score = calculate_total_score(scores)

    adult = is_adult(age)

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height)
    print("Weight:", weight)
    print("Total Score:", total_score)
    print("Adult:", adult)

# Приклад виклику функції
calculate_score("John", 25, "Male", 175, 70, {"score1": 85, "score2": 90, "score3": 75, "score4": 88, "score5": 92})