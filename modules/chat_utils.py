import streamlit as st
from modules.ollama_client import get_model_response
from datetime import datetime

def handle_user_input():
    if prompt := st.chat_input("Enter your command..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.markdown(f"<div class='user-message'><strong style='color: #58a6ff;'>USER:</strong> {prompt}</div>", unsafe_allow_html=True)
        
        # Create tabs for model comparison
        tab_labels = [f"{model.split(':')[0]}" for model in st.session_state["selected_models"]]
        tabs = st.tabs(tab_labels)
        
        model_responses = {}
        thinking_processes = {}
        errors = {}
        
        # Get responses from all selected models
        for i, model in enumerate(st.session_state["selected_models"]):
            with tabs[i]:
                with st.spinner(f"{model} processing..."):
                    response, thinking, response_time, error = get_model_response(
                        model, 
                        st.session_state["messages"],
                        st.session_state["temperature"],
                        st.session_state["max_tokens"],
                        st.session_state["top_p"]
                    )
                    
                    # Store response and thinking process
                    model_responses[model] = response
                    thinking_processes[model] = thinking
                    st.session_state["response_times"][model] = response_time
                    
                    if error:
                        errors[model] = error
                        st.error(f"Model error: {error}")
                    else:
                        # Display response
                        st.markdown(f"<div class='model-output'><strong style='color: #00ff00;'>OUTPUT:</strong> {response}</div>", unsafe_allow_html=True)
                        
                        # Display thinking process if available
                        if thinking:
                            with st.expander("Show Thinking Process"):
                                for thought in thinking:
                                    st.markdown(f"<div class='thinking-process'>{thought.strip()}</div>", unsafe_allow_html=True)
                        
                        # Display performance metrics
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"<div class='metric-box'><strong>Response Time:</strong> {response_time:.2f}s</div>", unsafe_allow_html=True)
                        with col2:
                            token_count = len(response.split())
                            st.markdown(f"<div class='metric-box'><strong>Tokens:</strong> {token_count}</div>", unsafe_allow_html=True)
        
        # Generate a consensus or best response if no errors
        if not errors:
            generate_consensus_response(prompt, model_responses, thinking_processes)

def generate_consensus_response(prompt, model_responses, thinking_processes):
    with st.spinner("Engineering optimal response..."):
        # Create a prompt to generate a consensus response
        consensus_prompt = "Below are responses from different AI models to the same query. " \
                        "Please analyze these responses and provide a single, optimized response " \
                        "that combines the best elements of each, corrects any errors, and provides " \
                        "the most comprehensive and accurate answer.\n\n"
        
        consensus_prompt += f"Original Query: {prompt}\n\n"
        
        for model, response in model_responses.items():
            consensus_prompt += f"Response from {model}:\n{response}\n\n"
        
        consensus_prompt += "Please provide the optimized, combined response:"
        
        # Get the consensus response using the first model
        consensus_response, _, _, error = get_model_response(
            st.session_state["selected_models"][0],
            [{"role": "user", "content": consensus_prompt}],
            temperature=0.3,  # Lower temperature for more deterministic output
            max_tokens=st.session_state["max_tokens"],
            top_p=0.5
        )
        
        if not error:
            # Add to session state
            st.session_state["messages"].append({"role": "assistant", "content": consensus_response})
            
            # Store model interactions for later analysis
            interaction = {
                "timestamp": datetime.now().isoformat(),
                "prompt": prompt,
                "model_responses": model_responses,
                "thinking_processes": thinking_processes,
                "consensus_response": consensus_response,
                "parameters": {
                    "temperature": st.session_state["temperature"],
                    "max_tokens": st.session_state["max_tokens"],
                    "top_p": st.session_state["top_p"]
                }
            }
            st.session_state["model_interactions"].append(interaction)
            
            # Display the engineered response
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='assistant-message'><strong style='color: #00ff00;'>ENGINEERED RESPONSE:</strong> {consensus_response}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='timestamp'>Generated at {datetime.now().strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)