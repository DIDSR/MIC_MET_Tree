# ui/styles.py

CSS = """
<style>
.reportview-container .main .block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-right: 2rem;
    padding-left: 2rem;
    padding-bottom: 2rem;
}
h1 {
    color: #2c5282;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
}
h2 {
    color: #1a202c;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
}
h3 {
    color: #1a202c;
    font-size: 1.75rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}
.stButton>button {
    background-color: #4299e1;
    color: white;
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    border: none;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
}
.stButton>button:hover {
    background-color: #3182ce;
    transform: translateY(-1px);
}
.stButton>button:active {
    background-color: #2c5282;
}
.stMarkdown p, .stMarkdown ul, .stMarkdown li {
    text-align: justify;
}
</style>
"""
