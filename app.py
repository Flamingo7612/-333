from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Моя страница</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f2f2;
                text-align: center;
                padding: 30px;
            }

            .card {
                max-width: 500px;
                margin: auto;
                background: white;
                padding: 25px;
                border-radius: 20px;
                box-shadow: 0 5px 20px #ccc;
            }

            a {
                display: block;
                margin: 12px;
                padding: 14px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 10px;
            }

            a:hover {
                background: #555;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Привет!</h1>

            <p>
                Это мой личный сайт.<br>
                Здесь можно найти информацию обо мне
                и мои контакты.
            </p>

            <h2>Контакты</h2>

            <a href="tel:+79992339777">
                📞 Телефон
            </a>

            <a href="https://t.me/tamletamak76/" target="_blank">
                ✈️ Telegram
            </a>

            <a href="https://vk.ru/hanofkazan" target="_blank">
                🔵 ВКонтакте
            </a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
