from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route('/incoming', methods=['POST'])
def incoming_call():
    # Create VoiceResponse object to construct TwiML
    response = VoiceResponse()
    gather = response.gather(num_digits=1, action='/handle-key', method='POST')
    gather.say("Welcome to the call center. Press 1 for sales, 2 for support.", voice='alice')
    return str(response)

@app.route('/handle-key', methods=['POST'])
def handle_key():
    digit_pressed = request.values.get('Digits', None)

    # Start building the response to send back to Twilio
    response = VoiceResponse()

    if digit_pressed == '1':
        response.say("Connecting to sales.", voice='alice')
        dial = Dial()
        dial.number("+46727242544")
        response.append(dial)
    elif digit_pressed == '2':
        response.say("Connecting to support.", voice='alice')
        dial = Dial()
        dial.number("+46727242544")
        response.append(dial)
    else:
        response.say("Invalid option. Please try again.", voice='alice')
        response.redirect('/incoming', method='POST')

    return str(response)

if __name__ == '__main__':
    app.run()