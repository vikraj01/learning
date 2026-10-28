# A ready-made app: WordPress, with no code at all

After this page you'll be able to run a real app other people built (a blog, its database, and a tool to look inside the database) from one `compose.yaml`, by reading the image's instructions and filling in its settings.

## Furniture from a shop

So far you built every app yourself: you wrote the code, then a Dockerfile, then `build:`. That's like making a table in your own workshop.

Most of the time at work, you don't build the parts. You take **ready-made images** someone else made (like `postgres` in section 7), the way you buy a table from a shop. Your job is to read the instructions on the box and put the parts together. In Compose that means: only `image:` lines, no `build:`, and the right settings.

## The app: a blog

**WordPress** is the program behind a huge number of websites and blogs. It needs a database to keep the posts. It uses **MySQL** (say "my-S-Q-L"), another database, like Postgres.

We'll add a third part: **phpMyAdmin**, a web page for looking inside a MySQL database (tables, rows), so you can see where your blog post really lives.

| Service | Image | Does | Door on your laptop |
| --- | --- | --- | --- |
| `wordpress` | `wordpress:7-apache` | the blog | 8080 |
| `db` | `mysql:8.4` | keeps the posts | none: private |
| `phpmyadmin` | `phpmyadmin:5` | look inside the database | 8081 |

## Where do the settings come from?

Every official image has a page on **Docker Hub** (hub.docker.com, the shop) that lists the environment variables it understands. You don't guess them; you read them there. For example:

- The **mysql** page says: set `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD` and `MYSQL_ROOT_PASSWORD`, and on the first start it makes that database and that user.
- The **wordpress** page says: tell me where the database is with `WORDPRESS_DB_HOST`, and how to log in with `WORDPRESS_DB_USER`, `WORDPRESS_DB_PASSWORD`, `WORDPRESS_DB_NAME`.
- The **phpmyadmin** page says: `PMA_HOST` is the database to connect to.

The two sides have to match: the user and password MySQL makes are the ones WordPress logs in with. Same idea as `POSTGRES_PASSWORD` and `DB_PASSWORD` on the last page, so we use `.env` again.

## The files

Make a folder called `wordpress`, and in it a file called `.env`:

```
DB_USER=blog
DB_PASSWORD=secret
DB_NAME=blog
DB_ROOT_PASSWORD=rootsecret
```

`DB_ROOT_PASSWORD` is the password of MySQL's **root** user, the all-powerful admin. MySQL insists on having one.

And `compose.yaml`:

```yaml
name: blog

services:
  wordpress:
    image: wordpress:7-apache
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: ${DB_USER}
      WORDPRESS_DB_PASSWORD: ${DB_PASSWORD}
      WORDPRESS_DB_NAME: ${DB_NAME}
    volumes:
      - site:/var/www/html
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: mysql:8.4
    environment:
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "127.0.0.1"]
      interval: 5s
      retries: 20
    restart: unless-stopped

  phpmyadmin:
    image: phpmyadmin:5
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
    depends_on:
      - db

volumes:
  site:
  db-data:
```

No folders, no Dockerfiles, no code. That's the whole app.

## What's worth noticing

- **`WORDPRESS_DB_HOST: db`**: the service name again. WordPress finds MySQL by the name `db` on the network Compose made (`blog_default`).
- **Two volumes**: `db-data` keeps the database (posts, users). `site` keeps WordPress's own files (`/var/www/html`): pictures you upload, themes, plugins. Lose either one and part of your blog is gone.
- **The healthcheck** uses `mysqladmin ping`, a tool that comes with MySQL and answers "mysqld is alive" when the database is ready. MySQL takes a while on its first start (it sets everything up), so we give it 20 tries, 5 seconds apart.
- **`db` has no `ports:`**. Only `wordpress` and `phpmyadmin` reach it, from inside the network. Same idea as the notes app's `db`.
- **No `restart:` on `phpmyadmin`**: it's a tool you open sometimes, not part of the blog, so if it stops, it can stay stopped.

## Try it: start the blog

From the `wordpress` folder:

```bash
docker compose up -d
```

No `--build`: there's nothing to build. Compose **pulls** (downloads) the three images first, the first time only. Then something like:

```
 ✔ Network blog_default         Created
 ✔ Volume blog_site             Created
 ✔ Volume blog_db-data          Created
 ✔ Container blog-db-1          Healthy
 ✔ Container blog-wordpress-1   Started
 ✔ Container blog-phpmyadmin-1  Started
```

Waiting for `Healthy` can take 20–30 seconds the first time. That's MySQL setting itself up.

Open <http://localhost:8080>. WordPress asks you to set up the blog:

1. Pick a language, click **Continue**.
2. Fill in a **Site Title** (say, "Tanvi's blog"), a **Username**, a **Password** and an **Email** (any email is fine, nothing is sent). Click **Install WordPress**.
3. Log in with that username and password.

You're in the blog's admin area. Go to **Posts → Add New**, write a title and a line of text, and click **Publish**. Then open <http://localhost:8080> again: your post is on the blog ✓

## Try it: find your post in the database

Open <http://localhost:8081>. That's phpMyAdmin. Log in with:

- Username: `blog`
- Password: `secret`

(The `DB_USER` and `DB_PASSWORD` from `.env`.)

On the left, click the `blog` database, then the table **`wp_posts`**. Find the row with your title in the `post_title` column. That's where your post really lives: a row in a table, in MySQL, in the `blog_db-data` volume.

## Try it: it survives

```bash
docker compose down
docker compose up -d
```

Open <http://localhost:8080>. The blog and your post are still there: the two volumes were kept. (`docker compose down -v` would delete them, and you'd be back at the setup screen.)

## Your own app vs a ready-made one

| | Notes app (page 3) | WordPress (this page) |
| --- | --- | --- |
| Where the images come from | `build:` from your folders | `image:` from Docker Hub |
| Where the settings' names come from | you chose them in your code (`DB_PASSWORD`) | the image's page on Docker Hub (`WORDPRESS_DB_PASSWORD`) |
| Start | `docker compose up -d --build` | `docker compose up -d` |
| What you share with a friend | the folder with the code | just `compose.yaml` and `.env` |

## Clean up

```bash
docker compose down -v
```

`-v` this time, because it's only a practice blog: the containers, the network and both volumes go.

## Check yourself

1. Where would you look to find out which environment variables the `mysql` image understands?
2. You change `DB_PASSWORD` in `.env` but not anything else. Which two services get the new password? (And remember the catch from page 3.)
3. Why don't we need `--build` here?

## Next

All the Compose commands from sections 7 and 14 on one page: [Compose commands](commands.md).
