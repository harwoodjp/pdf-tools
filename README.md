Optimize PDFs for web and search
  * Convenient API for Ghostscript and Tesseract operations

Setup
* `pip install -r requirements.txt`
* Install [Tesseract]() 
* Install [Ghostscript]() 

Usage
* `app.py extract INPUT_FILE OUTPUT_DIR`
* `app.py split INPUT_FILE OUTPUT_DIR`
* `app.py compress INPUT_FILE OUTPUT_DIR`
* `app.py ocr INPUT_FILE OUTPUT_FILE`

Examples
* `python app.py extract test.PDF test/text`
* `python app.py split test.PDF test/images`
* `python app.py compress test.PDF test_compressed.PDF`
* `python app.py ocr test.PDF test_ocr.PDF`

Functions
* `extract`
  * Paginates and writes text from INPUT_FILE to OUTPUT_DIR
* `split`
  * Paginates and writes PNGs from INPUT_FILE to OUTPUT_DIR
* `compress`
  * Compresses INPUT_FILE PDF and writes OUTPUT_FILE
* `ocr`
  * Generates text mapping for INPUT_FILE and writes out to OUTPUT_FILE

Recipes
* When preparing a PDF for the web, the following sequences are recommended:
* `INPUT_FILE` -> `ocr` -> `OUTPUT_FILE` -> `extract`
  * Creates OCR mapping for `INPUT_FILE` and extracts `.txt` files from `OUTPUT_FILE`
* `INPUT_FILE` -> `compress` -> `OUTPUT_FILE` -> `split`
  * Compresses `INPUT_FILE` and splits `OUTPUT_FILE` into web-ready PNGs
