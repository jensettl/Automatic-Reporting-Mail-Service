# Functions for building and sending emails

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

SMTP_PORT = config.SMTP_PORT  # Standard port for email submission
SMTP_SERVER = config.SMTP_SERVER  # Google SMTP server
PWD = config.EMAIL_PWD  # Password for email account

def sendEmail(email_from, email_to, subject, body):
    msg = MIMEMultipart("alternative")  # Create a multipart message
    msg["From"] = email_from  # Add sender email to message
    msg["To"] = email_to  # Add receiver email to message
    msg["Subject"] = subject  # Add subject to message

    # Add body to email
    msg.attach(MIMEText(body, "html"))

    text = msg.as_string()

    try:
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        TIE_server.starttls()
        TIE_server.login(email_from, PWD)
        print("Connected to server")

        print()
        print(f"Sending email to - {email_to}")
        TIE_server.sendmail(email_from, email_to, text)
        print(f"Email successfully sent to {email_to}")
        print()

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        TIE_server.quit()
        print("Connection closed...")
        

def build_email_body(weather_data, astronomy_data, stock_data):
    styles = """
        body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        }

        .email-container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 95%;
            max-width: 800px;
            padding: 20px;
            text-align: center;
        }

        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* index-row flexibles Layout */
        .index-row {
            display: flex;
            margin-bottom: 20px;
            justify-content: space-evenly;
        }

        .index-box {
            background-color: #cfdee9;
            border-radius: 5px;
            margin: 5px;
            padding: 10px;
            box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
            text-align: center;
            min-width: 150px; 
        }

        .stock-info {
            background-color: #f9f9f9;
            border-radius: 5px;
            padding: 5px;
            margin-bottom: 20px;
            text-align: left;
            position: relative; /* Für den Sektor oben rechts */
        }
        .stock-info-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .stock-info p {
            margin: 5px 0;
        }

        .sector {
            background-color: #e0f7fa;
            color: #00796b;
            padding: 5px 10px;
            border-radius: 12px;
            font-size: 12px;
            position: absolute;
            top: 10px;
            right: 10px;
        }

        .footer {
            font-size: 12px;
            color: #999;
            margin-top: 20px;
        }

        a {
            color: #0066cc;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Balkendiagramm für Empfehlungen */
        .recommendation-bar {
            display: flex;
            background-color: #f4f4f4;
            border-radius: 5px;
            overflow: hidden;
            margin: 10px 0;
            height: 20px;
        }

        .recommendation-bar div {
            text-align: center;
            color: white;
            font-size: 12px;
            line-height: 20px;
        }

        .strong-buy {
            background-color: #28a745; /* Grün */
        }

        .buy {
            background-color: #007bff; /* Blau */
        }

        .hold {
            background-color: #ffc107; /* Gelb */
        }

        .sell {
            background-color: #fd7e14; /* Orange */
        }

        .strong-sell {
            background-color: #dc3545; /* Rot */
        }
        """
    
    stock_html = ""

    for stock in stock_data:
        stock_html += f"""
            <div class="stock-info">
                <div class="stock-info-header">
                    <p><strong>{stock}</strong></p>
                </div>
                <p>Closing at {stock_data[stock]['closing_price']}€ <i>({stock_data[stock]['changeSymbol']}{stock_data[stock]['changePct']}%)</i></p>
                <div class="recommendation-bar">
                    <div class="strong-buy" style="width: {stock_data[stock]['strongBuy']}%">StrongBuy ({stock_data[stock]['strongBuy']}%)</div>
                    <div class="buy" style="width: {stock_data[stock]['buy']}%">Buy ({stock_data[stock]['buy']}%)</div>
                    <div class="hold" style="width: {stock_data[stock]['hold']}%">Hold ({stock_data[stock]['hold']}%)</div>
                    <div class="sell" style="width: {stock_data[stock]['sell']}%">Sell ({stock_data[stock]['sell']}%)</div>
                    <div class="strong-sell" style="width: {stock_data[stock]['strongSell']}%">StrongSell ({stock_data[stock]['strongSell']}%)</div>
                </div>
            </div>
        """
            
    return f"""
        <html lang="de">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Stock Report</title>
                <style>
                    {styles}
                </style>
            </head>
                <body>
            <div class="email-container">
                <!-- Header Titel -->
                <div class="header">Daily Report</div>
                <!-- Weather Section -->
                <div class="section">
                    <h2>Weather for {weather_data["location"]}, {weather_data["country"]} </h2>
                    <p>Temperature: {weather_data["temperature"]}°C</p>
                    <p>Humidity: {weather_data["humidity"]}%</p>
                    <p>Wind: {weather_data["wind_speed"]} km/h</p>
                    <p>Condition: {weather_data["condition"]}</p>
                    <p class="footer">Last Updated: {weather_data["last_updated"]}</p>
                </div>
                
                <!-- Astronomy Section -->
                <div class="section">
                    <h2>Astronomy</h2>
                    <p>Sunrise: {astronomy_data["sunrise"]}</p>
                    <p>Sunset: {astronomy_data["sunset"]}</p>
                </div>
                
                <!-- Stock Section -->
                <div class="section">
                    <h2>Stocks</h2>
                    {stock_html}
                </div>
                
                <!-- Footer -->
                <div class="footer">This is an automated email</div>
            </div>
            </body>
        </html>
    """