import os
from pathlib import Path

LINE = "Dear fridge: you have one job, but the yogurt in the back has survived three managers, two reorganizations, and my entire character arc."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
