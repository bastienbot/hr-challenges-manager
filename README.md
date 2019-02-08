# HR challenges Manager
WIP
<!-- ## Description
This program allows you to register/delete a new candidate, send the registered candidate a technical challenge. This challenge can be sent with the following methods:
- sending an email
- create a user on gitlab and forking a project in the user namespace
You can also view informations about a registered candidate: name, email, messages sent

## Requirement
- Python 3.6 or over

## Installation
```
git clone https://github.com/bastienbot/hr-challenges-manager
cd hr-challenges-manager
pip install -r requirement.txt
```

Copy and fill in the following files according to your needs :
- .env.exemple -> .env (your env constants)
- tc-informations.yaml.exemple -> tc-informations.yaml (informations about your challenges repos)
- templates/\*.html.exemple -> templates/\*.html (email templates)

## Usage:
  ```
  # Create a new candidate in db and send the suitable challenge
  python hrcm send <firstname> <lastname> <email> <job>

  # Archive a candidate
  python hrcm archive <email>

  # Show all candidates followed by last message date and time
  python hrcm candidates

  # Show informations about a specific candidate
  python hrcm show <email>

  # Delete candidate from DB
  python hrcm delete <email>
  ```

## Options:
  ```
  -h --help     Show this screen.
  --version     Show version.
  ```

## Upcoming:
- set reminders so you can send an email to a candidate who did not deliver his/her challenge result on time for instance -->