# Crawler
Simple crawler example created with Scrapy (Python 3)

## Requirements

Install Ubuntu dependencies:
```
# sudo apt install -y virtualenv python-pip
```

Create virtualenv and install Python dependencies
```
$ virtualenv env                        # Create virtualenv
$ . ./env/bin/activate                  # Enable virtualenv
$ pip install -r pip-requirements.txt   # Install Python dependencies on virtualenv
```

## How to run
Run spiders:

```
$ ./run-spiders.sh
```

Output will be added to `./out/`.