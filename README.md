# CurrencyRatesNotifier 📢💰

A Python-based currency exchange rate monitoring system that fetches real-time data from [Fixer.io](https://fixer.io/), archives rates, and sends notifications via email and SMS when predefined conditions are met.

## 🚀 Features
- ✅ Fetches live exchange rates from Fixer.io API.
- ✅ Archives exchange rates for historical reference.
- ✅ Sends email alerts when specified currencies meet defined thresholds.
- ✅ Sends SMS notifications for critical rate changes.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CurrencyRatesNotifier.git
   cd CurrencyRatesNotifier
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your settings in `config.py`:
   - Add your **Fixer.io API key**.
   - Set up **email SMTP** details.
   - Configure **SMS notification settings**.

## ⚡ Usage
Run the script manually:
```bash
python main.py
```
Or automate execution with a **cron job** (Linux) or **Task Scheduler** (Windows).

## 🛠 Configuration
Customize `config.py` for:
- **Email alerts** → Enable/disable & set preferred currencies.
- **SMS notifications** → Define min/max thresholds for alerts.
- **Archiving** → Store exchange rates for future reference.

### 🔧 Example `config.py`
```python
rules = {
    'archive': True,
    'email': {
        'enable': True,
        'preferred': ['USD', 'EUR', 'BTC']
    },
    'notification': {
        'enable': True,
        'preferred': {
            'USD': {'max': 1.1, 'min': 1.05},
            'BTC': {'max': 0.0000135, 'min': 0.00001}
        }
    }
}
```

## 🔒 Security Note
**Never expose API keys or credentials in public repositories.** Use environment variables instead.

## 🤝 Contributing
Feel free to fork this project and submit pull requests! Contributions are welcome. 💡

## 📜 License
This project is licensed under the MIT License.

