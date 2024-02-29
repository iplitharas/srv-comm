#!/usr/bin/env python3
"""
Service A demo client.
"""

import argparse
import sys
from urllib.parse import urljoin

from loguru import logger

from src.services.srv_a import ServiceA, ServiceAException


def cli_parser():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Send multiple requests to ServiceB.")
    parser.add_argument(
        "max_requests",
        type=int,
        nargs="?",
        default=10,
        help="Maximum number of requests to send (default: 10)",
    )
    return parser.parse_args()


def main(max_requests: int = 10) -> None:
    """
    Stress test ServiceB by sending multiple requests.
    """
    total_ok = 0
    srv_a = ServiceA()
    for _ in range(max_requests):
        try:
            srv_a.send_message(urljoin("http://localhost:8000", "greet"), data={"message": "hi"})
            total_ok += 1
        except ServiceAException:
            logger.warning("Failed to send message, server is unavailable... ")

    logger.info(
        f"Total requests: #{max_requests}, " f"succeeded: {total_ok / max_requests * 100:.2f}%"
    )


if __name__ == "__main__":
    args = cli_parser()
    if max_requests := args.max_requests < 1:
        logger.error("Max requests must be greater than 0")
        sys.exit(1)
    main(args.max_requests)
