import cv2
import base64
import numpy as np
import matplotlib.pyplot as plt

def base64_to_image(base64_string):
    """Convert a Base64 string back to a NumPy image array."""
    image_data = base64.b64decode(base64_string)
    np_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib

# Replace with your Base64 string
base64_string = ""

# Decode image
decoded_image = base64_to_image(base64_string)

# Display using matplotlib
plt.imshow(decoded_image)
plt.axis('off')  # Hide axis
plt.show()
