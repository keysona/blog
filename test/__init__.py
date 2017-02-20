import os
from unittest import TestCase as BaseTestCase
from application import create_app, db
from application.model import Category, Tag, Post, User

TEST_DB = "test.db"
data = {
    'Category': [
        {'name': '技术'}, {'name': '生活'}, {'name': '随想'}, {'name': '情感'}
    ],
    'Tag': [
        {'name': 'Python'}, {'name': 'JavaScript'}, {'name': 'Linux'}, {'name': 'Android'}
    ],
    'Post': [
        {
            'title': 'Test',
            'article': '最近开始做公司内部项目，CRM系统（客户关系管理）， 用的flask+python3.5.2。我以前闲着没事逛逛github的时候发现了这个cookiecutter-flask，就是用来生成一个项目模板的东西，直接帮你生成项目总体框架还有README文件，还是比较方便的，直接填写逻辑即可。以前并没有使用flask的经验，这次也是边摸索一边使用（好在没碰到坑），主要想记录下关于单元测试的东西。crm主要是crud操作，这次我比较重视测试代码编写，web项目单元测试需要处理数据库交互，模拟请求，模拟登录，表单提交等操作，如何编写易于构建和执行的单元测试也是需要注意的地方。新项目统一用flask+python3.5.2(python3库的支持比我想象中快，目前使用的依赖中都支持python3)，前端使用vue，前后分离，后端使用flask-restful写接口。贴出来一些代码，如果写得不合适的正好可以给我指正下:)',
            'slug': 'test-1',
            'category': '生活',
            'tags': ['Linux', 'JavaScript']
        },
        {
            'title': 'Test--1',
            'article': '最近开始做公司内部项目，CRM系统（客户关系管理）， 用的flask+python3.5.2。我以前闲着没事逛逛github的时候发现了这个cookiecutter-flask，就是用来生成一个项目模板的东西，直接帮你生成项目总体框架还有README文件，还是比较方便的，直接填写逻辑即可。以前并没有使用flask的经验，这次也是边摸索一边使用（好在没碰到坑），主要想记录下关于单元测试的东西。crm主要是crud操作，这次我比较重视测试代码编写，web项目单元测试需要处理数据库交互，模拟请求，模拟登录，表单提交等操作，如何编写易于构建和执行的单元测试也是需要注意的地方。新项目统一用flask+python3.5.2(python3库的支持比我想象中快，目前使用的依赖中都支持python3)，前端使用vue，前后分离，后端使用flask-restful写接口。贴出来一些代码，如果写得不合适的正好可以给我指正下:)',
            'slug': 'test',
            'category': '生活',
            'tags': ['Python', 'JavaScript']
        },
        {
            'title': 'Test--2',
            'article': '最近开始做公司内部项目，CRM系统（客户关系管理）， 用的flask+python3.5.2。我以前闲着没事逛逛github的时候发现了这个cookiecutter-flask，就是用来生成一个项目模板的东西，直接帮你生成项目总体框架还有README文件，还是比较方便的，直接填写逻辑即可。以前并没有使用flask的经验，这次也是边摸索一边使用（好在没碰到坑），主要想记录下关于单元测试的东西。crm主要是crud操作，这次我比较重视测试代码编写，web项目单元测试需要处理数据库交互，模拟请求，模拟登录，表单提交等操作，如何编写易于构建和执行的单元测试也是需要注意的地方。新项目统一用flask+python3.5.2(python3库的支持比我想象中快，目前使用的依赖中都支持python3)，前端使用vue，前后分离，后端使用flask-restful写接口。贴出来一些代码，如果写得不合适的正好可以给我指正下:)',
            'slug': 'test-2',
            'category': '情感',
            'tags': ['Python', 'JavaScript']
        },
        {
            'title': 'Test--3',
            'article': '最近开始做公司内部项目，CRM系统（客户关系管理）， 用的flask+python3.5.2。我以前闲着没事逛逛github的时候发现了这个cookiecutter-flask，就是用来生成一个项目模板的东西，直接帮你生成项目总体框架还有README文件，还是比较方便的，直接填写逻辑即可。以前并没有使用flask的经验，这次也是边摸索一边使用（好在没碰到坑），主要想记录下关于单元测试的东西。crm主要是crud操作，这次我比较重视测试代码编写，web项目单元测试需要处理数据库交互，模拟请求，模拟登录，表单提交等操作，如何编写易于构建和执行的单元测试也是需要注意的地方。新项目统一用flask+python3.5.2(python3库的支持比我想象中快，目前使用的依赖中都支持python3)，前端使用vue，前后分离，后端使用flask-restful写接口。贴出来一些代码，如果写得不合适的正好可以给我指正下:)',
            'slug': 'test-3',
            'category': '随想',
            'tags': ['Android', 'JavaScript']
        },
    ]
}


def init_data(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Category
        for item in data['Category']:
            category = Category(name=item['name'])
            category.save()
        # Tag
        for item in data['Tag']:
            tag = Tag(name=item['name'])
            tag.save()
        # Post
        for item in data['Post']:
            category = Category.query.filter_by(name=item['category']).first()
            post = Post(title=item['title'], article=item['article'], slug=item['slug'], category=category)
            for tag_name in item['tags']:
                tag = Tag.query.filter_by(name=tag_name).first()
                post.tags.append(tag)
            post.save()


class TestCase(BaseTestCase):
    def setUp(self):
        os.environ['MODE'] = "TESTING"
        basedir = os.path.abspath(os.path.dirname(__file__))
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
                                                os.path.join(basedir, TEST_DB)
        self.app = app
        self.client = app.test_client()
        init_data(self.app)

    def tearDown(self):
        with self.app.app_context():
            # db.drop_all()
            pass
