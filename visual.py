import streamlit.components.v1 as components

def display_business_model():
    mermaid_code = """
    graph TD;
        Idea-->Market;
        Market-->Revenue;
        Revenue-->Growth;
    """
    components.html(f'<pre class="mermaid">{mermaid_code}</pre>', height=400)
