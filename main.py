import os
from pathlib import Path

LINE = "My fridge has one job, yet the leftovers in the back have formed a civilization older than my career."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
