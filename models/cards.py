"""用户"""
from app import db
from sqlalchemy import and_,or_


class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    allowed_num = db.Column(db.Integer, default=3)
    rare = db.Column(db.String(16))


def get_white_cards(page_number=1, page_size=10, keyword=""):
    cards = db.session.query(Card).filter(and_(or_(Card.rare == 'SR',Card.rare == 'UR'), Card.name.like(f'%{keyword}%'))).order_by(Card.allowed_num.desc())
    pagination = cards.paginate(page=page_number, per_page=page_size)
    return cards_json(pagination.items), pagination.pages, cards.count()


def get_black_cards(page_number=1, page_size=10, keyword=""):
    cards = db.session.query(Card).filter(and_(or_(Card.rare == 'N',Card.rare == 'R'), Card.name.like(f'%{keyword}%'))).order_by(Card.allowed_num.desc())
    pagination = cards.paginate(page=page_number, per_page=page_size)
    return cards_json(pagination.items), pagination.pages, cards.count()


def cards_json(cards):
    return [{"name": card.name, "allowed_num": card.allowed_num, "rare": card.rare} for card in cards]