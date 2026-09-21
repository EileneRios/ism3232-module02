# ISM3232 - Module 2: zsh Navigation and File Operations

## Commands Practiced 

| Command      | What it does                             |
|--------------|------------------------------------------|
| pwd          | Print working directory, where am I?     | 
| ls           | List all files in current directory      | 
| ls -la       | List ALL files                           | 
| cd           | Changes to specific directory            | 
| cd ..        | Goes up one level                        | 
| cd ~         | Jump to home directory from anywhere     | 
| tree -L 2    | Visualise folder structure 2 levels deep | 
| code .       | Open current folder as VS Code workspace | 
| rm           | Removes file forever                     | 
| touch        | Creates new empty file                   | 
| python3      | Runs python script                       | 
| mv           | Renames or moves file                    | 

## AI Use Statement
I did not use AI for this lab.

## Week 3: Virtual Environments and .zshrc

| Command                       | What it does                                           |
|-------------------------------|--------------------------------------------------------|
| source .venv/bin/activate     | Activates the virtual environment                      |
| which python3                 | Shows which Python is currently active                 |
| pip install pytest ruff       | Installs packages                                      |
| pip list                      | Shows installed packages                               |
| pip freeze > requirements.txt | Writes installed packages to a file                    |
| cat requirements.txt          | Confirms the file was written                          |
| echo '.venv/' > .gitignore    | Creates a .gitignore file so .venv is never committed  | 
| gs='git status'               | Shortcut to check git status                           | 
| mkcd()                        | Custom function: creates a directory and moves into it |
| source ~/.zshrc               | Reloads the shell config so new aliases take effect    |
| pytest --collect-only         | Runs a quick test check with no tests yet              |
| deactivate                    | Exits the virtual environment                          |

## AI Use Statement
I did not use AI for this lab.
