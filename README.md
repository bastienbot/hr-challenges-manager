# Technical tests Manager

## Description
This program allows you to register a new candidate, send the candidate the technical test (on gitlab: creates user, fork the test repository to his/her namespace, send the candidate an email with instructions), and save the email.

Upcoming:
- delete candidate
- show candidate infos
- set and get reminders so you can sent an email to a candidate who did not deliver his test result on time for instance

## Installation
```
git clone https://github.com/bastienbot/technical-tests-manager
cd technical-tests-manager
pip install -r requirement.txt
```

Copy and fill in the following files according to your needs :
- .env.exemple -> .env (your env constants)
- tt-informations.yaml.exemple -> tt-informations.yaml (informations about your tests repos)
- templates/\*.html.exemple -> templates/\*.html (email templates)

## Usage:
  ```
  python ttm send <firstname> <lastname> <email> <job>
  python ttm show <email>
  python ttm delete <email>
  ```

## Options:
  ```
  -h --help     Show this screen.
  --version     Show version.
  ```