The folder `site/` on the left holds a small web page: `site/index.html`.

nginx shows whatever files are in its folder **`/usr/share/nginx/html`** inside the container. A **bind mount** puts a folder from **your laptop** there. Then nginx shows **your** files, live.

## Your job

1. Run nginx as `live-site`, opening on **http://localhost:8100**, with the lab's `site` folder bind-mounted onto `/usr/share/nginx/html`.
2. Open the page. You should see **Hello from my laptop**.
3. Change the heading in `site/index.html` (your name, anything), save, and **reload** the browser.

## The new part

```
-v "$(pwd)/site":/usr/share/nginx/html
   ─────┬──────  ──────────┬──────────
   folder on your laptop   folder inside the container
```

`$(pwd)` turns into the full path of the folder you're in, so you don't have to type it.

> A volume is storage Docker manages. A bind mount is **your own folder**, shared with the container, and changes go both ways instantly.
