import yagmail


class EmailListener:

    def __init__(self, username, password, destination):
        # initialise STMP client
        self.__yag = yagmail.SMTP(username, password)
        self.__dest = destination

    def notify(self, event):
        # send email if there is no water
        if not event['water']:
            self.__send()

    def __send(self):
        # structure email contents
        subject = 'Your plant needs watering!'
        contents = """
        Your plant is too dry and needs watering now. 
        Regards, your friendly WaterBoy.
        """

        # send the email
        self.__yag.send(self.__dest, subject, contents)
