import unittest
from datetime import datetime
from ticketing.models.ticket import Ticket, TicketStatus  # Adjust import as needed


class TestTicket(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now()

    def test_ticket_creation_with_enum_status(self):
        ticket = Ticket(
            ticket_id=1,
            title="Login Bug",
            description="User cannot log in",
            status=TicketStatus.OPEN,
            created_at=self.now,
            updated_at=self.now,
            assigned_to=None,
            priority="high"
        )
        self.assertEqual(ticket.status, TicketStatus.OPEN)
        self.assertEqual(ticket.assigned_to, "unassigned")
        self.assertEqual(ticket.priority, "high")

    def test_ticket_creation_with_int_status(self):
        ticket = Ticket(
            ticket_id=2,
            title="UI Issue",
            description="Button not clickable",
            status=1,  # Should convert to TicketStatus.IN_PROGRESS
            created_at=self.now,
            updated_at=self.now,
            assigned_to="agent1",
            priority="low"
        )
        self.assertEqual(ticket.status, TicketStatus.IN_PROGRESS)
        self.assertEqual(ticket.assigned_to, "agent1")

    def test_invalid_status_type(self):
        with self.assertRaises(TypeError):
            Ticket(
                ticket_id=3,
                title="Bad Data",
                description="Status is a string",
                status="open",  # Invalid type
                created_at=self.now,
                updated_at=self.now,
                assigned_to=None,
                priority="medium"
            )

    def test_invalid_status_value(self):
        with self.assertRaises(ValueError):
            Ticket(
                ticket_id=4,
                title="Out of range",
                description="Status = 99",
                status=99,  # Invalid int
                created_at=self.now,
                updated_at=self.now,
                assigned_to=None,
                priority="medium"
            )


if __name__ == '__main__':
    unittest.main()
