

host_url = 'https://testing.alytics.ru/'
site_mapping = {
    "registration": {
        "url": host_url + "/",
        "registration button": ".js-to-register",
        "full_name": "#name",
        "company": "#company",
        "site": "#site",
        "position": "#work",
        "email": "#email",
        "phone": "#phone",
        "password": "#password1",
        "verify password": "#password2",
        "promo_code": "#promo_code",
        "create_user_button": ".js-reg-submit",
        "class success": ".queue-text",
    },
    "authorization": {
        "url": host_url + "/",
        "username": "#req1",
        "password": "#req2",
        "login button": "[type=submit]",
        "class success": ".projects-list",
    },

    "createProject": {
        "url": host_url + "/",
        "username": "#req1",
        "password": "#req2",
        "login button": "[type=submit]",
        "add project button": ".add-project-button",
        "name project": "#project-input-0",
        "name site": "#project-input-1",
        "button submit form": ".submit-form",

        "animation loading": ".progress-bar",
        "login YD in Alytics": "#project-input-0",

        "login YD in YD": "#login",
        "passwd YD in YD": "#passwd",
        "button submit form YD": ".domik-submit-button",

        "radio button all company": ".all-campaigns",
        "email GE": "#Email",
        "button next": "#next",
        "passwd GE": "#Passwd",
        "button signIn GE": "#signIn",
        "button submit approve access": "#submit_approve_access",
        "radio all data": ".js-profile-value:first-of-type",
        "selector add goals": ".goal-name-placeholder",
        "selector add utm": "[name=utm_medium]",
        "button to see the project": ".addProject",

    },
}