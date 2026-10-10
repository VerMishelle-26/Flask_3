from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = {}

@app.route("/")
def index():
    """Главная страница блога."""
    return render_template("index.html")

@app.route("/notes", methods=["GET", "POST"])
def notes_page():
    """Дневник программиста."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        text = request.form.get("text", "").strip()
        if title and text:
            notes[title] = text
        return redirect(url_for("notes_page"))

    return render_template("notes.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)