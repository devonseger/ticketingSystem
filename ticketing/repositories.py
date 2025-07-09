from ticketing.models import ticket
import json
import os

TICKETS_DB = "tickets.json"


class TicketRepository:
    def __init__(self):
        self.tickets = {}
        self.load_tickets()

    def add_ticket(self, ticket):
        if ticket.ticket_id in self.tickets:
            raise ValueError("Ticket ID already exists.")
        self.tickets[ticket.ticket_id] = ticket
        self.save_tickets()

    def load_tickets(self):
        if os.path.exists(TICKETS_DB):
            with open(TICKETS_DB, 'r') as file:
                data = json.load(file)
                for ticket_data in data:
                    try:
                        ticket_obj = ticket.Ticket(
                            ticket_id=ticket_data['ticket_id'],
                            title=ticket_data['title'],
                            description=ticket_data['description'],
                            status=ticket.TicketStatus(ticket_data['status']),
                            created_at=ticket_data['created_at'],
                            updated_at=ticket_data['updated_at'],
                            assigned_to=ticket_data['assigned_to'],
                            priority=ticket_data['priority']
                        )
                        self.tickets[ticket_obj.ticket_id] = ticket_obj
                    except KeyError as e:
                        print(f"Error loading ticket data: Missing key {e} in {ticket_data}")
        else:
            print("No existing tickets found. Starting with an empty repository.")
            # Create the file if it doesn't exist
            with open(TICKETS_DB, 'w') as file:
                json.dump([], file)
                
    def save_tickets(self):
        with open(TICKETS_DB, "w") as f:
            json.dump([t.to_dict() for t in self.tickets.values()], f, indent=2)

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id)

    def get_all_tickets(self):
        return self.tickets

    def update_ticket(self, ticket):
        pass
