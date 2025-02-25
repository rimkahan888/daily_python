from flask import Flask, jsonify, render_template_string
import random
import datetime

app = Flask(__name__)

# List of daily learning tips
daily_tips = [
    "Practice good coding habits every day.",
    "Keep learning and exploring new technologies.",
    "Don't fear debugging—it's a step toward mastering your craft.",
    "Read the documentation thoroughly to understand best practices.",
    "Use version control to track your progress and collaborate.",
    "Break problems into smaller parts and tackle them one at a time.",
    "Stay curious: every challenge is an opportunity to learn.",
    "Test your code frequently to catch issues early.",
    "Refactor often to keep your code clean and efficient.",
    "Ask questions and learn from your peers."
]

def get_daily_tip():
    """
    Returns a tip based on the current day of the year.
    This ensures a different tip each day, rotating through the list.
    """
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    index = day_of_year % len(daily_tips)
    return daily_tips[index]

@app.route('/')
def index():
    """
    Renders a simple HTML page displaying the daily learning tip.
    """
    tip = get_daily_tip()
    html_content = f"""
    <html>
      <head>
        <title>Daily Learning Tip</title>
      </head>
      <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h1>Daily Learning Tip</h1>
        <p style="font-size: 1.2em;">{tip}</p>
      </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/api/daily_tip')
def daily_tip_api():
    """
    Returns the daily learning tip as a JSON object.
    """
    tip = get_daily_tip()
    return jsonify({"daily_tip": tip})

if __name__ == '__main__':
    app.run(debug=True)
