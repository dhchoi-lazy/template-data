import logging
import requests
import random
import aiohttp


class BaseCrawler:
    """
    responsible for crawling the website. All requests should be handled here.
    It doesn't have logic for extracting data.
    """

    def __init__(
        self,
        **kwargs,
    ):
        self.base_url = kwargs.get("base_url")
        self.params = kwargs.get("params")
        self.output_dir = kwargs.get("output_dir")

        self.user_agent = kwargs.get("user_agent", self.get_random_user_agent())
        self.rate_limit = kwargs.get("rate_limit", 1)
        self.retries = kwargs.get("retries", 8)
        self.backoff_factor = kwargs.get("backoff_factor", 2)
        self.session = self.create_session()

        self._async_session = None

        self.kwargs = kwargs

        self.logger = logging.getLogger(self.__class__.__name__)

    def create_session(self):
        session = requests.Session()
        session.headers.update({"User-Agent": self.get_random_user_agent()})
        return session

    async def get_async_session(self):
        """Get or create an async session as needed within an async context"""
        if self._async_session is None or self._async_session.closed:
            self._async_session = aiohttp.ClientSession(
                headers={"User-Agent": self.get_random_user_agent()}
            )
        return self._async_session

    def get_random_user_agent(self):
        if not hasattr(self, "AGENT") or not self.AGENT:
            # Default agents if not defined in BaseCrawler
            self.AGENT = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            ]
        return random.choice(self.AGENT)

    def refresh_user_agent(self):
        if hasattr(self, "session"):
            self.session.headers.update({"User-Agent": self.get_random_user_agent()})

    def fetch_page(self, url):
        response = self.session.get(
            url,
            headers={
                "User-Agent": self.get_random_user_agent(),
            },
        )
        return response

    async def fetch_page_async(self, url):
        session = await self.get_async_session()
        async with session.get(
            url, headers={"User-Agent": self.get_random_user_agent()}
        ) as response:
            return await response.text()

    def crawl(self):
        pass

    async def close_async_session(self):
        """Close the async session if it exists"""
        if self._async_session and not self._async_session.closed:
            await self._async_session.close()
