import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Fira Code', monospace;
            font-weight: 300;
            font-size: 14px;
            background-color: #0d1117;
            color: #c9d1d9;
        }
        
        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
            max-width: 95%;
        }
        
        .stChatInput textarea {
            font-family: 'Fira Code', monospace !important;
            font-weight: 300;
            background-color: #0d1117;
            color: #00ff00;
            border: 1px solid #238636;
            border-radius: 4px;
        }
        
        .stChatInput button {
            background-color: #238636;
            color: white;
            font-family: 'Fira Code', monospace;
        }
        
        .user-message {
            background-color: #161b22;
            padding: 1rem;
            border-radius: 4px;
            border-left: 3px solid #58a6ff;
            margin-bottom: 0.75rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .assistant-message {
            background-color: #0d1117;
            padding: 1rem;
            border-radius: 4px;
            border-left: 3px solid #00ff00;
            margin-bottom: 0.75rem;
            color: #00ff00;
            font-family: 'Fira Code', monospace;
            white-space: pre-wrap;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .model-comparison {
            background-color: #161b22;
            padding: 1rem;
            border-radius: 4px;
            border: 1px solid #30363d;
            margin-bottom: 1rem;
        }
        
        .model-output {
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            border-radius: 4px;
            background-color: #0d1117;
        }
        
        .header {
            color: #58a6ff;
            border-bottom: 1px solid #30363d;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-weight: 400;
        }
        
        /* Sidebar enhancements */
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #0d1117 0%, #090c10 100%);
            border-right: 1px solid #30363d;
        }
        
        .sidebar-header {
            background: linear-gradient(90deg, #1f6feb 0%, #58a6ff 100%);
            padding: 0.75rem 1rem;
            margin: -1rem -1rem 1rem -1rem;
            border-bottom: 1px solid #30363d;
        }
        
        .sidebar-section {
            background-color: #161b22;
            padding: 1rem;
            border-radius: 6px;
            border: 1px solid #30363d;
            margin-bottom: 1.25rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }
        
        .sidebar-title {
            color: #58a6ff;
            font-weight: 400;
            margin-bottom: 0.75rem;
            border-bottom: 1px solid #30363d;
            padding-bottom: 0.5rem;
            font-size: 0.95em;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .sidebar-title::before {
            content: "→";
            color: #3fb950;
        }
        
        .stSelectbox div[data-baseweb="select"] {
            background-color: #0d1117;
            color: #c9d1d9;
            border: 1px solid #30363d;
        }
        
        .stButton button {
            width: 100%;
            background: linear-gradient(90deg, #238636 0%, #2ea043 100%);
            color: white;
            border: none;
            font-family: 'Fira Code', monospace;
            font-weight: 300;
            margin-top: 0.5rem;
            transition: all 0.2s ease;
        }
        
        .stButton button:hover {
            background: linear-gradient(90deg, #2ea043 0%, #3fb950 100%);
            color: white;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(46, 160, 67, 0.2);
        }
        
        .metric-box {
            background-color: #0d1117;
            padding: 0.75rem;
            border-radius: 4px;
            border: 1px solid #30363d;
            margin-bottom: 0.5rem;
            transition: all 0.2s ease;
        }
        
        .metric-box:hover {
            border-color: #58a6ff;
            transform: translateX(2px);
        }
        
        .tab-container {
            border: 1px solid #30363d;
            border-radius: 4px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .thinking-process {
            background-color: #161b22;
            padding: 0.75rem;
            border-radius: 4px;
            border-left: 3px solid #ff7b72;
            margin-bottom: 0.5rem;
            font-size: 0.9em;
            color: #8b949e;
        }
        
        .divider {
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, #30363d 50%, transparent 100%);
            margin: 1rem 0;
        }
        
        .timestamp {
            color: #8b949e;
            font-size: 0.8em;
            text-align: right;
            margin-top: 0.5rem;
        }
        
        /* Slider styling */
        .stSlider div[data-baseweb="slider"] {
            color: #3fb950;
        }
        
        .stSlider div[data-baseweb="slider"]:hover {
            color: #58a6ff;
        }
        
        /* Custom multiselect styling */
        .stMultiSelect div[data-baseweb="select"] {
            background-color: #0d1117;
            border: 1px solid #30363d;
        }
        
        .stMultiSelect div[data-baseweb="select"]:hover {
            border-color: #58a6ff;
        }
        
        /* Status indicator */
        .status-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 8px;
        }
        
        .status-online {
            background-color: #3fb950;
            box-shadow: 0 0 6px #3fb950;
        }
        
        .status-offline {
            background-color: #8b949e;
        }
        
        /* Model badge */
        .model-badge {
            display: inline-block;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75em;
            margin-right: 0.5rem;
            background-color: #1f6feb;
            color: white;
        }
        
        /* Code-like elements */
        .code-block {
            background-color: #0d1117;
            padding: 0.5rem;
            border-radius: 4px;
            border: 1px solid #30363d;
            font-family: 'Fira Code', monospace;
            font-size: 0.85em;
            margin: 0.5rem 0;
            overflow-x: auto;
        }             
    </style>
    """, unsafe_allow_html=True)