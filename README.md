# A very Human-like AI Telegram Bot

A highly customizable, realistic AI Telegram bot powered by Google's Gemini 2.0 Flash. This bot is designed to mimic human interaction patterns, including realistic typing delays and natural message splitting.

## Key Features: "It feels like a real person"

The main goal of this project is to create a bot that doesn't feel like a bot. It achieves this through two core mechanisms:

### 1. Natural Message Splitting
Unlike standard bots that send a single wall of text, this bot understands how to break down thoughts into multiple messages.

**How it works:**
If you instruct the bot in the `system_prompt.txt` to "split messages with newlines," it will generate a response like:

```
Hey!
I was just thinking about that.
Let me check for you.
```

The bot's handler detects these newlines and sends them as three separate messages, just like a human would text.

### 2. Realistic Typing Delays
It doesn't just blast messages instantly. The bot calculates a "typing delay" based on the length of each message chunk.

- **Dynamic Calculation**: It estimates how long a fast typer (e.g., a teenager) would take to type the message.
- **Visual Feedback**: It displays the "typing..." status in Telegram while it "types" the message.
- **Random Variance**: Adds a slight random factor to the delay so it never feels robotic or perfectly consistent.

## 🚀 How It Works

The bot is built with **Python**, **python-telegram-bot**, and **Google GenAI**.

1.  **Message Reception**: Listens for messages in private chats or mentions in groups.
2.  **AI Generation**: We use the **Google GenAI** api to generate a response. Sends the conversation history and user input to Gemini 2.0 Flash (or the model you choose).
3.  **Processing**:
    - The AI generates a response (potentially multi-line).
    - The bot splits the response by newlines.
4.  **Delivery Loop**:
    - For each message part:
        - Calculates delay: `len(text) / chars_per_second * random_variance`.
        - Sends "Typing..." action.
        - Waits for the calculated delay.
        - Sends the message.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    - Rename `.env.example` to `.env`.
    - Add your API keys:
      ```env
      TELEGRAM_BOT_TOKEN=your_telegram_token
      GOOGLE_API_KEY=your_google_api_key
      GOOGLE_MODEL_NAME=gemini-2.0-flash # Optional, defaults to gemini-2.0-flash
      ```

## ⚙️ Configuration

### System Prompt (`data/system_prompt.txt`)
This is the brain of the bot. You can define its personality, tone, and behavior here.

**To enable the realistic splitting feature, include instructions like:**
> "Write as if you are texting a friend. Use short messages. Separate distinct thoughts with newlines."

### History
Chat histories are automatically saved in `data/histories/` as JSON files, ensuring the bot remembers context across conversations.

## 🖥️ Usage

Run the bot with:

```bash
python main.py
```

The bot will start polling for Telegram messages. It also starts a lightweight Flask server on port 5000 (useful for keeping the bot alive on some hosting platforms).

## 👨‍💻 Author

Created by **Emanuele Faraci**.

Check out my portfolio: [emanuelefaraci.com](https://emanuelefaraci.com)
