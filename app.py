from flask import Flask, render_template, request

from models import Board

app = Flask(__name__)
options = []


@app.route('/')
def index():
    number_of_boards = request.args.get('boards', default=1, type=int)
    boards = [Board(options) for _ in range(0, number_of_boards)]
    return render_template('index.j2', boards=boards)


if __name__ == '__main__':
    with open('cells.txt') as file:
        options = file.read().splitlines()
        app.run()
