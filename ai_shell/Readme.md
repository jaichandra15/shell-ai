# 🧠 AI Natural Language Shell

A command-line tool that lets you use plain English to run Linux commands safely and interactively.  
Powered by an AI language model, it translates your requests into shell commands, reviews them for safety, and only executes them with your approval.

---

## 🚀 Features

- **🗣️ Natural Language Input** – Type what you want to do in English—no need to remember complex shell syntax.
- **🤖 AI-Powered Translation** – Converts your prompt into a Linux shell command.
- **🔒 Safety First** – Reviews generated commands for dangerous patterns before execution.
- **🛑 Interactive Confirmation** – Always asks before running any command.
- **🧩 Extensible Design** – Easily add features or integrate with different AI providers (OpenAI, Groq, etc.).

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-shell.git
cd ai-shell
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your API Key

Edit the `ai` script and set your API key for your AI provider (OpenAI, Groq, etc.).

```bash
export GROQ_API_KEY="your-api-key"  # or OPENAI_API_KEY
```

### 4. Make the Tool Executable

```bash
chmod +x ai
```

### 5. Add to Your PATH

```bash
mv ai ~/.local/bin/
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🧪 Usage

```bash
ai "Show all files modified today"
```

### 💬 Sample Interactive Output:

```text
Suggested command: find . -type f -newermt today
Execute this command? (y/n): y
Output:
./report.txt
./notes/meeting.txt
```

---

## 🎯 Interactive Points

- **Prompt** – Enter your request in plain English.
- **Review** – See the suggested shell command before it runs.
- **Approve or Cancel** – Type `y` to execute, `n` to cancel.
- **Error Feedback** – Get a clear message if the command is unsafe or fails.

---

## 🛠️ Troubleshooting

| Issue              | Solution                                                    |
|-------------------|-------------------------------------------------------------|
| Command not found | Ensure `ai` is in your PATH and is executable               |
| API errors         | Check your API key and internet connectivity                |
| Permission denied | Run `chmod +x ai` to make the script executable             |

---

## 🤝 Contributing

- Fork the repository and submit pull requests.
- Suggest features or improvements via [issues](https://github.com/jaichandra15/ai-shell/issues).

---

## 📄 License

This project is licensed under the **MIT License**.

---

**Enjoy a safer, smarter, and more intuitive Linux command-line experience!**
