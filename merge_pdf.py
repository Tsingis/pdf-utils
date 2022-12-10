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


def merge_pdfs(input_pdfs: list[str], output_pdf: str):
    print(f"""Merging pdfs [{", ".join(input_pdfs)}] to [{output_pdf}]""")
    merger = PdfFileMerger()
    for pdf in input_pdfs:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()


if __name__ == "__main__":
    main()
