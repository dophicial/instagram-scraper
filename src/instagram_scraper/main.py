"""CLI entry point for the Instagram scraper software."""

from __future__ import annotations

import argparse

from .scraper import InstagramScraper


def main(args: list[str] | None = None) -> None:
    """Run the Instagram scraper command line interface."""
    parser = argparse.ArgumentParser(
        description="Fetch public contact information from Instagram."
    )
    parser.add_argument("profile", nargs="?", help="Target profile username")
    parser.add_argument("--username", help="Instagram login username")
    parser.add_argument("--password", help="Instagram login password")
    ns = parser.parse_args(args or [])

    if ns.profile is None:
        # Preserve behaviour for unit tests when no arguments are supplied.
        print("Instagram scraper project skeleton.")
        return

    scraper = InstagramScraper()
    if ns.username and ns.password:
        scraper.login(ns.username, ns.password)

    for contact in scraper.iter_contact_info(ns.profile):
        print(contact)


if __name__ == "__main__":
    main()
