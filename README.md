# SMS Bomber

SMS Bomber is a simple Python script designed for educational purposes to demonstrate the potential misuse of such tools. It allows users to send a large number of OTP (One-Time Password) requests to a specified phone number, simulating a form of SMS bombing.

**Disclaimer:** This script should only be used in a responsible and ethical manner. Any unauthorized use for malicious activities is strictly prohibited.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Minimum Requirements](#minimum-requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Sends multiple OTP requests to a specified phone number.
- Demonstrates a potential misuse scenario for educational purposes.

## How It Works

The SMS Bomber script uses a verification API to check the validity of the target phone number. If the number is valid, it obtains a secret token and performs a bombing attempt by sending OTP requests to the target number.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PrantaDas/sms-bomber.git
    ```

2. Change to the project directory:

    ```bash
    cd sms-bomber
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Minimum Requirements

- Python 3.x
- Requests library
- dotenv library

## Usage

1. Edit the `.env` file and provide the required environment variables:

    ```env
    BASE_URl=" https://web-api.banglalink.net/api/v1"
    ```

2. Run the script:

    ```bash
    python src/__main__.py
    ```

3. Follow on-screen instructions to start the bombing process.

**Note:** This script is for educational purposes only. Be responsible and use it ethically.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Please adhere to the [Code of Conduct](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct).

## License

This project is licensed under the [MIT License](https://github.com/PrantaDas/sms-bomber/blob/main/LICENSE).


## Acknowledgements
Inspired by [Rakibul Yeasin](https://github.com/dreygur)