import os.path
import json
from validate_email import validate_email


def email_validation(email):
    if os.path.exists("Persistance/DataBase/user_emails.json"):
        with open("Persistance/DataBase/user_emails.json") as file:
            data = json.load(file)
        if email not in data['UserEmails'] and validate_email(email):
            data['UserEmails'].append(email)
        else:
            raise ValueError('This email have already used')
    else:
        data = {"UserEmails": []}
        data["UserEmails"].append(email)
    with open("Persistance/DataBase/user_emails.json", "w") as file:
        json.dump(data, file)
    return email
