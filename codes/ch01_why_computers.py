"""
ch01_why_computers.py

Small illustrative script for Chapter 1: shows basic printing and a
simple loop. Variable names are verbose and comments are explanatory.
"""

def print_greeting_multiple_times(
    name_to_print: str, number_of_times: int
) -> None:
    """Prints a greeting message `number_of_times` times."""
    for repetition_index in range(number_of_times):
        message_to_display = (
            f"Hello, {name_to_print}! "
            f"(line {repetition_index + 1})"
        )
        print(message_to_display)


if __name__ == "__main__":
    learner_preferred_name = "Learner"
    times_to_repeat_message = 5
    print("Starting the simple greeting program...")
    print_greeting_multiple_times(
        learner_preferred_name, times_to_repeat_message
    )
    print("Program finished.")
