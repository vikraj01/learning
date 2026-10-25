Docker builds an image **one line at a time**, and it remembers each step (this memory is the **build cache**). If nothing a step uses has changed, Docker reuses the old result instead of doing it again. The output says `CACHED`.

But as soon as **one** step has to run again, **every step after it** runs again too.

## The problem

Look at the `Dockerfile` on the left:

```
COPY . .            ← copies everything, app.js too
RUN npm install     ← slow: downloads all the packages
```

Change one letter in `app.js`, and `COPY . .` changes. So `npm install` runs again, every time, even though the packages didn't change.

## Try it first

```
docker build -t fast-box .
```

Now change the message in `app.js`, save, and build again. Watch the `npm install` step. It runs again.

## Your job

Reorder the Dockerfile so `npm install` only runs again when **`package.json`** changes. Build `fast-box` again, change `app.js`, build once more, and look for `CACHED`.

> Things that change rarely go at the top. Things that change often go at the bottom.
