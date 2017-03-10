#coding=utf-8
from flask import Flask, render_template, session,  redirect, url_for, flash
from flask_script import Manager
# (注意：注释和#之间 是要有一个空格的！)

from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from flask_wtf import Form 这个已经过期了
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
# 之前写成moment = Moment() 导致一直出错，说是moment未定义！真是浪费了不少时间啊！
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


@app.route('/', methods=['GET', 'POST'])
def index():
    # 这个是先新建一个输入表格，这个是自定义实现。具体实现在上边
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    manager.run()


# 实例4-6 Flash消息 [4c]
# 测试URL1 404  http://127.0.0.1:5000






































































