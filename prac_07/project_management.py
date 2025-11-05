"""
CP1402 Project Management Program.
Estimated Time: 2hrs
Actual Time: 26 minutes (STARTED: 4:46PM ENDED: PM)
"""
from project import Project

MENU = ("- (L)oad projects \n"
        "- (S)ave projects \n"
        "- (D)isplay projects \n"
        "- (F)ilter projects by date \n"
        "- (A)dd new project \n"
        "- (U)pdate project \n"
        "- (Q)uit")
FILENAME = "projects.txt"


def main():
    """Run the Project Management program."""
    lines = load_lines()
    projects = []
    add_initial_projects(lines, projects)
    print(f"Welcome to Pythonic Project Management \n"
          f"Loaded {len(projects)} from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # TODO: Load projects
            pass
        elif choice == "S":
            # TODO: Save projects
            pass
        elif choice == "D":
            # TODO: Display projects
            pass
        elif choice == "F":
            # TODO: Filter projects by date
            pass
        elif choice == "A":
            # TODO: Add new project
            pass
        elif choice == "U":
            # TODO: Update project
            pass
        else:
            # TODO: Error message
            pass
        print(MENU)
        choice = input(">>> ").upper()


def add_initial_projects(lines: list[str], projects: list):
    """Append projects from file to list of project objects."""
    for line in lines:
        line = line.strip().split("\t")
        projects.append(Project(line[0], line[1], line[2], line[3], line[4]))


def load_lines():
    """Retrieve projects from file."""
    with open(FILENAME, 'r') as in_file:
        # Ignore first line,as it is headings
        in_file.readline()
        return in_file.readlines()

main()
