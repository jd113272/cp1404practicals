"""
CP1402 Project Management Program.
Estimated Time: 2hrs
Actual Time: 1 hr 46 minutes (STARTED: 4:14PM ENDED: PM)
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
    lines = load_lines(FILENAME)
    projects = []
    add_initial_projects(lines, projects)
    print(f"Welcome to Pythonic Project Management \n"
          f"Loaded {len(projects)} from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(projects)
        elif choice == "S":
            # TODO: Save projects
            pass
        elif choice == "D":
            print_projects_by_completion_status(projects)
        elif choice == "F":
            # TODO: Filter projects by date
            pass
        elif choice == "A":
            projects.append(add_new_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()


def print_projects_by_completion_status(projects: list):
    """Collate and output all incomplete and complete projects."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    display_projects(incomplete_projects, False)

    print("Completed projects:")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    display_projects(complete_projects, False)


def add_initial_projects(lines: list[str], projects: list):
    """Append projects from file to list of project objects."""
    for line in lines:
        line = line.strip().split("\t")
        # Order: name, start_date, priority, cost, completion_percentage
        projects.append(Project(line[0], line[1], int(line[2]), float(line[3]), int(line[4])))


def load_lines(chosen_file):
    """Retrieve projects from file."""
    with open(chosen_file, 'r') as in_file:
        # Ignore first line,as it is headings
        in_file.readline()
        return in_file.readlines()


def load_projects(projects):
    """Load projects from a user chosen file."""
    chosen_file = input("Filename: ")
    # Assume first line is always headings
    lines = load_lines(chosen_file)
    add_initial_projects(lines, projects)


def display_projects(projects, update):
    """Display projects in list.
    projects: list (of projects)
    update: Boolean (True if needed for updating, False if just displaying)"""

    for i, project in enumerate(projects):
        if update:
            placeholder = f"{i} "
        else:
            placeholder = " "
        print(f"{placeholder}{project}")


def update_project(projects):
    """Update a specific project record."""
    display_projects(projects, True)
    try:
        project_choice = int(input("Project choice: "))
    except ValueError:
        return  # No valid project choice entered
    print(projects[project_choice])

    try:
        percentage = int(input("New Percentage: "))
    except ValueError:
        percentage = projects[project_choice].completion_percentage
    projects[project_choice].completion_percentage = percentage
    try:
        priority = int(input("New Priority: "))
    except ValueError:
        priority = projects[project_choice].priority
    projects[project_choice].priority = priority


def add_new_project():
    """Create a new project object."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = int(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


main()
