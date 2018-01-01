import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from phue import Bridge

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('repeat after me')


    hue_bridge = Bridge('192.168.1.134')
    hue_bridge.connect()
    hue_bridge.get_api()
    lights = hue_bridge.lights
    light_names = hue_bridge.get_light_objects('name')


    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    recognizer.expect_hotword('jarvis')

    while True:
        #print('Press the button and speak')
        #recognizer.wait_for_hotword()
        print('Listening...')
        text = recognizer.recognize()
        if not text:
            #print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'turn on the couch' in text:
                light_names['couch'].on = True
            elif 'turn off the couch' in text:
                light_names['couch'].on = False
            elif 'repeat after me' in text:
                print('repeating text')
                repeattext = text.replace('repeat after me',' ',1)
                aiy.audio.say(repeattext,'en-GB',60,100)
            elif 'goodbye' in text:
                break


if __name__ == '__main__':
    main()
