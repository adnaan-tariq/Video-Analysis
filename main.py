import argparse
from config import load_config
from models import VideoObject
from prompts import SYSTEM_PROMPT, VIDEO_PROMPT
from media_processing import process_video
from model_invoker import invoke_model

def main():
    """Main function to orchestrate video analysis."""
    # Load configuration
    api_key = load_config()
    
    video_path = "videos/sample.mp4"
    
    # Process video
    try:
        video_base64 = process_video(video_path)
    except Exception as e:
        print(f"Video Processing Error: {str(e)}")
        return
    
    # Invoke model
    try:
        response = invoke_model(api_key, VIDEO_PROMPT, video_base64, VideoObject)
        # Output structured result
        print("Video Analysis Result:")
        print("\nVideo Title:", response.video_title)
        print("\nScene Description:", response.scene_description)
        print("\nNarrative Explanation:", response.narrative_explanation)
        print("\n")
    except Exception as e:
        print(f"Model Invocation Error: {str(e)}")

if __name__ == "__main__":
    main()