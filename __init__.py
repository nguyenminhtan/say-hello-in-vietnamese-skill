from mycroft import MycroftSkill, intent_file_handler


class SayHelloInVietnamese(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vietnamese.in.hello.say.intent')
    def handle_vietnamese_in_hello_say(self, message):
        self.speak_dialog('vietnamese.in.hello.say')


def create_skill():
    return SayHelloInVietnamese()

