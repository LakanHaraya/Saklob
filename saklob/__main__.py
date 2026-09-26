import argparse

from saklob.ui.terminal import Terminal
from saklob.wika.setting import DEFAULT_LOCALE


def main():
    parser = argparse.ArgumentParser(
        prog="saklob",
        description="Saklob command-line shell"
    )

    parser.add_argument(
        "--locale",
        choices=[
            "filipino",
            "english",
            "cebuano",
        ],
        default=DEFAULT_LOCALE,
        help="Piliin ang wika ng Saklob."
    )

    args = parser.parse_args()

    terminal = Terminal(locale=args.locale)
    terminal.run()


if __name__ == "__main__":
    main()