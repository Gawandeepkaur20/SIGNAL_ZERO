from urllib.parse import quote
import random

def generate_image(prompt):

    enhanced_prompt = (
        f"cinematic sci-fi, ultra detailed, concept art, 8k, {prompt}"
    )

    seed = random.randint(1, 1_000_000)

    return (
        f"https://image.pollinations.ai/prompt/"
        f"{quote(enhanced_prompt)}?seed={seed}"
    )