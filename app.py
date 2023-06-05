# Flaskクラスをimportする
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# Flaskクラスをインスタンス化する
app = Flask(__name__)

# SQLAlchemyの設定
# URI postgresql:userid:password@hostname:port/dbname
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
# SQLAlchemyでのデータベースの変更を追跡する場合は、True設定（開発環境はTrue、本番はFalse）
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# SQLAlchemyをインスタンス化
db = SQLAlchemy(app)


# モデルの定義
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))


# ルートエンドポイント
@app.route("/")
def get_users():
    # 出力用変数初期化
    userList = ""

    # テーブルからデータを取得
    users = Users.query.all()

    # 取得したデータを表示
    for user in users:
        userList += f"ID: {user.id}, Username: {user.name} <br>"

    return userList


if __name__ == "__main__":
    app.run()
