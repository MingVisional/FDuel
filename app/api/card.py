from . import api
from flask import request
from models.cards import get_white_cards, get_black_cards


@api.route('/white', methods=['GET'])
def white_cards():
    page_num = request.args.get('page_num', 1, int)
    page_size = request.args.get('page_size', 1000, int)
    keyword = request.args.get('keyword', "", str)
    cards, pages, total = get_white_cards(page_num, page_size, keyword)
    return {
        "cards": cards,
        "pages": pages,
        "total": total
    }


@api.route('/black', methods=['GET'])
def black_cards():
    page_num = request.args.get('page_num', 1, int)
    page_size = request.args.get('page_size', 1000, int)
    keyword = request.args.get('keyword', "", str)
    cards, pages, total = get_black_cards(page_num, page_size, keyword)
    return {
        "cards": cards,
        "pages": pages,
        "total": total
    }


# @api.route('/init', methods=['GET'])
# def init():
#     from .. import db
#     db.create_all()
#     return "SUCCESS"
