import os
import time
import yagmail
from jinja2 import Template, FileSystemLoader, Environment


class EmailListener:
    SECONDS_IN_DAY = 86400

    def __init__(self, username, password, destination):
        # initialise STMP client
        self.__yag = yagmail.SMTP(username, password)
        self.__dest = destination

        # set last email date as none
        self.__last_email = None

    def notify(self, event):
        # send email if there is no water
        if not event['water']:

            # check whether an email has been sent in the last day
            if (self.__last_email is not None 
                    and time.time() > self.__last_email + SECONDS_IN_DAY):
                # send email and update last email time
                self.__send()
                self.__last_email = time.time()

    def __render_template(self):
        # set up variables
        template_file = './email.html'
        render_vars = {
                'name': 'Jordan',
                'plant': 'Chili'
                }

        # get directory
        script_path = os.path.dirname(os.path.abspath(__file__))

        # render environment
        env = Environment(loader=FileSystemLoader(script_path))
        text = env.get_template(template_file).render(render_vars)

        return text


    def __send(self):
        # structure email contents
        subject = 'Your plant needs watering!'
        contents = self.__render_template()

        # send the email
        self.__yag.send(self.__dest, subject, contents)
