# Ticketing System

A simple command-line ticketing system built in Python to practice object-oriented programming (OOP) concepts. Tickets are stored in a JSON file, simulating a basic database.

## Features

- Create, view, and list support tickets
- Assign priorities and agents
- Persistent storage using a JSON file
- Modular OOP design with models and repositories

## Project Structure

```
main.py                  # Main CLI application
/ticketing
    /models
        ticket.py        # Ticket class and status enum
    repositories.py      # TicketRepository for managing tickets
/tests
    ticket_test.py       # Unit tests
/tickets.json            # JSON file acting as the ticket database
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ticketingSystem
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install inquirer
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

- Follow the prompts to create, view, or list tickets.
- Tickets are saved in `tickets.json`.

## Testing

Run unit tests with:

```bash
python -m unittest discover tests
```

## Notes

- The ticket database (`tickets.json`) is ignored by git by default.
- This project is for learning and practice purposes.

## License

MIT License
