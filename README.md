# Password Generator

## Overview

This is a simple command-line tool written in Python to generate random passwords. It allows users to specify the length and type of characters to include in the generated password.

## Installation

To use this tool, you need to have Python installed on your system. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/password-generator.git
```

## Usage

Go into the installation folder and then install the requirements with this command

```bash
pip install -r requirements.txt
```

Now, execute the script.

```bash
python genpasswd.py --length 15 --type aA1
```

### Options:

- `--length`: Specifies the length of the password (default is 15).
- `--type`: Specifies the type of characters to include in the password. You can choose from the following types:
  - `a`: Lowercase only
  - `aA`: All letters (lowercase and uppercase)
  - `aA1`: All letters and numbers
  - `aA1%`: Every character (including special characters)

## Example

Generate a password with a length of 12 characters and including lowercase and uppercase letters along with numbers:

```bash
python genpasswd.py --length 12 --type aA1
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
