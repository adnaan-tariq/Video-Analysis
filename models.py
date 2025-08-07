from pydantic import BaseModel, Field

class VideoObject(BaseModel):
    """Pydantic schema for video analysis output."""
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