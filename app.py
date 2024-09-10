from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the feedback form
form_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Feedback Form</title>
  </head>
  <body>
    <h1>Feedback Form</h1>
    <form method="POST">
      <label for="name">Name:</label><br>
      <input type="text" id="name" name="name" required><br><br>
      
      <label for="email">Email:</label><br>
      <input type="email" id="email" name="email" required><br><br>
      
      <label for="feedback">Your Feedback:</label><br>
      <textarea id="feedback" name="feedback" rows="4" cols="50" required></textarea><br><br>
      
      <label for="rating">Rate your experience (1-5):</label><br>
      <input type="number" id="rating" name="rating" min="1" max="5" required><br><br>
      
      <input type="submit" value="Submit Feedback">
    </form>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        feedback = request.form.get('feedback')
        rating = request.form.get('rating')

        print(f"Feedback received from {name} ({email}):")
        print(f"Rating: {rating}")
        print(f"Feedback: {feedback}")

        return "Thank you for your feedback!"

    return render_template_string(form_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

