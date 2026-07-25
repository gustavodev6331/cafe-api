import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


# URL FOR POSTMAN: https://documenter.getpostman.com/view/55360170/2sBXwntXXm
# MY VERY FIRST API!!!!!!

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    def to_dict(self):
        """Convert the Cafe model into a serializable dictionary."""
        return {
        "id": self.id,
        "name": self.name,
        "map_url": self.map_url,
        "img_url": self.img_url,
        "location": self.location,
        "has_sockets": self.has_sockets,
        "has_toilet": self.has_toilet,
        "has_wifi": self.has_wifi,
        "can_take_calls": self.can_take_calls,
        "seats": self.seats,
        "coffee_price": self.coffee_price
        }
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_cafe():
    """Return a random cafe from the database."""
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()
    random_cafe = random.choice(all_cafe)
    response = jsonify(cafe=random_cafe.to_dict())

    return response

@app.route("/all", methods=["GET", "POST"])
def all_cafes():
    """Get a list of all cafes."""
    results = db.session.execute(db.select(Cafe))
    all_cafe = results.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])

@app.route("/search", methods=["GET", "POST"])
def search_cafe():
    """search the cafe by spefici location."""
    location = request.args.get("loc")

    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafe = result.scalars().all()
    if all_cafe:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])
    else:
        return "Sorry, we don't have a cafe at that location."


@app.route("/add", methods=["POST"])
def post_new_cafe():
    """add a new cafe to the database."""
    new_cafe = Cafe (
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url= request.args.get("img_url"),
        location=request.args.get("location"),
        has_sockets= (request.args.get("has_sockets", "")).lower() == "true",
        has_toilet = (request.args.get("has_toilet", "")).lower() =="true",
        has_wifi = (request.args.get("has_wifi", "")).lower() == "true",
        can_take_calls = (request.args.get("can_take_calls", "")).lower() == "true",
        seats = request.args.get("seats"),
        coffee_price = request.args.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': "The new cafe has been added."})

@app.route("/update_price/<int:coffe_id>", methods=["PATCH"])
def update_price(coffe_id):
    new_price = request.args.get("new_price")
    coffe = db.session.get(Cafe, coffe_id)
    if coffe is None:
        return jsonify(response={'not found': "that coffe id does not exist in our database."}), 404
    else:
        coffe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={'success': "The coffe has been updated."}), 200

@app.route("/delete/<int:coffe_id>", methods=["DELETE"] )
def delete_cafe(coffe_id):
    api_key = request.args.get("api_key")

    if api_key != "TopSecretAPIKey":
        return jsonify(response={'not found': "You can not delete data without API key."}), 403
    coffe = db.session.get(Cafe, coffe_id)
    print(coffe_id)
    if coffe is None:
        return jsonify(response={'not found': "that coffe id does not exist in our database."}), 403

    else:
        db.session.delete(coffe)
        db.session.commit()
        return jsonify(response={'success': "The coffe has been deleted."}), 200



# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
