import datetime


def add_margins(box, margin_size):
    box["height"] += 2*margin_size
    box["width"] += 2*margin_size
    box["y"] -= margin_size
    box["x"] -= margin_size
    return box

async def find_footer_height(page):
    footer = page.get_by_role("contentinfo")
    footer_box = await footer.element_handle()
    footer_box = await footer_box.bounding_box()
    return footer_box["height"]

async def find_body_height(body_box):
    return body_box["height"]

async def find_body_box(page):
    body = await page.locator("body").all()
    body = body[0]
    body_box = await body.element_handle()
    body_box = await body.bounding_box()
    return body_box

async def find_top_banner_height(page):
    top_banner = await page.query_selector(".app-environment")
    top_banner_box = await top_banner.bounding_box()
    return top_banner_box["height"]

async def remove_top_banner(page):
    body_box = await find_body_box(page)
    top_banner_height = await find_top_banner_height(page)
    body_box["height"] -= top_banner_height
    body_box["y"] += top_banner_height
    return body_box

async def remove_top_banner_and_footer(page):
    body_box = await find_body_box(page)
    footer_height = await find_footer_height(page)
    top_banner_height = await find_top_banner_height(page)
    body_box["height"] -= footer_height + top_banner_height
    body_box["y"] += top_banner_height
    return body_box

async def get_date(session_date):
    day_input = await session_date.query_selector('input[name$="[value(3i)]"]')
    month_input = await session_date.query_selector('input[name$="[value(2i)]"]')
    year_input = await session_date.query_selector('input[name$="[value(1i)]"]')
    day_value = await day_input.get_attribute('value')
    month_value = await month_input.get_attribute('value')
    year_value = await year_input.get_attribute('value')
    date_obj = datetime.datetime(int(year_value), int(month_value), int(day_value))
    return date_obj