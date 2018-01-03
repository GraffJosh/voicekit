import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import snowboydecoder
from google_speech import Speech
from phue import Bridge

def main():

	hue_bridge = Bridge('192.168.1.134')
	hue_bridge.connect()
	hue_bridge.get_api()
	lights = hue_bridge.lights
	light_names = hue_bridge.get_light_objects('name')

	Speech('Josh Graff is present',"en").play(None)
	print ('test')
	button = aiy.voicehat.get_button()
	led = aiy.voicehat.get_led()
	aiy.audio.get_recorder().start()

	detector = snowboydecoder.HotwordDetector("resources/snowboy.umdl", sensitivity=0.5, audio_gain=1)
	detector.start(detected_callback)
	#jarvis_thread()


def jarvis_thread():
	recognizer = aiy.cloudspeech.get_recognizer()
	recognizer.expect_hotword('jarvis')
	recognizer.expect_phrase('repeat after me')

	print('Jarvis now listening...')
	while True:
		#print('Press the button and speak')
		#recognizer.wait_for_hotword()

		spoken_text = recognizer.recognize()
		if not spoken_text:
			print('Sorry, I did not hear you.')
		else:
			print('You said "', spoken_text, '"')
			if 'turn on the' or 'turn off the' in spoken_text:

				light_names['couch'].on = True
			elif 'turn off the couch' in spoken_text:
				light_names['couch'].on = False
			elif 'repeat after me' in spoken_text:
				print('repeating spoken_text')
				repeatspoken_text = spoken_text.replace('repeat after me',' ',1)
				aiy.audio.say(repeatspoken_text,'en-GB',60,100)
			elif 'goodbye' in spoken_text:
				break

def detected_callback():
	print ('hotword_detected')

if __name__ == '__main__':
	main()
