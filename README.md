# ![logo](https://avatars2.githubusercontent.com/u/25215892?v=3&size=50) Backquote 

[![Build Status](https://travis-ci.org/BackQuote/backquote.svg?branch=master)](https://travis-ci.org/BackQuote/backquote)
[![Coverage Status](https://codeclimate.com/github/BackQuote/backquote.svg?branch=master)](https://codeclimate.com/github/BackQuote/backquote)

# Summary
The goal of this project is to develop a performant, reliable infrastructure to backtest stock trading algorithms against large amounts of historical stock data and visualize the results with graphs. 

## Install

### API

Setup python environment and install dependencies:

```
mkdir -p $HOME/docker/volumes/postgres
sudo apt-get install libpq-dev
sudo apt install postgresql-client-12

virtualenv -p /usr/bin/python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
```

Start API
```
cd server
python app.py
```

### Client

Install javascript dependencies:
```
npm install
```

Start UI
```
npm start
```

## Team
[![Charles_Provencher](https://avatars0.githubusercontent.com/u/9503902?v=3&s=144)](https://github.com/cprovencher) | [![Anthony_Nadeau](https://avatars3.githubusercontent.com/u/15678424?v=3&s=144)](https://github.com/anadeau1) | [![Martin_Rancourt](https://avatars2.githubusercontent.com/u/2197856?v=3&s=144)](https://github.com/account)
---|---|---
[Charles Provencher](https://github.com/cprovencher) | [Anthony Nadeau](https://github.com/anadeau1) | [Martin Rancourt](https://github.com/mrancourt)


## License
MIT © BackQuote Team
