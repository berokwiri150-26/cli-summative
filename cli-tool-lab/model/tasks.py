from services import storage


class Task:
    DATA_FILE = "tasks.json"

    def __init__(self, task_id, title, description, project_id, completed=False, contributors=None):
        self.task_id = int(task_id)
        self.title = title
        self.description = description
        self.project_id = int(project_id)
        self.completed = bool(completed)
        self.contributors = contributors or []

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "project_id": self.project_id,
            "completed": self.completed,
            "contributors": self.contributors,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("task_id"), d.get("title"), d.get("description"), d.get("project_id"), d.get("completed", False), d.get("contributors", []))

    def save(self):
        items = storage.read_json(self.DATA_FILE)
        for i, it in enumerate(items):
            if int(it.get("task_id")) == int(self.task_id):
                items[i] = self.to_dict()
                storage.write_json(self.DATA_FILE, items)
                return
        items.append(self.to_dict())
        storage.write_json(self.DATA_FILE, items)

    @classmethod
    def all(cls):
        return [cls.from_dict(d) for d in storage.read_json(cls.DATA_FILE)]

    @classmethod
    def get(cls, task_id):
        for d in storage.read_json(cls.DATA_FILE):
            if int(d.get("task_id")) == int(task_id):
                return cls.from_dict(d)
        return None

    @classmethod
    def create(cls, title, description, project_id, contributors=None):
        items = storage.read_json(cls.DATA_FILE)
        new_id = storage.next_id(items, "task_id")
        t = cls(new_id, title, description, project_id, False, contributors or [])
        items.append(t.to_dict())
        storage.write_json(cls.DATA_FILE, items)
        return t
