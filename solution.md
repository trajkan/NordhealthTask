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
- **LLM**: I have chosen to use the Huggun Face APIs and more specifically a DeepSeek model (DeepSeek-V3-0324)
- **Environment**: The script should read API tokens from a .env
- **Ouput files**: For a given json file generate a corresponding json file in the folder "solution/"

## Plan for solving the task
1. Read consultation data from the input JSON file
2. Retrive the API key from config-file
3. Construct a prompt from the consultantion data.
4. Send the prompt to the LLM through the HuggingFace API
5. Save the ouput to a JSON file stored in solutions folder.

## Final remarks
- The chosen model works ok. It takes a couple of seconds to get a response and the response is mostly accurate
- The form of the outcome is not uniform, and would need some more work for it to produce uniform answers.
- There are no fault handling implemented. For instance, in case the HuggingFace API is not working this will currently not be handled in a good maner.
- I have only tried two different models, the current one and the OpenAI gpt2 where the latter one was not performing on a good level.
- Some more tuning could have been done of the model to prodcuce even better results.
- Post-processing of the response will probably be needed to make sure the the response does not contain false information or model halluctinations. For instance, the consultation2 data shows a price of £6450, while the model returns £64.50 and this needs to be handled in a proper way in the future.
