from flask import Blueprint
from flask.ext.login import login_required, current_user
from flask import jsonify, request, g
from models import Article
from datetime import datetime
from sqlalchemy import or_

article = Blueprint('article', __name__)


@article.route('/listing', methods=['POST'])
def listing_article():
    page_size = request.form.get('page_size', type=int, default=20)
    page = request.form.get('page', type=int, default=1)
    key = request.form.get('key', type=str, default='')
    articles = g.session.query(Article).filter_by(remove=False)
    if current_user.is_anonymous:
        articles = articles.filter_by(release=True)
    if key != '':
        articles = articles.filter(or_(Article.content.like('%{}%'.format(key)),
                                       Article.title.like('%{}%'.format(key))))
    count = articles.count()
    articles = articles.order_by(Article.create_time.desc()) \
        .limit(page_size).offset((page - 1) * page_size)

    return jsonify({
        'status': 'success',
        'data': {
            'count': count,
            'articles': [a.to_json(full_content=False) for a in articles]
        }
    })


@article.route('/get', methods=['POST'])
def get_article():
    note = g.session.query(Article).filter_by(id=request.form.get('id', type=int)).first()
    return jsonify({'status': 'success', 'data': note.to_json(full_content=True)})


@article.route('/create', methods=['POST'])
@login_required
def create_article():
    now = datetime.now()
    note = Article(
        title=request.form.get('title', type=str),
        abstract=request.form.get('abstract', type=str),
        content=request.form.get('content'),
        more=request.form.get('more', type=str) == 'true',
        create_time=now,
        update_time=now,
    )
    g.session.add(note)
    g.session.commit()
    return jsonify({'status': 'success', 'data': []})


@article.route('/update', methods=['POST'])
@login_required
def update_article():
    note = g.session.query(Article).filter_by(id=request.form.get('id', type=int)).first()
    note.title = request.form.get('title', type=str)
    note.content = request.form.get('content', type=str)
    note.abstract = request.form.get('abstract', type=str)
    note.more = request.form.get('more', type=str) == 'true'
    note.update_time = datetime.now()
    g.session.add(note)
    g.session.commit()
    return jsonify({'status': 'success', 'data': []})


@article.route('/remove', methods=['POST'])
@login_required
def remove_article():
    note = g.session.query(Article).filter_by(id=request.form.get('id', type=int)).first()
    note.remove = True
    note.update_time = datetime.now()
    g.session.add(note)
    g.session.commit()
    return jsonify({'status': 'success', 'data': []})


@article.route('/release', methods=['POST'])
@login_required
def release_article():
    note = g.session.query(Article).filter_by(id=request.form.get('id', type=int)).first()
    note.release = True
    note.update_time = datetime.now()
    g.session.add(note)
    g.session.commit()
    return jsonify({'status': 'success', 'data': []})
