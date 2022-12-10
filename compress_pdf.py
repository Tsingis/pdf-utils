from argparse import ArgumentParser
from PyPDF2 import PdfReader, PdfWriter


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="Input pdf file",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        required=False,
        type=str,
        default="Compressed.pdf",
        help="Compressed output pdf",
    )
    args = vars(parser.parse_args())
    input_pdf, output_pdf = args["input"], args["output"]
    try:
        compress_pdf(input_pdf, output_pdf)
    except Exception as ex:
        print(f"Error compressing pdf. {ex}")


def compress_pdf(input_pdf: str, output_pdf: str):
    print(f"""Compressing pdf [{input_pdf}] to [{output_pdf}]""")
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)


if __name__ == "__main__":
    main()
