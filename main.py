import os

EXCUSE = "The upload timed out, so I retried with exponential backoff, politely doubling my patience; your deadline, alas, ran a far stricter timeout."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
