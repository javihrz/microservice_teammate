import os
import time


def get_user_input():
    """
    Gets the user input. Loops until a valid input is submitted.
    """
    print("Type 'q' to quit the program, or 'g' to log a savings goal.")

    while True:
        user_input = input("Input: ")

        if user_input == "q":
            quit()
        elif user_input == "g":
            return
        else:
            print("\nInvalid input. Please try again.")


def initial_message():
    """
    Determines the initial message(s) to print while starting the program.
    """
    file_size = os.stat(log_path).st_size

    if file_size == 0:
        print("Please input a float value (ex: 50.00) to log your first savings goal.")

    else:
        prev_goal = get_prev_goal(log_path)
        print(f"\nPrevious savings goal was {prev_goal}.")
        print("\nPlease input a positive integer (ex: 10) or "
              "float (ex: 10.00) increase the savings goal.")


def get_num_rows(file_path):
    """
    Returns the total number of lines in a text file.
    """
    with open(file_path, "r") as text_file:
        all_lines = text_file.readlines()

    return len(all_lines)


def get_prev_goal(file_path):
    """
    Converts final line from a text file to a truncated string.
    """
    with open(file_path, "r") as text_file:
        goal_string = text_file.readlines()[-1]
        goal_string = goal_string.split()[0]

        return goal_string


def log_goal():
    """
    Writes to a text file the user's new saving goal.
    Loops until a valid input (positive float) is submitted.
    """
    while True:
        try:
            user_input = float(input("Input: "))

            if user_input <= 0:
                print("\nInvalid input. Please submit a positive integer (ex: 10)"
                      "or float (ex: 10.00) to continue.")
                continue
            break

        except ValueError:
            print("\nInvalid input. Please submit a positive integer (ex: 10)"
                  " or float (ex: 10.00) to continue.")

    with open(comm_path, "w") as text_file:
        text_file.write(str(user_input))

    print(f"\nRequest to update savings goal by ${user_input} has been submitted. Please hold.")


if __name__ == '__main__':
    comm_path = "comm_pipe.txt"
    log_path = "savings_log.txt"
    old_line_count = get_num_rows(log_path)

    get_user_input()
    initial_message()
    log_goal()

    while True:
        time.sleep(3)
        new_line_count = get_num_rows(log_path)

        if new_line_count > old_line_count:
            print(f"\nSavings goal has now been updated to be {get_prev_goal(log_path)}.")
            quit()
