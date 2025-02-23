# pip install --upgrade pip
# pip install ollama diffusers torch

import ollama
import torch

img = '2.jpg'

response = ollama.chat(model='llama3.2-vision',
					   messages=[{ 'role': 'user',
					   			   'content': 'What is in this image?', 
					   			   'images': [f'{img}'] }])

print(response['message']['content'])



from diffusers import DiffusionPipeline # ~ 20-25 min on CPU

pipe = DiffusionPipeline.from_pretrained("ostris/Flex.1-alpha") # pip install protobuf accelerate transformers[sentencepiece]

prompt = response['message']['content']
image = pipe(prompt).images[0]
image.save(f'neuro_alpha_{img}')



# from diffusers import DiffusionPipeline

# pipe = DiffusionPipeline.from_pretrained("digiplay/AbsoluteReality_v1.8.1") # ~ 6 min on CPU ~ 25 sec on GPU A10
# pipe = pipe.to("cuda") 

# prompt = response['message']['content']
# image = pipe(prompt).images[0]
# image.save(f'neuro_illustrious_{img}')

###################################################################################################################################


# from huggingface_hub import login
# login(token = "hf_QKe***NrifrjyxGskMoEpAc") # "hugging_face_access_token"

# from diffusers import DiffusionPipeline # pip install transformers

# pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev")
# pipe.load_lora_weights("fffiloni/carbo-800")

# prompt = response['message']['content'] + '. in the style of TOK'
# image = pipe(prompt).images[0]
# image.save(f'neuro_{img}')



# from diffusers import DiffusionPipeline

# pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev")
# pipe.load_lora_weights("strangerzonehf/Flux-Midjourney-Mix2-LoRA")
# pipe = pipe.to("cuda")

# prompt = "MJ v6," + pipe(prompt).images[0] + "--ar 47:64 --v 6.0 --style raw"
# image = pipe(prompt).images[0]
# image.save(f'neuroMidjourney-Mix2-LoRA_{img}')
