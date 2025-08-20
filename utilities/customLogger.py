import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_path = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        log_file = os.path.join(log_path, "automation.log")

        # Clear old handlers (important for pytest reruns)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Create file handler explicitly
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            handlers=[
                logging.FileHandler(log_file, mode="a"),
                logging.StreamHandler()  # optional: also show in console
            ]
        )

        logger = logging.getLogger()
        return logger
