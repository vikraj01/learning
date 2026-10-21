# The same app, in Python

After this page you'll have the message box written in Python too, and see that Docker treats it exactly the same way.

## Same app, different language

A web app can be written in many languages. This one does exactly what `app.js` does: `/web` shows the form, `/send` saves the message to `data/messages.txt`, and it listens on door 3000.

- **Python**: another programming language, popular because it reads almost like English.
- **Flask**: a small helper package for Python servers. It's Python's version of Express.
- **pip**: Python's tool for downloading packages, like npm.

## Try it: make the app

Make a new folder next to `message-box` (not inside it):

```bash
mkdir message-box-python
cd message-box-python
```

Make a file called `app.py` and type this in:

```python
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
```

## Side by side

| JavaScript (`app.js`) | Python (`app.py`) | What it does |
| --- | --- | --- |
| `require("express")` | `from flask import Flask, request` | Load the helper package. |
| `` const form = `...` `` | `form = """..."""` | The HTML form, as text. |
| `app.get("/web", ...)` | `@app.get("/web")` | When the browser asks for `/web`, send the form. |
| `app.post("/send", ...)` | `@app.post("/send")` | When the form is sent, save the message. |
| `fs.appendFileSync(...)` | `open(..., "a")` then `file.write(...)` | Add a line to the end of the file. `"a"` means **append**. |
| `app.listen(3000, ...)` | `app.run(host="0.0.0.0", port=3000)` | Start the server on door 3000. |

In Python, spaces at the start of a line matter. The lines inside `def web():` and `def send():` must be pushed in by 4 spaces.

`host="0.0.0.0"` means "answer anyone who knocks, not only this machine". Without it, the app would work on your laptop but not from inside a container. (Express does this by default.)

## Try it: run it on your laptop

Python keeps packages for a project in a **virtual environment**: a private folder of packages, so projects don't get in each other's way. Make one and install Flask into it:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
```

The last line should end with something like:

```
Successfully installed ... flask-3.1.3 ...
```

Run it:

```bash
python app.py
```

```
Message box is running on http://localhost:3000/web
 * Serving Flask app 'app'
```

You'll also see a red **WARNING** that this is a development server. That's fine for learning.

Open `http://localhost:3000/web` and send a message, then check `cat data/messages.txt` in a second terminal. Press `Ctrl + C` to stop the server.

## Try it: the Dockerfile

Still **5 lines**, and the same shape as before:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN pip install flask
COPY app.py .
CMD ["python", "app.py"]
```

| Line | In plain words |
| --- | --- |
| `FROM python:3.12-slim` | Start from an image that already has Python. |
| `WORKDIR /app` | Work in `/app` inside the image. |
| `RUN pip install flask` | Download Flask into the image. |
| `COPY app.py .` | Copy `app.py` into `/app`. |
| `CMD ["python", "app.py"]` | When a container starts, run the app. |

Only the language-specific words changed: `node` became `python`, `npm install express` became `pip install flask`.

Build and run it (make sure the JavaScript `msg` container is removed first, since both want door 3000):

```bash
docker rm -f msg
docker build -t message-box-python .
docker run -d --name msg -p 3000:3000 message-box-python
```

Open `http://localhost:3000/web`. Same page, now served by Python.

## Everything else is the same

The app still writes to `/app/data` and still uses door 3000. So every command from pages 3 to 6 works as it is. Only the image name at the end changes:

```bash
docker exec msg cat data/messages.txt
docker run -d --name msg -p 3000:3000 -v "$(pwd)/data:/app/data" message-box-python
docker run -d --name msg -p 3000:3000 -v messages:/app/data message-box-python
```

Docker doesn't care what language is inside the container. It only needs the recipe.

## Check yourself

1. Which two Dockerfile lines changed between the JavaScript and Python versions? Why?
2. What is Flask, in one sentence?
3. What would happen if you left out `host="0.0.0.0"`?

## Clean up

```bash
docker rm -f msg
docker rmi message-box-python
deactivate
```

`deactivate` leaves the virtual environment.
