# My solution to the Nordhealth AI Recruitment Task

## Introduction
The task is about automating the discharge note generation.

## Prerequisite
We need to use an LLM of our choice to generate the discharge note.
As we only have two discharge notes, we cannot fine-tune the chosen LLM in regards to existing discharge notes.
Instead we will try to prompt the consultations to the LLM and then post-process the answer and try to streamline
the answers so that they follow similar structure
- **Input**: A JSON file containing consultation data.
- **Ouput**: A JSON file with the discharge note 
- **LLM**: I have chosen to use the Huggun Face APIs
- **Environment**: The script should read API tokens from a config-file
- **Ouput files**: For a given json file generate a corresponding json file in the folder "/solution"

## Plan for solving the task
1. Read consultation data from the input JSON file
2. Retrive the API key from config-file
3. Construct a prompt from the consultantion data
4. Post-process the responose from the LLM so that is follows the general discharge note structure
5. Save the ouput to a JSON file stored in solutions folder.