import streamlit as st
from modules.ollama_client import get_model_response
from modules.chat_utils import generate_consensus_response
from datetime import datetime

def render_sidebar():
    with st.sidebar:
        # Sidebar header
        st.markdown("""
        <div class="sidebar-header">
            <h3 style="color: white; margin: 0; font-weight: 400;">
            <span class="status-indicator status-online"></span>
            OLLAMA PRISM PRO
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Model selection section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">MODEL SELECTION</div>', unsafe_allow_html=True)
        
        available_models = ["deepseek-r1:1.5b", "qwen2:0.5b", "llama2", "mistral", "codellama:7b", "phi3:mini"]
        selected_models = st.multiselect(
            "Choose models to compare:",
            available_models,
            default=st.session_state["selected_models"],
            help="Select at least two models for comparison"
        )
        
        if len(selected_models) >= 2:
            st.session_state["selected_models"] = selected_models
            st.markdown(f'<div class="code-block">Models active: {", ".join(selected_models)}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please select at least two models")
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close section
        
        # Engineering parameters section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">PARAMETERS</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            temperature = st.slider("Temperature", 0.1, 1.0, 0.7, 0.1, 
                                  help="Controls randomness: Lower = more deterministic")
        with col2:
            max_tokens = st.slider("Max Tokens", 100, 2000, 1000, 50, 
                                 help="Maximum length of response")
        
        top_p = st.slider("Top-P", 0.1, 1.0, 0.9, 0.1, 
                        help="Controls diversity via nucleus sampling")
        
        st.markdown(f"""
        <div class="code-block">
        Temperature: {temperature}<br>
        Max Tokens: {max_tokens}<br>
        Top-P: {top_p}
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state["temperature"] = temperature
        st.session_state["max_tokens"] = max_tokens
        st.session_state["top_p"] = top_p
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close section
        
        # Performance metrics section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">PERFORMANCE METRICS</div>', unsafe_allow_html=True)
        
        if st.session_state["response_times"]:
            for model, time_taken in st.session_state["response_times"].items():
                efficiency = "🟢" if time_taken < 2.0 else "🟡" if time_taken < 5.0 else "🔴"
                st.markdown(f"""
                <div class="metric-box">
                    <span class="model-badge">{model.split(':')[0]}</span>
                    {efficiency} {time_taken:.2f}s
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No performance data yet. Run a query to see metrics.")
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close section
        
        # System controls section
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">SYSTEM CONTROLS</div>', unsafe_allow_html=True)
        
        if st.button("🔄 CLEAR CHAT", help="Start a new conversation"):
            st.session_state["messages"] = [{"role": "system", "content": "You are a helpful assistant."}]
            st.session_state["model_interactions"] = []
            st.session_state["response_times"] = {}
            st.rerun()
        
        if st.button("💾 EXPORT HISTORY", help="Export conversation history"):
            # In a real implementation, this would export the chat history
            st.success("Export functionality would be implemented here")
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close section
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #8b949e; font-size: 0.8em;">
            <p>Ollama-Prism Pro v1.0</p>
            <p>Powered by Ollama</p>
        </div>
        """, unsafe_allow_html=True)

def render_main_content():
    # Main content
    st.markdown("<h1 class='header'>OLLAMA PRISM PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8b949e;'>Multi-model comparison with engineering insights</p>", unsafe_allow_html=True)

    # Display previous messages
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-message'><strong style='color: #58a6ff;'>USER:</strong> {msg['content']}</div>", unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f"<div class='assistant-message'><strong style='color: #00ff00;'>ASSISTANT:</strong> {msg['content']}</div>", unsafe_allow_html=True)

    # Show interaction history in an expandable section
    if st.session_state["model_interactions"]:
        with st.expander("View Interaction History", expanded=False):
            for i, interaction in enumerate(st.session_state["model_interactions"]):
                st.markdown(f"**Interaction {i+1}** - {interaction['timestamp'][:10]}")
                st.markdown(f"**Prompt:** {interaction['prompt']}")
                st.markdown(f"**Engineered Response:** {interaction['consensus_response']}")
                st.markdown("---")