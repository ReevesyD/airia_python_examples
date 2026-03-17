"""
Markdown to PDF Converter

How to use:
1. Install the dependency: pip install markdown-pdf
2. Update the two variables below with your values
3. Run the script
"""

from markdown_pdf import MarkdownPdf, Section

# UPDATE THESE VALUES
MD_PATH = "your_markdown_file.md"
OUTPUT_PATH = "your_output_file.pdf"

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_content = f.read()

pdf = MarkdownPdf()
pdf.add_section(Section(md_content))
pdf.save(OUTPUT_PATH)

print(f"🤙 PDF saved to: {OUTPUT_PATH}")