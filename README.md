# Goal

Create a Flask API that runs on a Distroless image from [GoogleContainerTools/distroless](https://github.com/GoogleContainerTools/distroless)

Requirements:

- install `flask` and create Hello World app
- install `gunicorn` to make sure that it runs not just with `werkzeug` dev server
- install a couple packages that rely on underlying C-libs like `numpy` and `pandas` to make sure that distroless output image still runs when dependencies are copied over

# Why?

Avoid the headache of security scanners. More distro dependencies = more problems.

# Setup

After cloning the repo, build via:

```shell
docker build -t flask-distroless:dev .
```

and run the built image (exposing port 5000) with:

```shell
docker run -d -p 5000:5000 flask-distroless:dev
```

You should see the hello world response at [localhost:5000](http://localhost:5000)

# Inspiration

- Google Distroless Python Example
  - repo: https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile
- How to Harden Your Containers With Distroless Docker Images by [@bharatmicrosystems](https://github.com/bharatmicrosystems)
  - article: https://betterprogramming.pub/how-to-harden-your-containers-with-distroless-docker-images-c2abd7c71fdb
	- repo: https://github.com/bharatmicrosystems/flask-hello-world
