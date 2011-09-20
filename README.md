# reddit-calpoly-addflair
A simple web application that allows users in the 
[Cal Poly subreddit](http://calpoly.reddit.com) to add flair to their username


## Install
1. Ensure that the Python packages [reddit](http://pypi.org/pypi/reddit) and 
[django-repatcha](http://pypi.org/pypi/django-recaptcha) are installed  
`pip install reddit`  
`pip install django-recaptcha`
2. Edit the settings.py template to your needs
3. Confirm the reddit login credentials in web/flair/flairclient.py and web/register/manage/commands/check.py
4. Run the server
