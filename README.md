# Technical challenges Manager

## Description
This program allows you to register a new candidate, send the candidate the suitable challenge (on gitlab: creates user, fork the challenge repository to his/her namespace, send the candidate an email with instructions), and save the email.

Upcoming:
- delete candidate
- show candidate infos
- set and get reminders so you can sent an email to a candidate who did not deliver his/her challenge result on time for instance

## Requirement
- Python 3.6 or over

## Installation
```
git clone https://github.com/bastienbot/technical-challenges-manager
cd technical-challenges-manager
pip install -r requirement.txt
```

Copy and fill in the following files according to your needs :
- .env.exemple -> .env (your env constants)
- tc-informations.yaml.exemple -> tc-informations.yaml (informations about your challenges repos)
- templates/\*.html.exemple -> templates/\*.html (email templates)

## Usage:
  ```
  python hrcm send <firstname> <lastname> <email> <job>
  python hrcm show <email>
  python hrcm delete <email>
  ```

## Options:
  ```
  -h --help     Show this screen.
  --version     Show version.
  ```