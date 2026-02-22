from models import Performance, Syllabus

def generate_study_plan(user_id):
    syllabus = Syllabus.query.all()
    performance = Performance.query.filter_by(user_id=user_id).all()
    plan = []
    for topic in syllabus:
        score = next((p.score for p in performance if p.topic == topic.topic), None)
        if score is None or score < 50:
            plan.append(f"Focus on {topic.topic} today (weak topic)")
        else:
            plan.append(f"Review {topic.topic} today (strong topic)")
    return plan
