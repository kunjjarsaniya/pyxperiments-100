# -------------------------------------------------------------
# 📰 Basic Blog using Flask + OOP + File Handling (JSON)
# -------------------------------------------------------------

from flask import Flask, render_template, request, redirect, flash
import json, os

# -------------------------------------------------------------
# 📦 BlogManager Class – Handles data operations
# -------------------------------------------------------------

class BlogManager:
    def __init__(self, filename="blog_data.json"):
        self.filename = filename
        self.posts = []
        self.load_posts()

    def load_posts(self):
        """Load posts from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    self.posts = json.load(f)
            except Exception as e:
                print(f"⚠️ Error loading posts: {e}")
                self.posts = []
        else:
            self.posts = []

    def save_posts(self):
        """Save posts to JSON file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.posts, f, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving posts: {e}")

    def add_post(self, title, content):
        """Add a new blog post."""
        post = {
            "title": title.strip(),
            "content": content.strip()
        }
        if post["title"] and post["content"]:
            self.posts.insert(0, post)
            self.save_posts()
        else:
            raise ValueError("Title and content cannot be empty.")

# -------------------------------------------------------------
# 🚀 Flask Web App Setup
# -------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "supersecret"
blog = BlogManager()

# -------------------------------------------------------------
# 🌐 Routes for Blog Web App
# -------------------------------------------------------------

@app.route('/')
def index():
    return render_template("index.html", posts=blog.posts)

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        try:
            blog.add_post(title, content)
            flash("✅ Post added successfully!", "success")
            return redirect('/')
        except Exception as e:
            flash(str(e), "danger")
    return render_template("create.html")

# -------------------------------------------------------------
# 🏁 Run the Flask Application
# -------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
