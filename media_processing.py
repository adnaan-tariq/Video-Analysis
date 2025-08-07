import cv2
import base64
from io import BytesIO

def process_video(video_path):
    """Process video file and return base64-encoded frame."""
    try:
        # Open video file using OpenCV
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("Unable to open video file")
        
        # Read the first frame
        ret, frame = cap.read()
        if not ret:
            raise ValueError("Unable to read video frame")
        
        # Convert frame to JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        video_data = BytesIO(buffer)
        video_base64 = base64.b64encode(video_data.getvalue()).decode('utf-8')
        
        # Release video capture
        cap.release()
        return video_base64
    except Exception as e:
        raise Exception(f"Error processing video: {str(e)}")