from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    if request.method == "POST":

        subject = request.form.get("subject")
        days = int(request.form.get("days"))
        hours = request.form.get("hours")
        difficulty = request.form.get("difficulty")

        timetable = []

        for i in range(1, days + 1):

            timetable.append({

                "day": f"Day {i}",
                "subject": subject,
                "hours": hours,
                "difficulty": difficulty

            })

        progress = min(days * 10, 100)

        tips = {

            "Easy": "Revise daily for better memory.",
            "Medium": "Practice questions every day.",
            "Hard": "Focus more time on difficult topics."

        }

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        return render_template(

            "result.html",

            timetable=timetable,
            progress=progress,
            tip=tips[difficulty],
            current_time=current_time
        )

    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")