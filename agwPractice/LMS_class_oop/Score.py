class Score:
    def __init__(self, uid, py, db, web, total, grade):
        self.id = uid
        self.py = py
        self.db = db
        self.web = web
        self.total = total
        self.grade = grade

    def to_line(self):
        return f"{self.id}|{self.py}|{self.db}|{self.web}|{self.total}|{self.grade}"

    @classmethod
    def from_line(cls, line):
        uid, py, db, web, total, grade = line.split("|")
        return Score(uid, py, db, web, total, grade)