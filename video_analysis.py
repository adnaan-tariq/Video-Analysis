import os
from dotenv import load_dotenv
import base64
from io import BytesIO
import cv2  # For video processing
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Prompt for Google API key if not set
if not os.environ.get("GOOGLE_API_KEY"):
    import getpass
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Gemini API Key: ")

# Define video-specific prompt
VIDEO_PROMPT = """
Analyze the provided video and return a structured response with:
- video_title: A concise title for the video (max 50 characters).
- scene_description: A description of key scenes (50-150 characters).
- narrative_explanation: An explanation of the video's context or narrative (3-5 sentences).
"""

# Define Pydantic schema for video analysis
class VideoObject(BaseModel):
    video_title: str = Field(
        max_length=50,
        description="Title of the video"
    )
    scene_description: str = Field(
        min_length=50,
        max_length=150,
        description="Description of key scenes in the video"
    )
    narrative_explanation: str = Field(
        description="Explanation of the video's context or narrative"
    )

# Function to process video and extract a frame for analysis
def process_video(video_path):
    try:
        # Open video file using OpenCV
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("Unable to open video file")
        
        # Read the first frame (or extract key frames as needed)
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

# Load and encode video
video_path = "videos/sample.mp4"  # Update to your video file path
try:
    video_base64 = process_video(video_path)
except Exception as e:
    print(f"Video Processing Error: {str(e)}")
    exit(1)

# Initialize Gemini model (use gemini-1.5-flash for video support)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Updated to correct model name
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0  # Ensure deterministic output
).with_structured_output(VideoObject)

# Prepare messages for video analysis
messages = [
    SystemMessage(content="You are a helpful video analysis assistant."),
    HumanMessage(content=[
        {"type": "text", "text": VIDEO_PROMPT},
        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{video_base64}"}  # Using frame as image
    ])
]

# Get response with error handling
try:
    response = model.invoke(messages)
    # Output structured result
    print("\nVideo Title:", response.video_title)
    print("\nScene Description:", response.scene_description)
    print("\nNarrative Explanation:", response.narrative_explanation)
except Exception as e:
    print(f"Error invoking model: {str(e)}")