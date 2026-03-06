# app.py
import streamlit as st
from engine.workflow_engine import run_workflow


st.set_page_config(
    page_title="AI-Flow Dashboard",
    page_icon="🤖",
    layout="wide"
)


st.sidebar.title("🤖 AI-Flow Controls")
workflow_options = ["meeting_workflow", "risk_assessment_workflow"]
workflow_name = st.sidebar.selectbox("Select Workflow:", workflow_options)

st.sidebar.markdown("---")
st.sidebar.subheader("📥 Input Method")
input_method = st.sidebar.radio("Choose input:", ["Paste text", "Upload file"], index=0)

input_text = ""
if input_method == "Paste text":
    input_text = st.sidebar.text_area("Paste input here:", height=150)
elif input_method == "Upload file":
    uploaded_file = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        input_text = uploaded_file.read().decode("utf-8")

run_button = st.sidebar.button("🚀 Run Workflow")


st.markdown(
    """
    <div style="text-align:center; padding:20px; background-color:#f0f2f6; border-radius:10px; margin-bottom:20px;">
        <h1 style="color:#4B0082;">AI-Flow Dashboard</h1>
        <p style="font-size:16px; color:#333;">
        AI flows where your thoughts go. <br>
        Select a workflow, provide input, and see structured AI outputs instantly!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


if run_button:
    if not input_text.strip():
        st.warning("⚠️ Please provide input before running the workflow.")
    else:
        with st.spinner("Running workflow..."):
            try:
                output = run_workflow(workflow_name, input_text)
                
                st.subheader("📊 Workflow Output")
                col1, col2 = st.columns([1, 2])
                
                # --- Workflow Info ---
                with col1:
                    st.markdown(
                        f"""
                        <div style="background-color:#E8F0FE; padding:15px; border-radius:10px;">
                        <h4 style="color:#1A73E8;">Workflow Info</h4>
                        <p><strong>Name:</strong> {workflow_name}</p>
                        <p><strong>Input length:</strong> {len(input_text)} characters</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                # --- Readable output for business users ---
                with col2:
                    st.markdown(
                        """
                        <div style="background-color:#F1F8E9; padding:15px; border-radius:10px;">
                        <h4 style="color:#388E3C;">Readable Output</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    def format_readable(value, indent=0):
                        """Recursively format JSON content in a readable format"""
                        lines = []
                        prefix = "&nbsp;" * (indent * 2)
                        
                        if isinstance(value, dict):
                            for k, v in value.items():
                                key_name = k.replace('_', ' ').title()
                                if isinstance(v, dict) and v:
                                    lines.append(f"{prefix}<strong>{key_name}:</strong>")
                                    lines.extend(format_readable(v, indent + 1))
                                elif isinstance(v, list) and v:
                                    lines.append(f"{prefix}<strong>{key_name}:</strong>")
                                    # Check if list contains dicts or primitives
                                    if isinstance(v[0], dict):
                                        for item in v:
                                            lines.extend(format_readable(item, indent + 1))
                                    else:
                                        for item in v:
                                            lines.append(f"{prefix}&nbsp;&nbsp;• {item}")
                                else:
                                    # Handle multi-line strings (like emails)
                                    value_str = str(v).replace('\n', '<br>')
                                    lines.append(f"{prefix}<strong>{key_name}:</strong> {value_str}")
                        elif isinstance(value, list):
                            for item in value:
                                if isinstance(item, dict):
                                    lines.extend(format_readable(item, indent))
                                else:
                                    lines.append(f"{prefix}• {item}")
                        else:
                            lines.append(f"{prefix}{value}")
                        
                        return lines
                    
                    formatted_output = format_readable(output)
                    st.markdown("<br>".join(formatted_output), unsafe_allow_html=True)

                    # --- Optional raw JSON ---
                    with st.expander("View Raw JSON Output"):
                        st.json(output)
                    
            except Exception as e:
                st.error(f"❌ Error running workflow: {e}")


st.markdown(
    """
    <div style="text-align:center; color:#888; margin-top:30px;">
    Made with ❤️ by AI-Flow
    </div>
    """,
    unsafe_allow_html=True
)