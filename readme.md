# Endpoint Availability Monitor

This script periodically checks the availability of an API endpoint and sends an SMS notification if the endpoint goes down or comes back online.

## Features
- Checks the availability of a specified API endpoint.
- Sends SMS notifications using Twilio when the endpoint status changes.
- Uses environment variables for configuration (stored in `.env`).

## Prerequisites
- Python 3.11
- Twilio account (for sending SMS notifications)
- `python-dotenv` package (for loading environment variables)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
    ```
2. Run the project
    ```bash
    nix-shell --run "python app.py"
    ```
    