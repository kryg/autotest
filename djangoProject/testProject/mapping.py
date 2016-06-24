host_url = 'http://example.com'
site_mapping = {
    "registration": {
        "url": host_url + "/registration/",
        "username": "//input[@id='username']",
        "email": "//input[@id='email']",
        "password": "//input[@name='password1']",
        "verify password": "//input[@name='password2']",
        "signup button": "//button[@name='signup']",
        "status message": "//div[@id='status']",
    },
    "authorization": {
        "url": host_url + "/login/",
        "username": "//input[@id='username']",
        "password": "//input[@name='password']",
        "login button": "//button[@name='login']",
        "status message": "//div[@id='status']",
    },
}