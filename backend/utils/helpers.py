import time

def calculate_fps(start_time, end_time):
    """
    Calculate FPS from start and end time.
    """
    duration = end_time - start_time
    if duration == 0:
        return 0
    return 1.0 / duration

def get_timestamp():
    """
    Returns a clean timestamp string.
    """
    return time.strftime("%Y%m%d-%H%M%S")