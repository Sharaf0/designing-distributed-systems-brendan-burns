docker build -f Dockerfile.legacy -t dc-legacy .

docker run --rm -v $(pwd)/shared:/shared dc-legacy

pgrep python

kill -s HUP <pid>

kill -s HUP $(pgrep python)