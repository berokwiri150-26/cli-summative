from services import storage


class User:
    DATA_FILE = "users.json"

    def __init__(self, user_id, username, email, project_ids=None):
        self.user_id = int(user_id)
        self.username = username
        self.email = email
        self.project_ids = project_ids or []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "project_ids": self.project_ids,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("user_id"), data.get("username"), data.get("email"), data.get("project_ids", [])
        )

    def save(self):
        items = storage.read_json(self.DATA_FILE)
        for i, it in enumerate(items):
            if int(it.get("user_id")) == int(self.user_id):
                items[i] = self.to_dict()
                storage.write_json(self.DATA_FILE, items)
                return
        items.append(self.to_dict())
        storage.write_json(self.DATA_FILE, items)

    @classmethod
    def all(cls):
        return [cls.from_dict(d) for d in storage.read_json(cls.DATA_FILE)]

    @classmethod
    def get(cls, user_id):
        for d in storage.read_json(cls.DATA_FILE):
            if int(d.get("user_id")) == int(user_id):
                return cls.from_dict(d)
        return None

    @classmethod
    def create(cls, username, email):
        items = storage.read_json(cls.DATA_FILE)
        new_id = storage.next_id(items, "user_id")
        u = cls(new_id, username, email)
        items.append(u.to_dict())
        storage.write_json(cls.DATA_FILE, items)
        return u
