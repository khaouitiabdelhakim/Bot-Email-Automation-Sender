# Bot Email Automation Sender

This script allows you to send automated emails using a Gmail account. It uses the `smtplib` library to establish a secure connection to the SMTP server and the `email` library to create and send the email.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your machine
- A Gmail account with "Less Secure Apps" access enabled. You can enable this feature in your Gmail account settings.

## Installation

1. Clone or download the repository to your local machine.

2. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Open the `script.py` file in a text editor.

2. Modify the following variables according to your needs:

    - `sender`: A list containing your Gmail address and your name.
    - `receiver_email`: The email address of the recipient.
    - `message["Subject"]`: The subject of the email.
    - `message["From"]`: The name of the sender.
    - `html`: The HTML content of the email.

3. Save the changes.

4. Run the script by executing the following command:

    ```
    python script.py
    ```

    The script will prompt you to enter the password for your Gmail account.

5. The script will send the email and display a success message if the email is sent successfully. If there are any errors, the script will display an error message.

## Author

- Name: KHAOUITI ABDELHAKIM
- GitHub: [@khaouitiabdelhakim](https://github.com/khaouitiabdelhakim)

## License

This project is licensed under the [MIT License](LICENSE).
