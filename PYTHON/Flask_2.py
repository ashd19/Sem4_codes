from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# A simple in-memory database for demonstration purposes
users = {}

@app.route('/')
def index():
    return render_template_string("""
        <h1>Welcome to the Flask App</h1>
        <p><a href="{{ url_for('show_form') }}">Submit your name</a></p>
    """)

@app.route("/form", methods=["GET", "POST"])
def show_form():
    if request.method == "POST":
        # Handling form submission
        name = request.form.get("name")
        email = request.form.get("email")
        if name and email:
            # Storing the submitted data (as an example)
            users[name] = email
            return redirect(url_for('thank_you', name=name))
        else:
            return "Please provide both name and email!", 400
    
    # Returning the HTML form for GET request
    return render_template_string("""
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <input type="submit" value="Submit">
        </form>
    """)

@app.route("/thank_you/<name>")
def thank_you(name):
    if name in users:
        return f"Thank you, {name}! Your email is {users[name]}"
    return "User not found!", 404

if __name__ == "__main__":
    app.run(debug=True)
