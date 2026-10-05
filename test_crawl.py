import unittest

from crawl import get_heading_from_html, normalize_url


class TestNormalize(unittest.TestCase):
    def test_normalize_url_protocol(self) -> None:
        input_url = "https://crawler-test.com/path"
        actual = normalize_url(input_url)
        expected = "crawler-test.com/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_slash(self) -> None:
        input_url = "https://crawler-test.com/path/"
        actual = normalize_url(input_url)
        expected = "crawler-test.com/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_capitals(self) -> None:
        input_url = "https://CRAWLER-TEST.com/path"
        actual = normalize_url(input_url)
        expected = "crawler-test.com/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_http(self) -> None:
        input_url = "http://CRAWLER-TEST.com/path"
        actual = normalize_url(input_url)
        expected = "crawler-test.com/path"
        self.assertEqual(actual, expected)


class TestGetHeading(unittest.TestCase):
    def test_get_heading_from_html(self):
        html_page = """
        <html>
            <body>
                <h1>Welcome to Boot.dev</h1>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body>
        </html>
        """
        actual = "Welcome to Boot.dev"
        expected = get_heading_from_html(html_page)
        self.assertEqual(actual, expected)
        


if __name__ == "__main__":
    unittest.main()
