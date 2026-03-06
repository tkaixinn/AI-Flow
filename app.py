import json
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

tab1, tab2 = st.tabs(["🚀 Run Workflow", "📘 Workflow Guide"])
with tab1:
    if run_button:
        if not input_text.strip():
            st.warning("⚠️ Please provide input before running the workflow.")
        else:
            with st.spinner("Running workflow..."):
                try:
                    output = run_workflow(workflow_name, input_text)
                    
                    st.subheader("📊 Workflow Output")
                    col1, col2 = st.columns([1, 2])
                    
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
        
                                        if isinstance(v[0], dict):
                                            for i, item in enumerate(v):
                                                lines.extend(format_readable(item, indent + 1))

                                                if i < len(v) - 1:
                                                    lines.append("")
                                        else:
                                            for item in v:
                                                lines.append(f"{prefix}&nbsp;&nbsp;• {item}")
                                    else:

                                        value_str = str(v).replace('\n', '<br>')
                                        lines.append(f"{prefix}<strong>{key_name}:</strong> {value_str}")
                            elif isinstance(value, list):
                                for i, item in enumerate(value):
                                    if isinstance(item, dict):
                                        lines.extend(format_readable(item, indent))

                                        if i < len(value) - 1:
                                            lines.append("")
                                    else:
                                        lines.append(f"{prefix}• {item}")
                            else:
                                lines.append(f"{prefix}{value}")
                            
                            return lines
                        
                        formatted_output = format_readable(output)
                        st.markdown("<br>".join(formatted_output), unsafe_allow_html=True)

                        with st.expander("View Raw JSON Output"):
                            st.json(output)
                        
                        st.download_button(
                            label="⬇️ Download Output as JSON",
                            data=json.dumps(output, indent=2),
                            file_name="workflow_output.json",
                            mime="application/json"
                        )

                except Exception as e:
                    st.error(f"❌ Error running workflow: {e}")

with tab2:

    st.header("📘 Workflow Guide")

    st.markdown("### 📝 Meeting Workflow")

    st.markdown("""
**Purpose:** Convert meeting transcripts into structured action items.

**What to include in your input:**

• Meeting discussion points  
• Tasks assigned to team members  
• Owners responsible for tasks  
• Deadlines if mentioned  

**Example Input**

Project X is delayed due to resource issues.  
Alice will prepare the updated timeline by Friday.  
Bob will notify stakeholders about the delay.

**Output Generated**

• Meeting summary  
• Action items with owners and deadlines  
• Identified project risks  
• Follow-up email draft
""")

    st.markdown("---")

    st.markdown("### ⚠️ Risk Assessment Workflow")

    st.markdown("""
**Purpose:** Analyze project plans and identify potential risks.

**What to include in your input:**

• Project description  
• Timeline or deadlines  
• Resource constraints  
• Dependencies between teams  
• Possible bottlenecks  

**Example Input**

Project X will launch in Q3.  
Development depends on external vendors.  
Testing resources are limited.

**Output Generated**

• Risk description  
• Likelihood of occurrence  
• Potential impact  
• Recommended mitigation plan
""")
    
st.markdown(
    """
    <div style="text-align:center; color:#888; margin-top:30px;">
    Made with ❤️ by AI-Flow
    </div>
    """,
    unsafe_allow_html=True
)