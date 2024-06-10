import requests

class Quote:
    def get_quote_from_api(self):
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"'{quote}'\n          -- {author}"

    def display_quote(self):
        print(f"Quote of the Day: {self.get_quote_from_api()}")

