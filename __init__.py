from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler


class ManagementLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require('Management.location'))
    def handle_management_location(self):
        nl = self.settings.get("new_location")
        self.speak_dialog("Management.location", data={"nl": nl})
        if nl == "firstfloor":
            self.speak_dialog('first.floor')
        elif nl == "secondfloor":
            self.speak_dialog('second.floor')
        elif nl == "thirdfloor":
            self.speak_dialog('third.floor')
        elif nl == "groundfloor":
            self.speak_dialog('ground.floor')

    @intent_handler(IntentBuilder("").require('Management.time'))
    def handle_management_time(self):
        opening = self.settings.get("opening")
        closure = self.settings.get("closure")
        self.speak_dialog("Management.time", data={"opening": opening, "closure": closure})

    @intent_handler(IntentBuilder("").require('contact.Management'))
    def handle_management_contact(self):
        email = self.settings.get("email")
        tel = self.settings.get("tel")
        self.speak_dialog("Management.contact", data={"email": email, "tel": tel})


def create_skill():
    return ManagementLocation()

