from playwright.sync_api import sync_playwright

URL_TEMPLATE = "https://www.realityrealtypr.com/properties/type:venta/pagination:size%7C15%7Cpage%7C{page}/?search%5Barea%5D=&search%5Bprice_from%5D=&search%5Bkeywords%5D=&search%5Bproperty_type%5D={property_type}&search%5Bprice_to%5D="

def get_property_data(property_type: str, n_page: int):
    with sync_playwright() as pw:
        chrome = pw.chromium.launch(headless=False)
        context = chrome.new_context()
        page = context.new_page()
        url = create_realityrealty_url(property_type, n_page)
        print("Entering to URL",url)
        page.goto(url)
        page.wait_for_selector("body > div.container.container-main-padding.list-container > div.results")
        visible_properties = page.locator("body > div.container.container-main-padding.list-container > div.results").get_by_role("heading").all()
        print("Visible objects found:",len(visible_properties))
        data = []
        for i in range(len(visible_properties)):
            visible_properties = page.locator("body > div.container.container-main-padding.list-container > div.results").get_by_role("heading")
            element_text = visible_properties.nth(i).inner_text()
            print(f"Clicking on: {element_text}")
            
            clickable = visible_properties.nth(i).locator("..").get_by_role("link",name=element_text)
            clickable.click()

            page.wait_for_load_state("domcontentloaded")

            print(f"Scraping data from: {page.url}")
            if page.is_visible("#thumbcarousel > div"):
                page.wait_for_selector("#thumbcarousel > div", timeout=50000)
            
            page_data = scrape_data_from_property(page,element_text)
            data.append(page_data)

            page.go_back()
            page.wait_for_selector("body > div.container.container-main-padding.list-container > div.results", timeout=50000)
        return data

def scrape_data_from_property(page, title):
    url = page.url
    flyer_url = page.locator("#top-content > div > div:nth-child(2) > div.col-xs-12.col-sm-4.title-side > span:nth-child(1)").get_by_role("link").all()[0].get_attribute("href")
    images = [image.get_attribute("src") for image in page.locator("#thumbcarousel > div > div.item.active").get_by_role('img').all()] if page.query_selector("#thumbcarousel > div > div.item.active") != None else []
    city = page.locator("#top-content > div > div:nth-child(2) > div.col-xs-12.col-sm-8").get_by_role('paragraph').all_text_contents()[0]
    prices = page.locator("#top-content > div > div:nth-child(3)").get_by_role("heading").all_text_contents()
    price_str = ",".join([price.replace(" ","").replace(":",": ").replace("\n", "") for price in prices])
    description = page.locator("#home").all_text_contents()[0].replace("\n", "").strip()
    page_data = {
        "url": url,
        "title": title,
        "city": city,
        "price": price_str,
        "description": description,
        "images": images,
        "flyer": flyer_url
    }
    return page_data

def create_realityrealty_url(property_type:str, page: int):
    ptype_dict = {
        "HOUSE":"Residential%3A1",
        "APARTMENT":"Residential%3A5"
    }
    if property_type not in ptype_dict:
        supported_ptypes_str = ",".join(ptype_dict.keys())
        raise ValueError(f"Tipo de propiedad inválida, el valor debe ser alguno de los siguientes ({supported_ptypes_str})")
    url = URL_TEMPLATE.format(
        property_type=ptype_dict[property_type],
        page=page
    )
    return url
