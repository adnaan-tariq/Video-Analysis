from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

def invoke_model(api_key, prompt, media_base64, VideoObject):
    """Initialize and invoke Gemini model with structured output."""
    try:
        # Initialize Gemini model
        model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.5
        ).with_structured_output(VideoObject)
        
        # Prepare messages
        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=[
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{media_base64}"}
            ])
        ]
        
        # Invoke model
        response = model.invoke(messages)
        return response
    except Exception as e:
        raise Exception(f"Error invoking model: {str(e)}")