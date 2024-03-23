from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Global variables to store dropdown values
dropdown1_value = None
dropdown2_value = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global dropdown1_value, dropdown2_value

    if request.method == 'POST':
        # Get form data
        dropdown1 = request.form['dropdown1']
        dropdown2 = request.form['dropdown2']

        # Store dropdown values in global variables
        dropdown1_value = dropdown1
        dropdown2_value = dropdown2

        # Trigger GitHub Actions
        trigger_github_actions(dropdown1, dropdown2)

        return "GitHub Actions triggered successfully!"
    else:
        return render_template('index.html')

def trigger_github_actions(dropdown1, dropdown2):
    # GitHub Actions webhook URL
    github_actions_url = "YOUR_GITHUB_ACTIONS_WEBHOOK_URL"

    # Payload data to send to GitHub Actions
    payload = {
        "dropdown1": dropdown1,
        "dropdown2": dropdown2
    }

    # Send HTTP POST request to GitHub Actions webhook
    response = requests.post(github_actions_url, json=payload)

    # Check response status
    if response.status_code == 200:
        print("GitHub Actions triggered successfully!")
    else:
        print("Failed to trigger GitHub Actions.")

# Endpoint to retrieve dropdown values
@app.route('/dropdown_values', methods=['GET'])
def get_dropdown_values():
    global dropdown1_value, dropdown2_value
    return jsonify({
        'dropdown1': dropdown1_value,
        'dropdown2': dropdown2_value
    })

if __name__ == '__main__':
    app.run(debug=True)
