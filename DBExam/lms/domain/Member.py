class Member:
    def __init__(self, id, uid, pw, name, role="user", active=True):
        self.id = id
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    def __str__(self):
        return f"{self.name}님 [{self.uid}|{self.pw}] [{self.role}]"

    @classmethod
    def from_dict(cls, row: dict):
        if not row:
            return None

        return cls(
            id=row.get("id"),
            uid=row.get("uid"),
            pw=row.get("password"),
            name=row.get("name"),
            role=row.get("role"),
            active=bool(row.get("active"))
        )

    def is_admin(self):
        return self.role == "admin"
