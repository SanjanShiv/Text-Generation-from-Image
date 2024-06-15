import cv2
import pytesseract
from PIL import Image
import base64
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sanja\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)
    
    return text

def segment_visual_elements(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to segment the image
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    visual_elements = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        visual_element = image[y:y+h, x:x+w]
        
        # Convert the visual element to a Base64 string
        _, buffer = cv2.imencode('.png', visual_element)
        visual_element_base64 = base64.b64encode(buffer).decode('utf-8')
        visual_elements.append(visual_element_base64)
    
    return visual_elements

def generate_html(text, visual_elements):
    html_content = "<html>\n<head>\n<title>Extracted Content</title>\n</head>\n<body>\n"
    
    # Replace new lines with <br> tags for HTML
    formatted_text = text.replace('\n', '<br>')
    
    # Add text to HTML content
    html_content += f"<p>{formatted_text}</p>\n"
    
    # Add visual elements to HTML content
    for element in visual_elements:
        html_content += f'<img src="data:image/png;base64,{element}" alt="Visual Element">\n'
    
    html_content += "</body>\n</html>"
    
    return html_content

if __name__ == "__main__":
    image_path = "IvV2y.png"  # Replace with your image path
    
    # Extract text from image
    text = extract_text(image_path)
    print("Extracted Text:")
    print(text)
    
    # Segment visual elements in image
    visual_elements = segment_visual_elements(image_path)
    
    # Generate HTML content
    html_content = generate_html(text, visual_elements)
    
    # Save the HTML content to a file
    html_file_path = "output.html"
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    
    print(f"HTML content saved as: {html_file_path}")
