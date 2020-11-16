from app import db
from sqlalchemy.dialects.postgresql import JSON  # noqa: F401


class Tutorial(db.Model):
    __tablename__ = 'tutorials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    tutorial_file = db.Column(db.String(), unique=True, nullable=False)
    starter_file = db.Column(db.String(), unique=True, nullable=False)
    solution_file = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, name, tutorial_file, starter_file, solution_file):
        self.name = name
        self.tutorial_file = tutorial_file
        self.starter_file = starter_file
        self.solution_file = solution_file

    def __repr__(self):
        return f'<id {self.id}>'
