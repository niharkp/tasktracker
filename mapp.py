from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return jsonify({"Name": "Naga_Nihar_KP",
        
        "goal": "Cloud & DevOps Engineer",
        "skills": ["Python", "Docker", "AWS", "Git", "HTML/CSS"],
       
       
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"deleted": task_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)