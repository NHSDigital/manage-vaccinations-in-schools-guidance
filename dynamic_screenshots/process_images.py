import time
from utils import add_margins, remove_footer


async def process_consent_matching(page, output_file):
    child_key = page.get_by_text("Child", exact=True)
    child_row = child_key.locator("..")
    child_value = await child_row.locator("dd").inner_text()
    await page.get_by_label("Name", exact=True).fill(child_value)
    await page.wait_for_timeout(5000) #wait for database search to complete
    await page.get_by_role("link", name="Select").click()

    title_key = page.get_by_text(" Link consent response with child record? ")
    title_box = await title_key.element_handle()
    title_box = await title_box.bounding_box()
    title_height = title_box["height"]+24

    details_key = page.get_by_text(" Compare details ", exact=True)
    details_box = await details_key.locator("..").element_handle()
    details_box = await details_box.bounding_box()

    details_box["height"] += title_height
    details_box["y"] -= title_height

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_get_consent(page, output_file):
    child_links = await page.get_by_text("Full name", exact=True).all()
    child_link = child_links[-1]
    parent = child_link.locator("..")
    await parent.locator("a").click()

    await page.get_by_role("button", name="Get consent response").click()
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[0].check()   
    await page.get_by_role("button", name="Continue").click()
    await page.get_by_role("button", name="Continue").click()

    details_box = await remove_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_pre_screening(page, output_file):
    child_links = await page.get_by_text(" Full name ", exact=True).all()
    child_link = child_links[-1]
    parent = child_link.locator("..")
    await parent.locator("a").click()

    await page.get_by_role("link", name="Update attendance").click()

    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[0].check() 
    await page.get_by_role("button", name="Save changes").click()

    header = page.get_by_role("heading", name=" Pre-screening questions ")
    parent = header.locator("..")
    header_box = await parent.element_handle()
    header_box = await header_box.bounding_box()

    header_box = add_margins(header_box, 16)

    await page.screenshot(path=output_file, clip=header_box, full_page=True)

async def process_get_gillick_competent_consent(page, output_file):
    child_links = await page.get_by_text(" Full name ", exact=True).all()
    child_link = child_links[-2]
    parent = child_link.locator("..")
    await parent.locator("a").click()
    
    await page.get_by_role("link", name="Gillick").click()
    radio_buttons = await page.locator("[type='radio']").all()    
    for button in radio_buttons:
        parent = button.locator("..")
        inner_text = await parent.locator("label").inner_text()
        if "Yes" in inner_text:
            await button.check()
    await page.get_by_role("button", name="your assessment").click()
    await page.get_by_role("button", name="Get consent response").click()

    header = page.get_by_role("heading", name=" Who are you trying to get consent from? ")
    parent = header.locator("..")
    header_box = await parent.element_handle()
    header_box = await header_box.bounding_box()

    header_box = add_margins(header_box, 16)

    await page.screenshot(path=output_file, clip=header_box, full_page=True)

async def process_sessions_add_dates(page, output_file):
    sessions_links = await page.get_by_text("Location", exact=True).all()
    session_link = sessions_links[-1]
    parent = session_link.locator("..")
    await parent.locator("a").click()

    await page.get_by_role("link", name="Edit session").click()

    body_box = await remove_footer(page)

    await page.screenshot(path=output_file, full_page=True, clip=body_box)
