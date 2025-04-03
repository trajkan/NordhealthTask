from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import json


class DischargeNoteGenerator:
    """
    A class to generate discharge notes for veterinary consultations using a language model.
    """
    def __init__(self):
        self.hf_token = self.load_token()
        self.client = self.create_client()

    def load_token(self):
        """
        Load the Hugging Face token from the environment variable. requires a .env file with HF_TOKEN variable.
        """
        load_dotenv()
        hf_token = os.getenv("HF_TOKEN")
        if not hf_token:
            raise ValueError("Please set the HF_TOKEN environment variable.")
        return hf_token


    def create_client(self):
        """
        Create an InferenceClient instance using the Hugging Face token.
        """
        client = InferenceClient(
            provider="novita",
            api_key=self.hf_token
        )
        return client

    def generate_prompt(self, json_file):
        """
        Generate a prompt for the language model based on the JSON file.
        The JSON file should contain the consultation data.
        """
        with open(json_file, 'r') as file:
            data = file.read()

        prompt = f"""You are an AI assistant generating discharge notes for veterinary consultations.
        Generate a discharge note based on the following data: {data}
        Only include information explicitly provided in the data. If no treatments or clinical notes are recorded, state that clearly.
        The discharge note should be in a professional tone, suitable for a veterinary clinic and in a concise form summarizing only the provided data.
        Generate the discharge note in 3–5 sentences, summarizing only the provided data."""
        return prompt

    def generate_discharge_text(self, prompt):
        """
        Generate the discharge note text using the language model withb the given prompt.
        """
        completion = self.client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )
        return completion.choices[0].message.content
    
    def generate_discharge_note(self, json_file):
        """
        Generate a discharge note for a given JSON file and save it to the solution folder.
        """
        prompt = self.generate_prompt(json_file)
        discharge_note = self.generate_discharge_text(prompt)

        input_base_name = os.path.basename(json_file).replace(".json", "")
        output_file = f"solution/{input_base_name}_discharge_note.json"
        self.save_discharge_note(discharge_note, output_file)
        return discharge_note
    
    def save_discharge_note(self, discharge_note, output_file):
        """
        Save the discharge note to a JSON file in the solution folder.
        """
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as file:
            json.dump({"discharge_note": discharge_note}, file, indent=2)
    
    def get_all_json_files(self, directory):
        """
        Get all JSON files in the specified directory.
        """
        json_files = []
        for files in os.listdir(directory):
            if files.endswith(".json"):
                json_files.append(os.path.join(directory, files))
        return json_files

if __name__ == "__main__":
    discharge_note_generator = DischargeNoteGenerator()
    all_json_files = discharge_note_generator.get_all_json_files("data")
    # discharge_note = discharge_note_generator.generate_discharge_note(json_file)
    for json_file in all_json_files:
        discharge_note = discharge_note_generator.generate_discharge_note(json_file)
        print(f"Discharge note for {json_file}:")
        print(discharge_note)
        print("\n")