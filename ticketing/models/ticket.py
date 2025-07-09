from enum import Enum


class TicketStatus(Enum):
    OPEN = 0
    IN_PROGRESS = 1
    CLOSED = 2


class Ticket:
    def __init__(
            self,
            ticket_id,
            title,
            description,
            status: TicketStatus,
            created_at,
            updated_at,
            assigned_to,
            priority
    ):

        if isinstance(status, int):
            try:
                status = TicketStatus(status)
            except ValueError:
                raise ValueError(f"{status} is not a valid TicketStatus value.")
        elif not isinstance(status, TicketStatus):
            raise TypeError("status must be an int or TicketStatus enum.")

        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.assigned_to = assigned_to or "unassigned"
        self.priority = priority

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.value,  # Store as int for serialization
            "created_at": self.created_at,
            "assigned_to": self.assigned_to,
            "priority": self.priority
        }

    def update_status(self, updated_status):
        if isinstance(updated_status, int):
            try:
                updated_status = TicketStatus(updated_status)
            except ValueError:
                raise ValueError(f"{updated_status} is not a valid TicketStatus value.")
        elif not isinstance(updated_status, TicketStatus):
            raise TypeError("updated_status must be an int or TicketStatus enum")

        self.status = updated_status

    def assign_agent(self):
        pass
