from urllib.parse import urlparse, parse_qsl, urlencode


class PFFRURLProcessor:

    def get_query_params(self, url):
        parsed = urlparse(url)
        params = dict(parse_qsl(parsed.query))
        return params

    def add_query_params(self, url, params: dict):
        if not params:
            return url
        current_params = self.get_query_params(url)
        merged_params = urlencode({**current_params, **params})
        parsed = urlparse(url)
        parsed = parsed._replace(query=merged_params)
        return parsed.geturl()


pffr_url_processor = PFFRURLProcessor()
