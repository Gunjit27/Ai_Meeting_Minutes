# AI Meeting Minutes Generator

Automate the process of **transcribing meetings** and **generating professional meeting minutes** using AI!

This project uses **CrewAI** and **OpenAI Whisper** to:
- Transcribe an audio recording of a meeting
- Summarize the meeting
- Extract action items
- Perform sentiment analysis
- Generate a complete, well-structured Meeting Minutes document in Markdown format

---

## Features

✅ Automatic transcription of audio meetings (using Whisper)  
✅ Summarization of main points discussed  
✅ Extraction of actionable tasks  
✅ Sentiment analysis of the meeting tone  
✅ Full meeting minutes document generation in Markdown  
✅ Modular CrewAI structure for easy customization and scaling

---

## How It Works

1. **Audio Transcription**: The meeting `.wav` file is transcribed using OpenAI Whisper.
2. **Text Analysis**: CrewAI agents summarize the transcript, extract action items, and perform sentiment analysis.
3. **Meeting Minutes Writing**: A final professional meeting minutes document is created, combining all outputs.
4. **Files are Saved**:
   - `summary.txt`
   - `action_items.txt`
   - `sentiment.txt`
   - `meeting_minutes.md`

---

## Project Structure

```bash
├── crews/
│   └── meeting_minutes_crew/
│       ├── meeting_minutes_crew.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
├── meeting_minutes/
│   └── (Generated output files will be stored here)
├── main_flow.py
├── .env
└── README.md

```

---

## Requirements

- Python 3.10+
- [CrewAI](https://docs.crewai.com/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [pydantic](https://docs.pydantic.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- ffmpeg (required by Whisper for audio processing)

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Gunjit27/ai_meeting_minutes.git
cd ai-meeting-minutes
```

2. **Install dependancies**:
```bash
pip install crewai
pip install "crewai[tools]"
pip install git+https://github.com/openai/whisper.git
```

3. **Install ffmpeg**:

Download ffmpeg and ensure it's added to your PATH.

4. **Set up environment variables**:

```bash
touch .env
```

Specify model
```bash
MODEL=gemini/gemini-1.5-flash
GEMINI_API_KEY=YOUR-API-KEY
```

## Usage

1. Place your `.wav` audio file (e.g., `EarningsCall.wav`) inside the base directory (`\ai_meeting_minutes` or update accordingly).

2. Run the project:

    ```bash
    python main.py
    ```

This will automatically:
- Transcribe the audio
- Generate summaries, action items, and sentiment analysis
- Create the final meeting minutes document

Outputs will be saved inside the `meeting_minutes/` folder.

---

## Configuration

Agent and Task configurations are located in YAML files:
- `config/agents.yaml`
- `config/tasks.yaml`

You can easily modify agent behaviors and task descriptions there without touching the main code!
