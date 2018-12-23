# Technical tests Manager

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
  python ttm remove <email>
  ```

## Options:
  ```
  -h --help     Show this screen.
  --version     Show version.
  ```