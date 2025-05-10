import datetime
from utils import add_margins, get_date, remove_top_banner,remove_top_banner_and_footer


async def process_consent_matching(page, output_file):
    match_links = await page.get_by_role("link", name="Match", exact=True).all()
    await match_links[0].click()
    child_key = page.get_by_text("Full name", exact=True)
    child_row = child_key.locator("..")
    child_value = await child_row.locator("dd").inner_text()
    search_input = page.locator('#search-form-q-field')
    await search_input.fill(child_value)
    await page.get_by_role("button", name="Search").click()
    await page.click(f'a:text("{child_value}")')

    title_key = page.get_by_text(" Link consent response with child record? ")
    title_box = await title_key.element_handle()
    title_box = await title_box.bounding_box()
    title_height = title_box["height"]+24

    details_key = page.locator('div.nhsuk-card-group')
    details_box = await details_key.element_handle()
    details_box = await details_box.bounding_box()

    details_box["height"] += title_height
    details_box["y"] -= title_height

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_get_consent(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    await child.click()

    await page.get_by_role("button", name="Get consent response").click()
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[0].check()   
    await page.get_by_text("Continue", exact=True).click()
    await page.get_by_text("Continue", exact=True).click()

    details_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_school_move_review(page, output_file):
    first_link = await page.query_selector("a:has-text('Review')")
    await first_link.click()
    
    details_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_pre_screening(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    await child.click()

    headers = await page.query_selector_all(".nhsuk-card__content")
    header = headers[-1]

    header_box = await header.bounding_box()

    header_box = add_margins(header_box, 16)

    await page.screenshot(path=output_file, clip=header_box, full_page=True)

async def process_get_gillick_competent_consent(page, output_file):
    child = await page.query_selector("a.nhsuk-card__link")
    await child.click()
    
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
    change_links = await page.query_selector_all("a.nhsuk-link:has-text('Change')")
    await change_links[1].click()

    delete_button = await page.get_by_text("Delete", exact=True).all() 
    
    while delete_button:   
        await delete_button[0].click()
        delete_button = await page.get_by_text("Delete", exact=True).all() 
    
    await page.get_by_text("Continue", exact=True).click()
    await page.get_by_text("Back", exact=True).click()
    await page.get_by_text("Continue", exact=True).click()
    await page.get_by_text("Schedule sessions", exact=True).click()

    body_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, full_page=True, clip=body_box)

async def process_session_no_consent(page, output_file):
    radio_buttons = await page.locator("[type='radio']").all()
    await radio_buttons[1].check()

    await page.get_by_text("Update results", exact=True).click()

    body_box = await remove_top_banner(page)

    await page.screenshot(path=output_file, clip=body_box)

async def process_clinic_invitations(page, output_file):
    link = page.get_by_text("Send clinic invitations", exact=True)
    await link.click()

    details_key = page.locator('div.nhsuk-grid-column-two-thirds')
    details_box = await details_key.element_handle()
    details_box = await details_box.bounding_box()

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

    await page.get_by_text("Send clinic invitations", exact=True).click()

async def process_booking_reminders(page, output_file):
    await page.get_by_text("Edit session", exact=True).click()
    change_links = await page.query_selector_all("a.nhsuk-link:has-text('Change')")
    await change_links[1].click()

    delete_buttons = await page.get_by_text("Delete", exact=True).all()
    
    today = datetime.datetime.now().strftime("%d %m %Y")
    session_dates = await page.query_selector_all('.app-add-another__list-item')
    for index,session_date in enumerate(session_dates):
        date_obj = await get_date(session_date)
        if date_obj.strftime("%d %m %Y") == today:
            await delete_buttons[index].click()
            break

    await page.get_by_text("Continue", exact=True).click()
    await page.get_by_text("Continue", exact=True).click()

    link = page.get_by_text("Send booking reminders", exact=True)
    await link.click()

    details_key = page.locator('div.nhsuk-grid-column-two-thirds')
    details_box = await details_key.element_handle()
    details_box = await details_box.bounding_box()

    details_box = add_margins(details_box, 16)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)

async def process_class_list_year_groups(page, output_file):
    search_input = page.locator('input[role="combobox"]')
    await search_input.fill("b")
    select_field = page.locator('#draft-class-import-session-id-field__listbox')
    first_option = select_field.locator('li:first-child')
    first_option = await first_option.element_handle()
    await first_option.click()

    await page.get_by_text("Continue", exact=True).click()

    details_box = await remove_top_banner_and_footer(page)

    await page.screenshot(path=output_file, clip=details_box, full_page=True)
