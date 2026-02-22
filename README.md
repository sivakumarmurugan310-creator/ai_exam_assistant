# ai_exam_assistant
 AI-Powered Study Planner
An intelligent web-based study planner built using Flask that helps students organize their learning, track performance, and generate practice questions dynamically.

🚀 Features
🔐 User Registration & Login System

📊 Performance Tracking (subject-wise scores)

📚 Predefined Syllabus Management

🧠 AI-Based Study Plan Generation

📝 Automatic Practice Question Generator

🔓 Session Management (Login/Logout)

🛠️ Tech Stack
Backend: Python (Flask)

Database: SQLite

ORM: SQLAlchemy

Frontend: HTML, CSS (Templates)

📂 Project Structure
Code

project/
│
├── app.py                  # Main Flask application
├── models.py              # Database models
├── study_planner.py       # Study plan generator
├── questions_generator.py # Question generator
├── database.db            # SQLite database
│
├── templates/             # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── study_plan.html
│   ├── practice.html
⚙️ Installation & Setup
1️⃣ Clone the repository
Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
Bash

pip install flask flask_sqlalchemy
3️⃣ Run the application
Bash

python app.py
4️⃣ Open in browser
Code

http://127.0.0.1:5000/
🧪 How It Works
Users register and log in

Default syllabus topics are loaded automatically

Dummy performance data is added for demonstration

Study plan is generated based on performance

Practice questions are generated dynamically for each subject


(Add screenshots after running your project)

🔮 Future Enhancements
📱 Mobile App Integration

🤖 AI-Based Risk Prediction

📊 Advanced Analytics Dashboard

🌍 Multi-language Support

⌚ Wearable Device Integration
