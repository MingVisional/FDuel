"""主函数"""
from flask import render_template

from app import create_app


app = create_app(debug=False)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=7400)
