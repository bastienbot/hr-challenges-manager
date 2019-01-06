# Technical challenges Manager

## Description
This program allows you to register/delete a new candidate, send the registered candidate a technical challenge. This challenge can be sent with the following methods:
- sending an email
- create a user on gitlab and forking a project in the user namespace
You can also view informations about a registered candidate: name, email, messages sent

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

## Upcoming:
- set reminders so you can send an email to a candidate who did not deliver his/her challenge result on time for instance