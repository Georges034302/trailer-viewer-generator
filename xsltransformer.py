import lxml.etree as ET
import re
import os

# Path to files
xml_file = '/usr/bin/trailer.xml'
xslt_file = '/usr/bin/trailer.xsl'
html_output_file = '/usr/bin/trailer.html'
readme_file = '/usr/bin/README.md'

# Check if XML file exists
if not os.path.exists(xml_file):
    print(f"Error: XML file not found at {xml_file}")
    exit(1)

# Check if XSLT file exists
if not os.path.exists(xslt_file):
    print(f"Error: XSLT file not found at {xslt_file}")
    exit(1)

# Parse XML and XSLT files
try:
    xml = ET.parse(xml_file)
    xslt = ET.parse(xslt_file)
except ET.XMLSyntaxError as e:
    print(f"Error parsing XML or XSLT: {e}")
    exit(1)

# Transform XML using XSLT
try:
    transform = ET.XSLT(xslt)
    html = transform(xml)
except Exception as e:
    print(f"Error during transformation: {e}")
    exit(1)

# Convert HTML to string
html_str = ET.tostring(html, pretty_print=True, method='html').decode('utf-8')
full_url = f"https://georges034302.github.io/trailer-viewer/trailer.html"

# Update the HTML content with the full URL
html_str = html_str.replace('<a href="{view/trailers/link}">Visit Trailer Viewer</a>', f'<a href="{full_url}">Visit Trailer Viewer</a>')

# Write the HTML content to a file
with open(html_output_file, 'w') as f:
    f.write(html_str)
print(f'HTML file generated: {html_output_file}')

# Function to update README.md with the latest URL
def update_readme(readme_file, new_url):
    if not os.path.exists(readme_file):
        print(f"Error: README.md file not found at {readme_file}")
        return

    with open(readme_file, 'r') as f:
        content = f.read()

    marker = "[Latest Trailers URL]"
    url_pattern = f"You can view the trailers [here]({new_url})."

    content = re.sub(rf'{re.escape(marker)}\s*[\s\S]*?(?=\n\S|$)', '', content).rstrip()

    if not content.endswith('\n\n'):
        content += '\n\n'

    content += f"{marker}\n{url_pattern}\n"

    with open(readme_file, 'w') as f:
        f.write(content)
    print(f'Full URL appended to README.md: {new_url}')

# Update README.md with the new URL
update_readme(readme_file, full_url)
