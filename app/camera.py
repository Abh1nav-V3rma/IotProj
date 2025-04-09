import os
import logging
import cv2

CAMERA_ENDPOINT = os.getenv('CAMERA_ENDPOINT')
OPTIONS = [
    "framesize",
    "led_intensity",
]

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    logging.error("Error opening camera.")
    exit(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# def modify_settings(key, value):
#     if key not in OPTIONS:
#         logging.error(f'Invalid camera setting: {key}')
#         return False
    
#     try:
#         response = get(f'{CAMERA_ENDPOINT}/control?var={key}&val={value}')
#         return response.status_code == 200
    
#     except Exception as err:
#         logging.error(f'Error configuring camera: {err}')
        # return False

def take_snapshot():
    try:
        ret, frame = cap.read()
        if ret:
            _, img_encoded = cv2.imencode('.jpg', frame)
            logging.info(f"Image shape: {img_encoded.shape}")
            logging.info(f"Image size: {img_encoded.size}")
            logging.info(f"Image type: {type(img_encoded)}")
            logging.info(f"Image dtype: {img_encoded.dtype}")
            return img_encoded.tobytes()
        else:
            logging.error("Failed to capture image.")
            return None
    
    except Exception as err:
        logging.error(f'Error taking snapshot: {err}')
        return None