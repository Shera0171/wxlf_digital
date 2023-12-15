# filename: generate_image.py

# from diffusers

from diffusers import StableDiffusionPipeline
from PIL import Image

def generate_image(prompt):
    # Load the model
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", low_cpu_mem_usage=False).to('cpu')
    # pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", low_cpu_mem_usage = False).to('cpu')

    # Process the prompt
    images = pipe([prompt])

    if images['nsfw_content_detected'][0]:
        _ = images['images'].pop(0)
        del _
        image = 'The prompt returned NSFW content, please try another'
    else:
        image = images['images'][0]

    # Save the image to the current directory
    image.save('generated_image_5.png')

    return image

if __name__ == "__main__":
    # Example usage
    user_prompt = input('What would you like me to create: ')
    result_image = generate_image(user_prompt)
    print(result_image)
    print("Generated image saved as 'generated_image_5.png' in the current directory.")

