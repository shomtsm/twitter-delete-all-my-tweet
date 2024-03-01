# A program to delete al tweets at once using Twitter Archive and Twitter API

## Assumptions
- The tweets you want to delete at once must be your own tweets.
- You must have an archive of your account.
- You must have an API KEY or TOKEN with "Created with Read, Write, and Direct Messages permissions" (free accounts are OK).
- You must be able to run python.

## How it works

1. Replace API KEY etc
need: "Created with Read, Write, and Direct Messages permissions"

```py
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
```

2. Specify the path to the archive file
should be the /data/tweets.js file from your archieve data.
```py
archive_file_path = 'tweets-sample.js'
```

3. Run app.py
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

