from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse
from diffusers import StableDiffusionPipeline
from PIL import Image
from io import BytesIO

app = FastAPI()

# Load the pretrained model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", low_cpu_mem_usage=False).to('cpu')

@app.post("/generate-image")
async def generate_image(prompt: str):
    try:
        # Process the prompt
        images = pipe([prompt])

        if images['nsfw_content_detected'][0]:
            # Handle NSFW content detection
            raise HTTPException(status_code=400, detail="The provided text resulted in NSFW content. Please try another text.")
        else:
            # Get the image from the result
            generated_image = images['images'][0]

            # Save the image to a BytesIO buffer
            image_buffer = BytesIO()
            generated_image.save(image_buffer, format="PNG")
            image_buffer.seek(0)

            return StreamingResponse(image_buffer, media_type="image/png")
    except Exception as e:
        # Handle any other exceptions
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
