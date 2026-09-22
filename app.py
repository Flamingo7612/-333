from flask import Flask, request

app = Flask(__name__)

questions = [
    {
        "question": "Сколько столпов в исламе?",
        "answers": ["3", "7", "1", "5"],
        "correct": "5"
    },
    {
        "question": "Сколько будет 5 + 7?",
        "answers": ["10", "11", "12", "13"],
        "correct": "12"
    },
    {
        "question": "Сколько обязательных намазов?",
        "answers": ["10", "5", "6", "0"],
        "correct": "5"
    },
    {
        "question": "Сколько планет в Солнечной системе?",
        "answers": ["7", "8", "9", "10"],
        "correct": "8"
    },
    {
        "question": "Кюп зюз - ?",
        "answers": [
            "айбят зюз",
            "бук зюз",
            "зачем?",
            "бр бр патапим"
        ],
        "correct": "бук зюз"
    }
]


@app.route("/", methods=["GET", "POST"])
def quiz():

    if request.method == "POST":

        score = 0

        for i, question in enumerate(questions):
            answer = request.form.get(f"question{i}")

            if answer == question["correct"]:
                score += 1

        return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1.0">
            <title>Результат</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(
                        135deg,
                        #667eea,
                        #764ba2
                    );
                    min-height: 100vh;
                    margin: 0;
                    padding: 20px;
                    box-sizing: border-box;
                }}

                .result {{
                    background: white;
                    max-width: 500px;
                    margin: 40px auto;
                    padding: 30px;
                    border-radius: 20px;
                    text-align: center;
                    box-sizing: border-box;
                }}

                .result h1 {{
                    font-size: 28px;
                }}

                .score {{
                    font-size: 24px;
                    margin: 20px 0;
                }}

                a {{
                    display: inline-block;
                    margin-top: 15px;
                    padding: 14px 20px;
                    background: #4f46e5;
                    color: white;
                    text-decoration: none;
                    border-radius: 12px;
                }}
            </style>
        </head>

        <body>

            <div class="result">
                <h1>🎉 Викторина завершена!</h1>

                <div class="score">
                    Ты набрал {score} из {len(questions)}
                </div>

                <p>
                    Правильных ответов: {score}
                </p>

                <a href="/">
                    Пройти ещё раз
                </a>
            </div>

        </body>
        </html>
        """

    html = """
    <!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>Моя викторина</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(
                    135deg,
                    #667eea,
                    #764ba2
                );
                min-height: 100vh;
                margin: 0;
                padding: 15px;
            }

            .quiz {
                background: white;
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border-radius: 20px;
            }

            h1 {
                text-align: center;
                font-size: 28px;
                margin-top: 5px;
            }

            .question {
                margin-top: 25px;
                padding: 18px;
                background: #f5f5f5;
                border-radius: 15px;
            }

            .question h3 {
                margin-top: 0;
                line-height: 1.4;
            }

            label {
                display: block;
                background: white;
                padding: 14px;
                margin: 8px 0;
                border-radius: 10px;
                cursor: pointer;
            }

            label:hover {
                background: #e8eaff;
            }

            input {
                margin-right: 8px;
            }

            button {
                width: 100%;
                padding: 16px;
                margin-top: 25px;
                border: none;
                border-radius: 12px;
                background: #4f46e5;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }

            button:hover {
                background: #3730a3;
            }
        </style>
    </head>

    <body>

        <div class="quiz">

            <h1>🧠 Моя викторина</h1>

            <form method="POST">
    """

    for i, question in enumerate(questions):

        html += f"""
            <div class="question">

                <h3>
                    {i + 1}. {question["question"]}
                </h3>
        """

        for answer in question["answers"]:

            html += f"""
                <label>
                    <input
                        type="radio"
                        name="question{i}"
                        value="{answer}"
                        required
                    >
                    {answer}
                </label>
            """

        html += """
            </div>
        """

    html += """
                <button type="submit">
                    Проверить ответы 🚀
                </button>

            </form>

        </div>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
