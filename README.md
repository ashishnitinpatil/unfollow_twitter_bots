## Project setup instructions

1. Clone project & cd into it
    - `git clone https://github.com/ashishnitinpatil/unfollow_twitter_bots.git`
    - `cd unfollow_twitter_bots/`
2. Setup virtual env
    - `python3 -m pip install virtualenv`
    - `virtualenv -p python3 .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`
3. Create new Twitter app & fetch keys & access tokens
    - Goto https://apps.twitter.com/app/new and enter project details with callback url as http://localhost:8000/callback/ (rest settings don't matter much)
    - You'll get redirected to your new app (e.g.https://apps.twitter.com/app/14811934)
    - Goto /keys and grab API key & Secret. Update secrets.json with these.
4. Migrate
    - `python manage.py migrate`
5. Run server
    - `python manage.py runserver`

## Licensing

This project copies (and modifies) sufficient parts of code from [martinjc/DjangoTweepy](https://github.com/martinjc/DjangoTweepy). Kindly note that his code is [licensed differently](https://creativecommons.org/licenses/by/3.0/) than [mine](./LICENSE). In short (**not legal advice**), any restrictions that may exist, are mainly due to the copied code.