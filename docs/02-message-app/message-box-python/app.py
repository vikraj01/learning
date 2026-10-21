import os
from flask import Flask, request

app = Flask(__name__)

form = """
<!doctype html>
<html>
  <body>
    <h1>Message box</h1>
    <form action="/send" method="post">
      <input name="message" placeholder="Write something">
      <button type="submit">Send</button>
    </form>
  </body>
</html>
"""


@app.get("/web")
def web():
    return form


@app.post("/send")
def send():
    os.makedirs("data", exist_ok=True)
    with open("data/messages.txt", "a") as file:
        file.write(request.form["message"] + "\n")
    return 'Saved! <a href="/web">Write another</a>'


print("Message box is running on http://localhost:3000/web")
app.run(host="0.0.0.0", port=3000)
