import inquirer
from ticketing.models.ticket import Ticket as TicketModel
from ticketing.repositories import TicketRepository

# Initialize the ticket repository
repo = TicketRepository()

def create_ticket():
    title = input("Please enter the Ticket Title: ")
    description = input("Please enter the Ticket Description: ")
    priority = input("Please enter the Ticket Priority (low, medium, high): ")
    
    # Create a new ticket instance
    ticket = TicketModel(
        ticket_id=len(repo.tickets) + 1,  # Simple ID generation
        title=title,
        description=description,
        status=0,  # Open by default
        created_at="2023-10-01",  # Placeholder for created_at
        updated_at="2023-10-01",  # Placeholder for updated_at
        assigned_to=None,
        priority=priority
    )
    
    repo.add_ticket(ticket)
    print(f">> Ticket '{title}' created successfully.")
    print(f"Ticket ID: {ticket.ticket_id}")


def view_ticket():
    ticket_id = input("Please enter the Ticket ID.")
    print(f">> Attempting to view ticket number {ticket_id}")
    ticket = repo.get_ticket(ticket_id)
    if ticket:
        print(f"Ticket ID: {ticket.ticket_id}")
        print(f"Title: {ticket.title}")
        print(f"Description: {ticket.description}")
        print(f"Status: {ticket.status.name}")
        print(f"Created At: {ticket.created_at}")
        print(f"Updated At: {ticket.updated_at}")
        print(f"Assigned To: {ticket.assigned_to}")
        print(f"Priority: {ticket.priority}")


def view_all_tickets():
    tickets = repo.get_all_tickets()
    if tickets:
        for ticket in tickets.values():
            print(f"Ticket ID: {ticket.ticket_id}, Title: {ticket.title}, Status: {ticket.status.name}")
    else:
        print("No tickets found.")


def exit_program():
    print(">> Goodbye.")
    exit(0)


def accept_ticket(ticket_id):
    print(f"Attempting to accept ticket {ticket_id}")


def main_menu():
    questions = [
        inquirer.List('choice',
                      message="Select an option.",
                      choices=['Accept Ticket', 'Create a Ticket', 'View Ticket', 'View all Tickets', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['choice']


menu_actions = {
    'Create a Ticket': create_ticket,
    'View Ticket': view_ticket,
    'Accept a Ticket': accept_ticket,
    'View all Tickets': view_all_tickets,
    'Exit': exit_program
}


if __name__ == "__main__":

    while True:
        # Call the menu function and store choice
        choice = main_menu()
        # define action by getting the choice from the action menu
        action = menu_actions.get(choice)
        # if there's a valid selection run that function
        if action:
            action()
            # action should translate to the function name from menu_actions
        else:
            print("Invalid choice.")
