import argparse
import sys
from services import admin


def cmd_create_user(args):
    u = admin.create_user(args.username, args.email)
    print(f"Created user: {u.user_id} - {u.username} <{u.email}>")


def cmd_list_users(args):
    for u in admin.list_users():
        print(f"{u.user_id}: {u.username} ({u.email}) Projects: {u.project_ids}")


def cmd_add_project(args):
    p = admin.add_project_to_user(args.owner, args.name, args.description)
    print(f"Created project: {p.project_id} - {p.project_name} (owner {p.owner_id})")


def cmd_list_projects(args):
    projects = admin.list_projects(args.owner)
    for p in projects:
        print(f"{p.project_id}: {p.project_name} - {p.description} (owner {p.owner_id}) Tasks: {p.task_ids} Status: {p.status}")


def cmd_add_task(args):
    contributors = []
    if args.contributors:
        contributors = [int(x) for x in args.contributors.split(",") if x.strip()]
    t = admin.add_task_to_project(args.project, args.title, args.description, contributors)
    print(f"Created task: {t.task_id} - {t.title} (project {t.project_id})")


def cmd_list_tasks(args):
    tasks = admin.list_tasks(args.project)
    for t in tasks:
        print(f"{t.task_id}: {t.title} - {t.description} Project: {t.project_id} Completed: {t.completed} Contributors: {t.contributors}")


def cmd_complete_task(args):
    t = admin.complete_task(args.task_id)
    if t:
        print(f"Marked task {t.task_id} complete")
    else:
        print("Task not found")


def main():
    parser = argparse.ArgumentParser(prog="cli-tool")
    sub = parser.add_subparsers(dest="cmd")

    ucreate = sub.add_parser("user-create")
    ucreate.add_argument("username")
    ucreate.add_argument("email")
    ucreate.set_defaults(func=cmd_create_user)

    ulist = sub.add_parser("user-list")
    ulist.set_defaults(func=cmd_list_users)

    padd = sub.add_parser("project-add")
    padd.add_argument("owner", type=int)
    padd.add_argument("name")
    padd.add_argument("description", nargs="?", default="")
    padd.set_defaults(func=cmd_add_project)

    plist = sub.add_parser("project-list")
    plist.add_argument("owner", nargs="?", type=int)
    plist.set_defaults(func=cmd_list_projects)

    tadd = sub.add_parser("task-add")
    tadd.add_argument("project", type=int)
    tadd.add_argument("title")
    tadd.add_argument("description", nargs="?", default="")
    tadd.add_argument("--contributors", "-c", help="comma-separated user ids")
    tadd.set_defaults(func=cmd_add_task)

    tlist = sub.add_parser("task-list")
    tlist.add_argument("project", nargs="?", type=int)
    tlist.set_defaults(func=cmd_list_tasks)

    tcomp = sub.add_parser("task-complete")
    tcomp.add_argument("task_id", type=int)
    tcomp.set_defaults(func=cmd_complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        # If no args provided, run interactive numeric menu
        if len(sys.argv) == 1:
            interactive_menu()
        else:
            parser.print_help()
def interactive_menu():
    """Simple numeric menu for interactive use."""

    def ask_int(prompt):
        try:
            return int(input(prompt).strip())
        except Exception:
            return None

    while True:
        print("\nCLI Menu:\n1) Create user\n2) List users\n3) Add project\n4) List projects\n5) Add task\n6) List tasks\n7) Complete task\n0) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Bye")
            return
        if choice == "1":
            username = input("username: ").strip()
            email = input("email: ").strip()
            u = admin.create_user(username, email)
            print(f"Created user: {u.user_id} - {u.username} <{u.email}>")
            continue
        if choice == "2":
            for u in admin.list_users():
                print(f"{u.user_id}: {u.username} ({u.email}) Projects: {u.project_ids}")
            continue
        if choice == "3":
            owner = ask_int("owner id: ")
            name = input("project name: ").strip()
            desc = input("description: ").strip()
            p = admin.add_project_to_user(owner, name, desc)
            print(f"Created project: {p.project_id} - {p.project_name} (owner {p.owner_id})")
            continue
        if choice == "4":
            owner = input("owner id (leave blank for all): ").strip()
            owner_id = int(owner) if owner else None
            for p in admin.list_projects(owner_id):
                print(f"{p.project_id}: {p.project_name} - {p.description} (owner {p.owner_id}) Tasks: {p.task_ids} Status: {p.status}")
            continue
        if choice == "5":
            project = ask_int("project id: ")
            title = input("title: ").strip()
            desc = input("description: ").strip()
            contribs = input("contributors (comma-separated ids): ").strip()
            contributors = [int(x) for x in contribs.split(",") if x.strip()] if contribs else []
            t = admin.add_task_to_project(project, title, desc, contributors)
            print(f"Created task: {t.task_id} - {t.title} (project {t.project_id})")
            continue
        if choice == "6":
            project = input("project id (leave blank for all): ").strip()
            project_id = int(project) if project else None
            for t in admin.list_tasks(project_id):
                print(f"{t.task_id}: {t.title} - {t.description} Project: {t.project_id} Completed: {t.completed} Contributors: {t.contributors}")
            continue
        if choice == "7":
            tid = ask_int("task id: ")
            t = admin.complete_task(tid)
            if t:
                print(f"Marked task {t.task_id} complete")
            else:
                print("Task not found")
            continue
        print("Invalid choice")


if __name__ == "__main__":
    main()


