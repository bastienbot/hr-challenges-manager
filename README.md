# Technical tests Manager

## Installation
```
git clone https://github.com/bastienbot/technical-tests-manager
cd technical-tests-manager
pip install -r requirement.txt
```

Copy and fill in the following files according to your needs :
- .env.exemple -> .env (your env constants)
- tt-informations.exemple.yaml -> tt-informations.exemple.yaml (informations about your tests repos)
- templates/\*.exemple.txt -> templates/\*.txt (email templates)

## Usage:
  ```
  python ttm send <firstname> <lastname> <email> <job>
  python ttm show <email>
  python ttm remove <email>
  ```

## Options:
  ```
  -h --help     Show this screen.
  --version     Show version.
  ```