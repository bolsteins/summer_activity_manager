import requests
from pyfiglet import Figlet

class quote:
    def get_quote_from_api(self):
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"'{quote}'\n          -- {author}"

    def display_quote(self):
        figlet = Figlet(font='banner')
        text = self.get_quote_from_api()
        print(figlet.renderText(text))

if __name__ == "__main__":
    quote_service = quote()
    quote_service.display_quote()