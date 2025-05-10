import asyncio
import os
from playwright.async_api import async_playwright
from tqdm import tqdm
from utils import remove_top_banner, remove_top_banner_and_footer
from images import create_images

async def login(page, base_url, username: str, password: str, timeout=1000):
    await page.goto(base_url)
    await page.get_by_text("Start now", exact=True).click()
    await page.get_by_label("Email address", exact=True).fill(username)
    await page.get_by_label("Password", exact=True).fill(password)
    await page.get_by_role("button", name="Log in", exact=True).click()
    await page.wait_for_url("**/users/organisations/new", timeout=timeout)
    organisation_heading = await page.query_selector("h2.nhsuk-card__heading")
    await organisation_heading.click()
    await page.wait_for_url("**/dashboard", timeout=timeout)

async def find_sessions(page):
    session_ids = []
    comm_clinic_slug = None
    location_links = await page.query_selector_all("a.nhsuk-link")
    for link in location_links:
        href = await link.get_attribute("href")
        id = href.split("/")[-1].split("-")[-1]
        if id.isdigit():
            session_ids.append(int(id))
        else:
            comm_clinic_slug = href.split("/")[-1]
    first_session_id = min(session_ids)
    return first_session_id, comm_clinic_slug

async def main():   
    username = "nurse.joy@example.com"
    password = "nurse.joy@example.com"
    base_url = "http://127.0.0.1:4000/"
    dynamic_screenshots_dir = os.path.dirname(__file__)

    manual_screenshots = ["notices.png", "offline-spreadsheet.png"]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()  # Set headless=True as needed
        context = await browser.new_context(viewport={ 'width': 1280, 'height': 1024 })

        page = await context.new_page()

        # Login to the application
        await login(page, base_url, username, password, timeout=1000)

        await page.goto(base_url+"sessions")
        first_session_id, clinic_slug = await find_sessions(page)
        image_metadata = create_images(first_session_id, clinic_slug)

        for image in tqdm(image_metadata):
            try:
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
                        body_box = await remove_top_banner_and_footer(page)
                    else:
                        body_box = await remove_top_banner(page)
                    await page.screenshot(path=output_file, full_page=full_page, clip=body_box)
            except Exception as e:
                tqdm.write(f"Error capturing screenshot: {image['image_name']}. Error: {str(e)}")
                manual_screenshots.append(image["image_name"])
                continue

        await browser.close()
    print("Done")
    print("Manual screenshots required for the following images:")
    for image in manual_screenshots:
        print(" - ", image)

if __name__ == "__main__":
    asyncio.run(main())
