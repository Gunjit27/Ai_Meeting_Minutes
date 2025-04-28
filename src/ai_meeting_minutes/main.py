#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start
import whisper
import subprocess
from dotenv import load_dotenv
import os
from crews.meeting_minutes_crew.meeting_minutes_crew import MeetingMinutesCrew
load_dotenv()

class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""



class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating Transcription...")
        base_dir = r"D:\Projects\ai_meeting_minutes"
        file_name = "EarningsCall.wav"
        txt_file = os.path.splitext(file_name)[0] + ".txt"
        txt_path = os.path.join(base_dir, txt_file)

        if txt_file not in os.listdir(base_dir):
            print("Running Whisper...")
            subprocess.run(["whisper", os.path.join(base_dir, file_name), "--model", "medium.en"])

        with open(txt_path, "r", encoding="utf-8") as f:
            self.state.transcript = f.read()

        

        # file_path = r"D:\Projects\ai_meeting_minutes\meeting_minutes\transcript.txt"
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # with open(file_path, "w", encoding="utf-8") as f:
        #     f.write(self.state.transcript)


        print("Transcription complete.")
        print(self.state.transcript)
    
    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print("Generating Meeting Minutes...")
        crew = MeetingMinutesCrew()
        inputs = {
            "transcript": self.state.transcript,
        }
        meeting_minutes = crew.crew().kickoff(inputs)
        self.state.meeting_minutes = meeting_minutes

def kickoff():
    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.kickoff()


if __name__ == "__main__":
    kickoff()
