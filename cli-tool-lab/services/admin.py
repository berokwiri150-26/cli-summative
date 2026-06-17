from model import User, Project, Task


def create_user(username: str, email: str) -> User:
	return User.create(username, email)


def list_users():
	return User.all()


def add_project_to_user(owner_id: int, project_name: str, description: str) -> Project:
	# create project
	p = Project.create(project_name, description, owner_id)
	# update user
	u = User.get(owner_id)
	if u:
		if p.project_id not in u.project_ids:
			u.project_ids.append(p.project_id)
			u.save()
	return p


def list_projects(owner_id: int = None):
	projects = Project.all()
	if owner_id is None:
		return projects
	return [p for p in projects if p.owner_id == int(owner_id)]


def add_task_to_project(project_id: int, title: str, description: str, contributors=None) -> Task:
	t = Task.create(title, description, project_id, contributors or [])
	# update project
	p = Project.get(project_id)
	if p:
		if t.task_id not in p.task_ids:
			p.task_ids.append(t.task_id)
			p.save()
	return t


def list_tasks(project_id: int = None):
	tasks = Task.all()
	if project_id is None:
		return tasks
	return [t for t in tasks if t.project_id == int(project_id)]


def complete_task(task_id: int) -> Task:
	t = Task.get(task_id)
	if not t:
		return None
	t.completed = True
	t.save()
	return t
