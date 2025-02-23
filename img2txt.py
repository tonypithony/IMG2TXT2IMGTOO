import ollama

img = '2.jpg'

response = ollama.chat(model='llama3.2-vision',
					   messages=[{ 'role': 'user',
					   			   'content': 'What is in this image?', 
					   			   'images': [f'{img}'] }])

print(response['message']['content'])

'''
The image depicts a serene winter scene of Amsterdam's famous canals, with snow-covered streets and buildings lining the waterways. 
The city's iconic architecture, including its historic houses and bridges, is visible along the canal banks. 
A few boats are moored at the dock, adding to the tranquil atmosphere of the scene. 
Overall, the image captures the beauty and charm of Amsterdam's winter landscape
'''

'''
The image depicts a self-portrait of Vincent van Gogh, painted by the artist himself. 
The painting features Van Gogh with his characteristic red beard and hair, dressed in a suit jacket and shirt. 
He is shown facing slightly to the right, looking directly at the viewer. 
The background of the painting is a swirling pattern of blue and green brushstrokes, 
which was a hallmark of Van Gogh's post-Impressionist style.
This self-portrait is one of several that Van Gogh created during his lifetime, 
and it is considered one of his most important works. It is also one of the most 
famous self-portraits in art history, and it continues to be widely admired and studied today.
'''

'''
This image depicts a serene winter scene of Amsterdam, featuring several boats along a canal 
and snow-covered buildings. The sky above is a soft blue with clouds, evoking the feeling of 
an early morning or late evening during the holiday season. The overall atmosphere is peaceful 
and tranquil, perfect for capturing the essence of this iconic city.

The image shows three young women standing on a bridge overlooking a canal, with their backs to the camera. 
They are all wearing shorts or skirts and have their hands raised above their heads, possibly taking a selfie 
or posing for a photo. The background of the image is out of focus, but it appears to be a city street with 
trees and buildings in the distance.
'''