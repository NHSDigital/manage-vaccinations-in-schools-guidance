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

async def remove_footer(page):
    body_box = await find_body_box(page)
    footer_height = await find_footer_height(page)
    body_box["height"] -= footer_height
    return body_box
