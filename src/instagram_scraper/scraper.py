"""Instagram scraping utilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Optional
import requests
import instaloader


@dataclass
class ContactInfo:
    """Public contact information for an Instagram user."""

    username: str
    phone_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class InstagramScraper:
    """Fetch followers and contact info from Instagram."""

    def __init__(self) -> None:
        self.loader = instaloader.Instaloader()

    def login(self, username: str, password: str) -> None:
        """Log in to Instagram using Instaloader."""
        self.loader.login(username, password)

    def _fetch_user_info(self, user_id: str) -> dict:
        """Call the mobile API for user info."""
        url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            return resp.json().get("user", {})
        except Exception:
            return {}

    def iter_contact_info(
        self, profile_name: str
    ) -> Generator[ContactInfo, None, None]:
        """Yield public contact info for followers of *profile_name*."""
        profile = instaloader.Profile.from_username(
            self.loader.context, profile_name
        )
        for follower in profile.get_followers():
            info = self._fetch_user_info(str(follower.userid))
            yield ContactInfo(
                username=follower.username,
                phone_number=(
                    info.get("public_phone_number")
                    or info.get("contact_phone_number")
                ),
                email=info.get("public_email"),
                address=info.get("address_street"),
            )
