import asyncio
import os
from playwright.async_api import async_playwright
from tqdm import tqdm
from utils import remove_footer
from images import IMAGES

async def login(page, base_url, username: str, password: str, timeout=1000):
    # Replace with your app's login URL and adjust selectors as needed.
    await page.goto(base_url)
    await page.get_by_text("Start now", exact=True).click()
    await page.get_by_label("Email address", exact=True).fill(username)
    await page.get_by_label("Password", exact=True).fill(password)
    await page.get_by_role("button", name="Log in", exact=True).click()
    await page.wait_for_url("**/users/organisations/new", timeout=timeout)
    await page.get_by_role("heading", name="SAIS Organisation 1 (R1L)", exact=True).click()
    await page.wait_for_url("**/dashboard", timeout=timeout)


async def main():
    username = "nurse.joy@example.com"
    password = "nurse.joy@example.com"
    base_url = "http://127.0.0.1:4000/"

    dynamic_screenshots_dir = os.path.dirname(__file__)
    os.makedirs(os.path.join(dynamic_screenshots_dir,"screenshots"), exist_ok=True)

    image_metadata = IMAGES
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()  # Set headless=True as needed
        context = await browser.new_context(viewport={ 'width': 1280, 'height': 1024 })

        page = await context.new_page()

        # Login to the application
        await login(page, base_url, username, password, timeout=1000)

        for image in tqdm(image_metadata):
            tqdm.write(f"Capturing screenshot: {image['image_name']}")
            target_url = base_url + image["path"]
            output_file = f"{dynamic_screenshots_dir}/../app/assets/images/{image['image_name']}"

            full_page = image["full_page"] if "full_page" in image.keys() else False

            page = await context.new_page()
            await page.set_viewport_size({
            "width": image["screen_size"]["width"],
            "height": 100 if full_page else image["screen_size"]["height"]
            })

            # Navigate to the target URL and capture the screenshot.
            await page.goto(target_url)
            if "further_processing" in image.keys():
                await image["further_processing"](page, output_file)
            else:
                if full_page:
                    body_box = await remove_footer(page)
                else:
                    body_box = None
                await page.screenshot(path=output_file, full_page=full_page, clip=body_box)

        await browser.close()
    print("Done")

if __name__ == "__main__":
    asyncio.run(main())
