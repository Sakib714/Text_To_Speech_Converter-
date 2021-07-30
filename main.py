import pyttsx3

frnd = pyttsx3.init()

# Set up Voice speed rate
rate = frnd.getProperty('rate')
print('Vice speed rate: ', rate)
frnd.setProperty('rate', 140)

# Setting  up volume
volume = frnd.getProperty('volume')
print('Volume: ', volume)
frnd.setProperty('volume', 1)

# Changing voices
# try:
#     tone = frnd.getProperty('voice')
#
#     print('Voice: ', tone)
#     frnd.setProperty('voice', tone[0].id)
#
# except Exception as e:
#     print(e)
#     frnd.say(e)


speech = input('Enter your text: ')

frnd.say(speech)
frnd.save_to_file(speech, 'tts.mp3')

frnd.runAndWait()
