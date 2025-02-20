# Telegram Bot for Exchange Rates

This project is a Telegram bot that provides users with the current exchange rates for Baht to Ruble and USDT to Baht. The bot responds to specific commands in the chat to fetch and display the latest rates.

## Project Structure

```
telegram-bot
├── src
│   ├── bot.py                # Main entry point for the Telegram bot
│   ├── handlers
│   │   └── __init__.py       # Message handlers for the bot
│   ├── services
│   │   └── exchange_rate.py   # Functions to fetch exchange rates
│   └── utils
│       └── __init__.py       # Utility functions
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot by creating a new bot via the BotFather on Telegram and obtain your bot token.

4. Update the bot token in `src/bot.py`.

5. Run the bot:
   ```
   python src/bot.py
   ```

## Usage

- Send "курс рубля" to the bot to get the current exchange rate of Baht to Ruble.
- Send "курс USDT" to get the current exchange rate of USDT to Baht.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.