import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_wrapper(func):
    def wrapper(*args, **kwargs):
        instance_name = args[0].__class__.__name__
        method_name = func.__name__
        
        try:
            logging.info(f"Executing {method_name} in {instance_name}")
            result = func(*args, **kwargs)
            logging.info(f"{method_name} completed successfully")
            return result
        except Exception as e:
            error_message = f"Error in {method_name} of {instance_name}: {str(e)}"
            logging.error(error_message)
            raise
    return wrapper