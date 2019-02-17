# HR challenges Manager
WIP
## Description
This program allows you to register/delete a new candidate, send the registered candidate a technical challenge. This challenge can be sent with the following methods:
- sending an email
- create a user on gitlab and forking a project in the user namespace
You can also view informations about a registered candidate: name, email, messages sent

## Requirement
- Python 3.6 or over

## Installation
```
$ git clone https://github.com/bastienbot/hr-challenges-manager
$ cd hr-challenges-manager
```
Copy and fill in the following files according to your needs :
- .env.exemple -> .env (your env constants)
- app/tc-informations.yaml.exemple -> app/tc-informations.yaml (informations about your challenges repos)
- app/templates/\*.html.exemple -> app/templates/\*.html (email templates)
```
$ docker-compose build && docker-compose up
```

## Endpoimts:
  ```
  # /candidates
  POST, GET, PUT, DELETE : Standard CRUD

  # /challenges/preview
  POST : Preview a challenge before sending to a candidate

  # /challenges/preview
  POST : Send a challenge to a candidate
  ```

## Upcoming:
- set reminders so you can send an email to a candidate who did not deliver his/her challenge result on time for instance
- a feature that would help you correct a challenge based on pre-determined criterias