#!/bin/bash

# Enable virtualenv
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $DIR/env/bin/activate

# Scrapy
cd $DIR/recipes
scrapy crawl tudogostoso