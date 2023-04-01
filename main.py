from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    pr = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(pr)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/mars.jpg"align="middle">
                        <h1>Вот она какая, красная планета.</h1>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1 class="text-danger">Жди нас, Марс!</h1>
                        <img src="static/img/mars.jpg"align="middle">
                        <h1></h1>
                        <h1 class="text-default" style="background-color:  #C3D099; font-size: 16px;">Человечество вырастает из детства.</h1>
                        <h1 class="text-default" style="background-color:  #d63384; font-size: 16px;">Человечеству мала одна планета.</h1>
                        <h1 class="text-default" style="background-color:  #fd7e14; font-size: 16px;">Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                        <h1 class="text-default" style="background-color:  #198754; font-size: 16px;">И начнем с Марса</h1>
                        <h1 class="text-default" style="background-color:  #dc3545; font-size: 16px;">Присоединяйся!</h1>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>{planet_name}</title>
                          </head>
                          <body>
                            <h1 class="text-primary">Мое предложение: {planet_name}</h1>
                            <h3 class="text-default" style="background-color:  #C3D099; font-size: 16px;">Пригодна для жизни.</h1>
                            <h3 class="text-default" style="background-color:  #d63384; font-size: 16px;">Много необходимых ресурсов.</h1>
                            <h3 class="text-default" style="background-color:  #fd7e14; font-size: 16px;">Близко находится к земле.</h1>
                            <h3 class="text-default" style="background-color:  #198754; font-size: 16px;">Магнитное поле сравнимо с Землей.</h1>
                            <h3 class="text-default" style="background-color:  #dc3545; font-size: 16px;">Возможно переселение.</h1>
                          </body>
                        </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
