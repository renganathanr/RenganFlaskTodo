import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flasktodo import mail

def save_profile_pic(form_profile_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_profile_pic.filename)
    profile_pic_fn = random_hex + f_ext
    profile_pic_path = os.path.join(app.root_path, 'static/profile_pics', profile_pic_fn)
    form_profile_pic.save(profile_pic_path)

    output_size = (125, 125)
    i = Image.open(form_profile_pic)
    i.thumbnail(output_size)
    i.save(profile_pic_path)

    return profile_pic_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='RenganFlaskBlog', recipients=[user.email])
    msg.body = f'''To reset your password, click the following link:{url_for('users.reset_token', token=token, _external=True)}
If you did not made this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)