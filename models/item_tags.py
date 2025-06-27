from db import db


# class ItemTags(db.Model):
#     __tablename__ = "Items_tags"
#
#     id = db.Column(db.Integer, primary_key=True)
#     item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
#     tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))


items_tags = db.Table(
    "items_tags",
    db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True)
)