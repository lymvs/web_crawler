import unittest

from crawl import (
    get_first_paragraph_from_html,
    get_heading_from_html,
    get_urls_from_html,
    normalize_url,
)


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
        actual = get_heading_from_html(html_page)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)
    
    def test_get_h2_heading_from_html(self):
        html_page = """
       <html>
            <body>
                <h2>Welcome to Boot.dev</h2>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body>
        </html> 
        """
        actual = get_heading_from_html(html_page)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)
    
    def test_no_heading_from_html(self):
        html_page = """
        <html>
            <body>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body>
        </html>
        """
        actual = get_heading_from_html(html_page)
        expected = ""
        self.assertEqual(actual, expected)


class TestGetFirstParagraph(unittest.TestCase):
    def test_get_first_paragraph_from_html_basic(self) -> None:
        input_body = "<html><body><p>This is the first paragraph.</p></body></html>"
        actual = get_first_paragraph_from_html(input_body)
        expected = "This is the first paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self) -> None:
        input_body = """<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>"""
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_no_paragraph(self) -> None:
        input_body = "<html><body><h1>No paragraphs here</h1></body></html>"
        actual = get_first_paragraph_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)


class TestGetUrls(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com"]
        self.assertEqual(actual, expected)
    
    def test_get_urls_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="/path_test"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/path_test"]
        self.assertEqual(actual, expected)
    
    def test_get_urls_from_html_multiple_urls(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a><a href="/path_test"><span>relative bootdev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com", "https://crawler-test.com/path_test"]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
