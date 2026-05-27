# Password Manager
A local, command-line password manager built in Python. All credentials are encrypted and stored on your machine.

<br>

## Features

- Add, retrieve, update, and delete password entries for any site.
- Passwords copied to clipboard on retrieval - never displayed on screen.
- Secure password generator for creating strong random passwords.
- Vault encrypted with AES - all data stored locally, no cloud sync.
- Master password never stored - derived into an encryption key at runtime.
- Unique salt per vault prevents pre-computed password attacks.

## Setup Instructions

**Prerequisites:** Python 3.10+
**1. Clone the repository:**
```
git clone https://github.com/smallik1029/password-manager.git
cd password-manager
```

**2. Install dependencies**
```
pip install -r requirements.txt
```

**3. Run**
```
python main.py
```

On first run, you will be prompted to create a master password and a new vault will be created.
For clarity, when you are typing any password (such as master password or site-specific password), the program will not display the letters as you type them for privacy reasons. Just type and press enter as normal.

## Usage

Run the program once and type commands at the prompt:

```
python main.py
```

### `add`
Add a new entry. You will be prompted for a site, username, and password. You can either type the password yourself or generate a strong random one. 
```
> add
Site: site.com
Username: user
Generate password? (y/n): y
Generated: l/uKj:J|0&$bgR>|
Entry for site.com saved.
```
**OR**
```
> add
Site: site.com
Username: user
Generate password? (y/n): n
Password:
Entry for site.com saved.
```
### `get <site>`
Retrieve an entry. The password will be copied to your clipboard so that other people cannot see your password by looking at your screen. 
```
> get site.com
Site:     site.com
Username: user
Password: copied to clipboard
Created:  2026-05-26 19:27:11 Pacific Daylight Time
```
### `list`
List all saved sites.
```
> list
  - site.com
```
### `update <site>`
Update the username and password for an existing entry.
```
> update site.com
New username: new_username
New password:
Entry for site.com successfully updated.
```
### `delete <site>`
Delete an entry.
```
> delete site.com
Entry for site.com deleted.
```
### `exit`
Lock the vault and exit the program.
```
> exit
```
