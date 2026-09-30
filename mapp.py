from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Tracker</title>
</head>
<body>
    <h1>Task Tracker</h1>

    <form action="/add" method="POST">
        <input name="task" placeholder="Enter a task" required>
        <button>Add</button>
    </form>

    <ul>
    {% for i, task in enumerate(tasks) %}
        <li>
            {% if task.done %}
                <s>{{ task.text }}</s>
            {% else %}
                {{ task.text }}
            {% endif %}

            <form action="/toggle/{{ i }}" method="POST" style="display:inline">
                <button>✓</button>
            </form>

            <form action="/delete/{{ i }}" method="POST" style="display:inline">
                <button>Delete</button>
            </form>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks, enumerate=enumerate)

@app.post("/add")
def add():
    text = request.form["task"].strip()
    if text:
        tasks.append({"text": text, "done": False})
    return redirect("/")

@app.post("/toggle/<int:i>")
def toggle(i):
    tasks[i]["done"] = not tasks[i]["done"]
    return redirect("/")

@app.post("/delete/<int:i>")
def delete(i):
    tasks.pop(i)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)