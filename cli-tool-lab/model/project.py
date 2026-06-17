from services import storage


class Project:
    DATA_FILE = "projects.json"

    def __init__(self, project_id, project_name, description, owner_id, task_ids=None, status="In Progress"):
        self.project_id = int(project_id)
        self.project_name = project_name
        self.description = description
        self.owner_id = int(owner_id)
        self.task_ids = task_ids or []
        self.status = status

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "description": self.description,
            "owner_id": self.owner_id,
            "task_ids": self.task_ids,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("project_id"), d.get("project_name"), d.get("description"), d.get("owner_id"), d.get("task_ids", []), d.get("status", "In Progress"))

    def save(self):
        items = storage.read_json(self.DATA_FILE)
        for i, it in enumerate(items):
            if int(it.get("project_id")) == int(self.project_id):
                items[i] = self.to_dict()
                storage.write_json(self.DATA_FILE, items)
                return
        items.append(self.to_dict())
        storage.write_json(self.DATA_FILE, items)

    @classmethod
    def all(cls):
        return [cls.from_dict(d) for d in storage.read_json(cls.DATA_FILE)]

    @classmethod
    def get(cls, project_id):
        for d in storage.read_json(cls.DATA_FILE):
            if int(d.get("project_id")) == int(project_id):
                return cls.from_dict(d)
        return None

    @classmethod
    def create(cls, project_name, description, owner_id):
        items = storage.read_json(cls.DATA_FILE)
        new_id = storage.next_id(items, "project_id")
        p = cls(new_id, project_name, description, owner_id)
        items.append(p.to_dict())
        storage.write_json(cls.DATA_FILE, items)
        return p
