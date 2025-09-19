import ollama
import re
import time

# Function to clean unwanted thinking tags
def clean_response(text):
    # Remove everything between <think> and </think> but save it for display
    thinking_content = re.findall(r'<think>(.*?)</think>', text, flags=re.DOTALL)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    # Remove any other leading <tags>
    text = re.sub(r'^<[^>]+>\s*', '', text)
    return text.strip(), thinking_content

# Function to get model response
def get_model_response(model, messages, temperature, max_tokens, top_p):
    start_time = time.time()
    
    try:
        response = ollama.chat(
            model=model,
            messages=messages,
            options={
                'temperature': temperature,
                'num_predict': max_tokens,
                'top_p': top_p
            }
        )
        
        response_time = time.time() - start_time
        final_reply, thinking_process = clean_response(response.message.content)
        
        return final_reply, thinking_process, response_time, None
    except Exception as e:
        return f"Error: {str(e)}", [], time.time() - start_time, str(e)