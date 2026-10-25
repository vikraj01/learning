Two different web servers, both wanting port 80. Can they run together?

- **nginx** shows a page that says *Welcome to nginx!*
- **httpd** (also called Apache, another web server) shows a page that says *It works!*

## Your job

Run both at the same time:

| Container | Image | Opens on |
| --- | --- | --- |
| `site-one` | `nginx` | http://localhost:8091 |
| `site-two` | `httpd` | http://localhost:8092 |

## Think about it

Both programs listen on port **80** inside their container. That's fine: every container is its own little computer, with its own doors. Only the doors on **your laptop** have to be different.

> `-p 8091:80` means: *the laptop's door 8091 leads to the container's door 80.*
