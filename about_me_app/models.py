from about_me_app import db


class Aboutme(db.Model):
    """Модель 'Обо мне', для хранения в БД."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    nickname = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    about_author = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Сериализатор модели."""
        return dict(
            id = self.id,
            name = self.name,
            surname = self.surname,
            nickname = self.nickname,
            age = self.age,
            about_author = self.about_author,
        )

    def from_dict(self, data):
        """Десериализатор модели."""
        for field in ['name', 'surname', 'nickname', 'age', 'about_author']:
            if field in data:
                setattr(self, field, data[field]) 
