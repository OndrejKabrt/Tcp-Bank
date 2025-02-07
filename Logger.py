import json
import logging

with open('ipConfig.json', 'r') as f:
    config = json.load(f)
    logger_file = config['IP']['logger_file']

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=logger_file,
    filemode="a",
    encoding="utf-8"
)

def log_input(command, from_ip):
    logging.info(f"User from '{from_ip}' called '{command}'")

def log_output(message, to_ip):
    logging.info(f"User from '{to_ip}' recieved '{message}'")

def log_user_connected(from_ip):
    logging.info(f"User from '{from_ip}' have now connected")

def log_user_disconnected(from_ip):
    logging.info(f"User from '{from_ip}' have now disconnected")

