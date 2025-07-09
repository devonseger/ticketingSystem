import inquirer

if __name__ == "__main__":

    def main_menu():
        questions = [
            inquirer.List('choice',
                          message="Select an option.",
                          choices=['Create a Ticket', 'View Tickets', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions)


    while True:
        # Display open tickets?
        main_menu()
        # OPTIONS : View My Tickets, Accept a Ticket,

