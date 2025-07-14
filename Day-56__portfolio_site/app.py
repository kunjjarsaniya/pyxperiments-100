from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

class PortfolioApp:
    def __init__(self, app, data_path="data/projects.json"):
        self.app = app
        self.data_path = data_path
        self.configure_routes()

    def configure_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                title = request.form.get("title")
                description = request.form.get("description")
                image = request.form.get("image")
                link = request.form.get("link")

                if not title or not description or not image or not link:
                    flash("All fields are required!", "error")
                    return redirect(url_for("home"))

                new_project = {
                    "title": title,
                    "description": description,
                    "image": image,
                    "link": link
                }

                success = self.save_project(new_project)
                if success:
                    flash("Project added successfully!", "success")
                    return redirect(url_for("home"))
                else:
                    flash("Failed to save project. Please try again.", "error")
                    return redirect(url_for("home"))

            projects = self.load_projects()
            return render_template("index.html", projects=projects, title="Home")

        @self.app.route("/about")
        def about():
            return render_template("about.html", title="About")

    def load_projects(self):
        if not os.path.exists(self.data_path):
            return []
        try:
            with open(self.data_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading projects: {e}")
            return []

    def save_project(self, project):
        projects = self.load_projects()
        projects.append(project)
        try:
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            with open(self.data_path, "w", encoding="utf-8") as file:
                json.dump(projects, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving project: {e}")
            return False

if __name__ == "__main__":
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.secret_key = "supersecretkey"
    portfolio = PortfolioApp(app)
    app.run(debug=True)
