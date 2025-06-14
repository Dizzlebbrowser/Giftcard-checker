from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_balance():
    data = request.get_json()
    card = data.get('card_number')
    month = data.get('exp_month')
    year = data.get('exp_year')
    cvv = data.get('cvv')

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://balance.vanillagift.com')
        time.sleep(2)
        driver.find_element(By.ID, 'cardNumber').send_keys(card)
        driver.find_element(By.ID, 'expMonth').send_keys(month)
        driver.find_element(By.ID, 'expYear').send_keys(year)
        driver.find_element(By.ID, 'cvv').send_keys(cvv)
        driver.find_element(By.ID, 'submit').click()
        time.sleep(6)
        balance = driver.find_element(By.CLASS_NAME, 'balance-amount').text
        return jsonify({'balance': balance})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000')
