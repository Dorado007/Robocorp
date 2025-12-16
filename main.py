from RPA.Browser.Playwright import Playwright

def run(context):
    browser = Playwright()
    browser.open_browser("https://www.google.com/search?q=dolar+peso+colombiano")
    # Ajusta este selector si cambias de sitio
    rate_selector = "text=/\\$.* COP/"
    element = browser.get_text(rate_selector)
    browser.close_browser()

    # Guarda el resultado como output
    context["outputs"]["exchange_rate"] = element
    print(f"Valor dólar peso colombiano: {element}")
