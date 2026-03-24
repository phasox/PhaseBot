# PhaseBot

PhaseBot is a multi-feature Discord bot made by **PhaseDev**.

It uses a modular **cog-based** system, a dynamic per-server prefix system, a startup boot manager, and a DND rotating status that shows server and user counts. The main bot file loads every `.py` cog from the `src` folder automatically. :contentReference[oaicite:1]{index=1}

## Features

PhaseBot currently includes systems and modules for: admin tools, AFK, blacklist, casino, economy, help menu, invite command, server list, logging, mute, nuke, ping, ping detection, prefix management, snipe, tickets, verification, warnings, welcome/leave, and word detection. :contentReference[oaicite:2]{index=2}

Some highlighted features:
- **Dynamic prefixes** with a default prefix set in `config/prefix.py` and per-server prefixes stored in `data/prefixes.json`. :contentReference[oaicite:3]{index=3}
- **Economy system** with balances, daily rewards, and inventory data. :contentReference[oaicite:4]{index=4}
- **Mute system** with persistent storage and automatic unmute handling. :contentReference[oaicite:5]{index=5}
- **Snipe system** that stores deleted messages and keeps the latest 25 per channel. :contentReference[oaicite:6]{index=6}
- **Verification system** with setup and `verify_panel`. :contentReference[oaicite:7]{index=7}
- **Help menu** with grouped categories such as General, Config, and Moderation. :contentReference[oaicite:8]{index=8}

## Project Structure

```text
PhaseBot/
├── Main.py
├── requirements.txt
├── config/
│   ├── prefix.py
│   └── token.py
├── data/
└── src/
    ├── admin.py
    ├── afk.py
    ├── blacklist.py
    ├── casino.py
    ├── economy.py
    ├── help.py
    ├── inv.py
    ├── list.py
    ├── logs.py
    ├── mute.py
    ├── nuke.py
    ├── nukev2.py
    ├── ping.py
    ├── pingdetect.py
    ├── prefix.py
    ├── secret.py
    ├── snipe.py
    ├── ticket.py
    ├── verify.py
    ├── warn.py
    ├── welcome_leave.py
    └── world.py
````

This structure matches the current repository tree on the `main` branch. ([GitHub][1])

## Requirements

Install the current dependencies with:

```bash
pip install -r requirements.txt
```

Current requirements:

* `discord`
* `phasedb`
* `pillow` ([GitHub][2])

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/phasedev-oxiodev/PhaseBot.git
cd PhaseBot
```

### 2. Add your bot token

Open:

```python
config/token.py
```

and set:

```python
TOKEN = "YOUR_BOT_TOKEN"
```

The bot currently expects the token to be set there and exits if it is empty. ([GitHub][3])

### 3. Set the default prefix

Open:

```python
config/prefix.py
```

Example:

```python
DEFAULT_PREFIX = "!"
```

The bot uses this as the fallback prefix when a server does not have a custom one saved yet. ([GitHub][3])

### 4. Run the bot

```bash
python Main.py
```

`Main.py` starts the bot, loads all cogs from `src`, and starts the rotating DND presence loop after login. ([GitHub][3])

## Commands

PhaseBot’s help system currently groups commands into categories including:

* General
* Config
* Moderation
* and more custom sections inside the help cog. ([GitHub][4])

Example commands seen in the project:

* `ping`
* `help`
* `setprefix <prefix>`
* `setlog <#channel>`
* `setwelcome <#channel>`
* `setleave <#channel>`
* `setautorole <role>`
* `mute`
* `daily`
* `snipe`
* `verify_panel`
* `setroleword` ([GitHub][4])

## Notes

* The bot uses **all intents** in its current main file. ([GitHub][3])
* The default help command is disabled and replaced by a custom help system. ([GitHub][3])
* Prefixes are read from `data/prefixes.json`. ([GitHub][3])
* Several systems use JSON-based storage under the `data` folder. This is visible in modules like economy, snipe, and welcome/leave. ([GitHub][5])

## Credits

Made by **PhaseDev**. The startup output in `Main.py` also identifies the project as **PhaseBot** and includes a “Made By PhaseDev” line. ([GitHub][3])
