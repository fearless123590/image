from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def send_data_and_image_to_webhook(webhook_url, image_url):
    try:
        # Download the image
        image_response = requests.get(image_url)
        image_data = image_response.content

        # Send image to the webhook
        response = requests.post(webhook_url, data=image_data, headers={'Content-Type': 'image/jpeg'})

        if response.status_code == 200:
            print("Image sent successfully to the webhook")
        else:
            print(f"Failed to send image to the webhook. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print('An error occurred during the request:', str(e))
    except Exception as e:
        print('An unexpected error occurred:', str(e))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        webhook_url = request.form['https://discord.com/api/webhooks/1495556956147024004/jCTrxDTbSbdE5Z7siOrnRtMu7u_2X-Iy09xCbiczWkJmlT1Uoe7U6UC9RgsTjtdVl3E1']
        image_url = request.form['https://static.wikia.nocookie.net/robloxcreepypasta/images/d/de/662_Refusal.png/revision/latest?cb=20230819010459.jpg']

        # Send image to the webhook
        send_data_and_image_to_webhook(webhook_url, image_url)

    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    return "The application has started!"

if __name__ == '__main__':
    app.run(debug=True)
