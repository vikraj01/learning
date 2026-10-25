`-p 8080:80` opens a door on **every** network your laptop is on. Your phone on the same Wi-Fi could open the page too.

Sometimes you don't want that. A database or an admin page should only be reachable from your own laptop.

## The address in front

```
-p 8095:80              everyone who can reach your laptop
-p 127.0.0.1:8095:80    only your own laptop
```

`127.0.0.1` means "this computer". A door opened on it can only be used from this same laptop.

## Your job

Run nginx as `private-site`, opening on **http://localhost:8095**, with a door that only your laptop can use.

Then compare:

```
docker port private-site
```
