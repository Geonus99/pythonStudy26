class Board:
    def __init__(self,no, title, content, wirer):
        self.no = no
        self.title = title
        self.content = content
        self.writer = wirer


    def __str__(self):
        return f"{self.no} | {self.title} | {self.content} | {self.writer}"

    def to_line(self):
        return f"{self.no}|{self.title}|{self.content}|{self.writer}"


    @staticmethod
    def from_line(line:str):
        no, title, content, writer = line.strip().split("|")
        return Board(no,
                     title,
                     content,
                     writer
                    )