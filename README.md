# Video Analysis with Google Gemini

A Python application that analyzes video content using Google's Gemini AI model to generate structured insights including titles, scene descriptions, and narrative explanations.

## Features

- **Video Processing**: Extract frames from video files using OpenCV
- **AI-Powered Analysis**: Leverage Google Gemini 1.5 Flash model for intelligent video analysis
- **Structured Output**: Get organized results with video titles, scene descriptions, and narrative explanations
- **Environment Configuration**: Secure API key management with environment variables
- **Modular Design**: Clean, maintainable code structure with separate modules for different functionalities

## Project Structure

```
Video-Analysis/
├── main.py                 # Main application entry point
├── config.py              # Configuration and environment variable handling
├── models.py              # Pydantic data models for structured output
├── prompts.py             # AI prompts and system messages
├── media_processing.py    # Video processing and frame extraction
├── model_invoker.py       # Google Gemini model integration
├── pyproject.toml         # Project dependencies and metadata
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore patterns
├── videos/               # Directory for input videos
│   └── sample.mp4        # Sample video file
└── README.md             # This file
```

## Prerequisites

- Python 3.8 or higher
- Google API key with Gemini access
- UV package manager (recommended) or pip

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adnaan-tariq/Video-Analysis.git
   cd Video-Analysis
   ```

2. **Install dependencies using UV (recommended)**:
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Getting Your Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key and add it to your `.env` file

## Usage

### Basic Usage

Run the application with the default sample video:

```bash
python main.py
```

### Command Line Arguments

The application currently processes the default sample video (`videos/sample.mp4`). You can modify the `video_path` variable in `main.py` to analyze different videos.

### Example Output

```
Video Analysis Result:

Video Title: Sample Video Analysis
Scene Description: A brief description of the key scenes and visual elements in the video
Narrative Explanation: A detailed explanation of the video's context, storyline, or purpose providing insights into what the video is about and its significance.
```

## Dependencies

- **langchain-google-genai**: Google Gemini integration for AI analysis
- **opencv-python**: Video processing and frame extraction
- **pydantic**: Data validation and structured output models
- **python-dotenv**: Environment variable management

## Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)

### Model Configuration

The application uses Google Gemini 1.5 Flash model with:
- Temperature: 0.5 (balanced creativity/consistency)
- Structured output using Pydantic models
- Image and text input support

## Development

### Project Structure

- **`main.py`**: Application entry point and orchestration
- **`config.py`**: Environment configuration and API key management
- **`models.py`**: Pydantic schemas for structured AI output
- **`prompts.py`**: AI prompts and system instructions
- **`media_processing.py`**: Video file processing and frame extraction
- **`model_invoker.py`**: Google Gemini model integration and invocation

### Adding New Video Formats

The application currently supports any video format that OpenCV can read. To add support for additional formats or processing options, modify the `process_video` function in `media_processing.py`.

### Customizing Analysis

You can customize the analysis by:
1. Modifying prompts in `prompts.py`
2. Updating the output schema in `models.py`
3. Adjusting model parameters in `model_invoker.py`

## Error Handling

The application includes comprehensive error handling for:
- Invalid video files or formats
- Missing or invalid API keys
- Network connectivity issues
- AI model response errors

## Security

- Environment variables are used for sensitive configuration
- API keys are loaded securely from `.env` files
- The `.env` file is excluded from version control via `.gitignore`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:
1. Check the error messages for specific guidance
2. Ensure your Google API key is valid and has Gemini access
3. Verify that your video file is in a supported format
4. Create an issue in the GitHub repository

## Roadmap

Future enhancements may include:
- Support for multiple video formats and processing options
- Batch processing capabilities
- Web interface for easier interaction
- Advanced analysis features (object detection, sentiment analysis)
- Export capabilities (JSON, CSV, PDF reports)