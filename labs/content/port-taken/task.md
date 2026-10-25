Someone already started a container called `squatter`, and it holds port **8093** on your laptop.

## Your job

1. First, **try** to start a website called `shop` on port 8093:

   ```
   docker run -d --name shop -p 8093:80 nginx
   ```

2. Read the error carefully. What does it say?
3. You're **not allowed** to stop `squatter`. Make `shop` open on **http://localhost:8094** instead.

## Two things to notice

- Two programs can never use the **same door** on your laptop at the same time.
- A failed `docker run` can still leave a container behind, with the name you asked for. `docker ps -a` shows **all** containers, stopped ones too.
