from flask import Blueprint, request, render_template, current_app as app
from . import Post, Tag

blog = Blueprint('blog', __name__)


@blog.route('/', defaults={'page': 1})
@blog.route('/index/page/<int:page>')
def index(page):
    pagination = Post.query.order_by(Post.pub_date.desc()).paginate(page, per_page=app.config['PER_PAGE'],
                                                                    error_out=False)
    posts = pagination.items
    return render_template('index.html', **{'posts': posts, 'pagination': pagination})


@blog.route('/tag/<string:name>')
def get_tag_detail(name):
    tag = Tag.query.filter_by(name=name).first_or_404()
    return str(tag)


@blog.route('/post/<string:slug>')
def get_post_detail(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    post.add_hit_count()
    return render_template('post.html', post=post)
