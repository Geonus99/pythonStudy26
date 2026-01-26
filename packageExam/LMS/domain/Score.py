class Score:
    def __init__(self, uid, py:int, db:int, web:int, total:int, grade):
        self.uid = uid
        self.py = py
        self.db = db
        self.web = web
        self.total = total
        self.grade = grade

    def __str__(self):
        return f"{self.uid} | {self.py} | {self.db} | {self.web} | {self.total} | {self.grade}"

    def to_line(self):
        return f"{self.uid}|{self.py}|{self.db}|{self.web}|{self.total}|{self.grade}"

    @staticmethod
    def from_line(line):
        uid, py, db, web, total, grade = line.strip().split("|")
        return Score(uid,
                     py,
                     db,
                     web,
                     total,
                     grade
                     )