from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

transcripts_folder = "transcripts"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(transcripts_folder):
    if filename.endswith(".txt"):
        transcript_file = os.path.join(transcripts_folder, filename)
        transcript_name = os.path.splitext(filename)[0]

        with open(transcript_file, "r") as file:
            transcript_content = file.read()

        issues_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are analyzing an interview from a past inmate. Please extract the issues they have mentioned in this interview. Purely only mention issues and not the solutions  "},
                {"role": "user", "content": transcript_content}
            ]
        )

        issues_output_path = os.path.join(output_folder, transcript_name, "issues.txt")
        os.makedirs(os.path.join(output_folder, transcript_name), exist_ok=True)
        issues_content = issues_response.choices[0].message.content
        with open(issues_output_path, "w") as issues_file:
            issues_file.write(issues_content)

        print("Issues response saved to:", issues_output_path)

        solutions_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are analyzing an interview from a past inmate. Please extract the solutions they have mentioned in this interview. Purely only mention solutions and not the issues "},
                {"role": "user", "content": transcript_content}
            ]
        )

        solutions_output_path = os.path.join(output_folder, transcript_name, "solutions.txt")
        solutions_content = solutions_response.choices[0].message.content
        with open(solutions_output_path, "w") as solutions_file:
            solutions_file.write(solutions_content)

        print("Solutions response saved to:", solutions_output_path)
