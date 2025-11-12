"""
CP1402 Project Management Program.
Estimated Time: 2hrs
Actual Time: 4 hr 20 minutes
"""
from project import Project
from datetime import datetime
from operator import attrgetter

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
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            print_projects_by_completion_status(projects, False)
            print_projects_by_completion_status(projects, True)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            projects.append(add_new_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    save = input(f"Would you like to save to {FILENAME}?").upper()
    if save == "Y":
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project-management software.")


def print_projects_by_completion_status(projects: list, is_complete: bool):
    """Output projects by completion status."""
    if is_complete:
        print("Complete projects:")
        filtered_projects = [project for project in projects if project.is_complete()]
    else:
        print("Incomplete projects:")
        filtered_projects = [project for project in projects if not project.is_complete()]
    filtered_projects.sort(key=attrgetter("priority"))
    display_projects(filtered_projects, False)


def add_initial_projects(lines: list[str], projects: list):
    """Append projects from file to list of project objects."""
    for line in lines:
        line = line.strip().split("\t")
        start_date = datetime.strptime(line[1], "%d/%m/%Y").date()  # Convert to date type.
        # Order of project attributes: name, start_date, priority, cost, completion_percentage.
        projects.append(Project(line[0], start_date, int(line[2]), float(line[3]), int(line[4])))


def load_lines(chosen_file):
    """Retrieve projects from file."""
    with open(chosen_file, 'r') as in_file:  # Assume file name is valid.
        # Ignore first line,as it is headings.
        in_file.readline()
        return in_file.readlines()


def load_projects(projects):
    """Load projects from a user chosen file."""
    try:
        chosen_file = input("Filename: ")
    except ValueError:
        return  # No file entered so return to menu.
    lines = load_lines(chosen_file)  # Assume first line is always headings.
    add_initial_projects(lines, projects)


def display_projects(projects, update):
    """Display projects in list.
    projects: list (of projects)
    update: Boolean (True if needed for updating, False if just displaying)."""

    for i, project in enumerate(projects):
        # Convert date to correct display format.
        project.start_date = datetime.strftime(project.start_date, "%d/%m/%Y")
        if update:
            placeholder = f"{i} "
        else:
            placeholder = " "
        print(f"{placeholder}{project}")
        project.start_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()  # Convert to date again.


def update_project(projects: list):
    """Update a specific project record."""
    display_projects(projects, True)
    try:
        project_choice = int(input("Project choice: "))
    except ValueError:
        return  # No valid project choice entered, so exit function.
    # Correct date format for outputting.
    projects[project_choice].start_date = datetime.strftime(projects[project_choice].start_date, "%d/%m/%Y")
    print(projects[project_choice])  # Print project details.
    # Convert back to date.
    projects[project_choice].start_date = datetime.strptime(projects[project_choice].start_date, "%d/%m/%Y").date()
    try:
        percentage = int(input("New Percentage: "))
    except ValueError:
        percentage = projects[project_choice].completion_percentage  # Retain original value.
    projects[project_choice].completion_percentage = percentage
    try:
        priority = int(input("New Priority: "))
    except ValueError:
        priority = projects[project_choice].priority  # Retain original value.
    projects[project_choice].priority = priority


def add_new_project():
    """Create a new project object."""
    print("Let's add a new project")
    name = get_valid_input("Name: ", str)
    start_date = get_valid_input("Start date (dd/mm/yy): ", str)
    start_date = datetime.strptime(start_date, "%d/%m/%Y").date()  # Convert to date type.
    priority = get_valid_input("Priority: ", int)
    cost_estimate = get_valid_input("Cost estimate: $", float)
    completion_percentage = get_valid_input("Percent complete: ", int)
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def get_valid_input(message, data_type):
    is_valid_input = False
    while not is_valid_input:
        try:
            response = data_type(input(f"{message}"))
            if response == "":
                print("Invalid input.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input.")
    return response


def filter_projects(projects):
    """Show projects completed on or after a specific date."""
    filter_date = get_valid_input("Show projects that start after date (dd/mm/yy): ", str)
    filter_date = datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=attrgetter("start_date"))
    display_projects(filtered_projects, False)


def save_projects(projects, filename):
    """Save projects to the specified file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  # File headings.
        for project in projects:
            # Correct date format for exporting.
            project.start_date = datetime.strftime(project.start_date, "%d/%m/%Y")
            print(project.export_project(), file=out_file)
            project.start_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()  # Convert to date again.


main()
