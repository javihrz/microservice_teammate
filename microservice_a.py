import time
import os


def write_initial_goal(file_path):
    """
    Writes $0.00 to file if empty.
    """
    with open(file_path, "w") as text_file:
        text_file.write("$0.00")


def get_prev_goal(file_path):
    """
    Converts final line from text file to a truncated string, then to a float.
    """
    with open(file_path, "r") as text_file:
        prev_goal = text_file.readlines()[-1]
        prev_goal = prev_goal.split()[0]
        prev_goal = float(prev_goal[1:])  # Drops '$'.

        return prev_goal


def get_goal_addition(file_path):
    """
    Gets the user's input from the text file.
    """
    with open(file_path, "r") as text_file:
        add_to_goal = float(text_file.read())

    open(file_path, "w").close()  # Clears text file for future use.

    return add_to_goal


def log_goal(prev_goal, add_to_goal):
    """
    A new savings goal is amended into the logging text file.
    """
    file_size_log = os.stat(log_path).st_size

    if file_size_log == 0:
        write_initial_goal(log_path)

    new_goal = round(prev_goal + add_to_goal, 2)
    new_goal = "$" + f"{new_goal:.2f}"

    add_to_goal = "$" + f"{add_to_goal:.2f}"
    side_info = f"(+{add_to_goal} from previous goal)"

    with open(log_path, "a") as text_file:
        text_file.write(f"\n{new_goal} {side_info}")


def get_values():
    """
    Gets the string values from two different text files.
    """
    prev_goal = get_prev_goal(log_path)
    add_to_goal = get_goal_addition(comm_path)

    return prev_goal, add_to_goal


if __name__ == '__main__':
    comm_path = "comm_pipe.txt"
    log_path = "savings_log.txt"

    file_size_goal = os.stat(comm_path).st_size

    while True:
        time.sleep(3)
        file_size_goal = os.stat(comm_path).st_size

        if file_size_goal != 0:
            file_values = get_values()
            log_goal(file_values[0], file_values[1])

            print("New savings goal logged.")
