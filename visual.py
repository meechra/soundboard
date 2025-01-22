import streamlit.components.v1 as components

def display_business_model():
    mermaid_code = """
    graph TD;
        Idea["Business Idea"] --> |Market Research| Market[Market Analysis]
        Market --> |Revenue Plan| Revenue[Revenue Streams]
        Revenue --> |Expansion Strategy| Growth[Growth Opportunities]
    """
    components.html(f'<pre class="mermaid">{mermaid_code}</pre>', height=400)
