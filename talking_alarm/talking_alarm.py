from num2words import num2words
from gtts import gTTS
import os


def convert_time_verbal(hour, minute):
    """
    Accept time as an arg and print out verbal statement
    Ex: convert_time_verbal(01,30) --> It's one thirty am
    @param hour:
    @param minute:
    @return: alarm clock string
    """

    if int(hour) >= 12:
        suffix = "p m"
        hour = int(hour) - 12       # do not follow 24 hour format verbally (i.e, 14:00 PM = 2:00 PM)
    else:
        suffix = "a m"

    # is an "oh" necessary?
    oh = ""
    if int(minute[-2]) == 0:
        oh = "oh "

    # never say 'zero' minute or hour
    zero = False
    if num2words(minute) == "zero":
        zero = True
    if num2words(hour) == "zero":
        hour = "12"

    alarm_text = ""
    if not zero:
        alarm_text = "It's " + num2words(hour) + " " + oh + num2words(minute) + " " + suffix
    else:
        alarm_text = "It's " + num2words(hour) + " " + suffix

    alarm_voice = gTTS(text=alarm_text, lang='en', slow=False)
    alarm_voice.save("alarm.mp3")
    os.system("start alarm.mp3")
    return alarm_text


print(convert_time_verbal("21", "00"))
