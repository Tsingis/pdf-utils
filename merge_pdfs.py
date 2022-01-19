from argparse import ArgumentParser
from PyPDF2 import PdfFileMerger


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--inputs",
        nargs="+",
        required=True,
        type=str,
        help="List of input pdf files",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        required=False,
        type=str,
        default="Merged.pdf",
        help="Merged output pdf",
    )
    args = vars(parser.parse_args())
    pdfs, output = args["inputs"], args["output"]
    try:
        merge_pdfs(pdfs, output)
    except Exception as ex:
        print(f"Error merging pdfs. {ex}")


def merge_pdfs(pdfs: list[str], output: str):
    print(f"""Merging pdfs [{", ".join(pdfs)}] to [{output}]""")
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(output)
    merger.close()


if __name__ == "__main__":
    main()
