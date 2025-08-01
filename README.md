# 🧩 Word Search Puzzle Solver

This project is a **Word Search Puzzle Solver** that uses **OCR (Optical Character Recognition)** and **image processing** to detect letters from a word search puzzle image, find given words within the grid, and highlight them directly on the image.

---

## 🧠 Overview

* Takes an image of a word search puzzle.
* Uses `pytesseract` to extract letters from the grid.
* Searches for predefined words in 8 possible directions (horizontal, vertical, diagonal).
* Highlights the found words with colored rectangles.
* Displays the result visually using `matplotlib`.

---

## 📸 Example Input

* Input: `img.jpeg` — an image of a word search puzzle.
* Output: The same image with rectangles drawn over the found words.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Pytesseract (OCR)
* NumPy
* Matplotlib

---

## 📁 Project Structure

```
.
├── img.jpeg                       # Input image with word search puzzle
├── main.py                        # Main execution script (code shown above)
├── teste_encontra_letras.py      # Module to extract letters from the image
├── teste_encontra_palavras.py    # Module to extract the list of words to search
```

---

## 🔍 How It Works

1. **Letter Extraction:**

   * `encontra_letras()` processes the image and returns a matrix of detected characters.

2. **Word List Extraction:**

   * `encontra_palavras()` returns a list of words to be found in the grid.

3. **Word Search Algorithm:**

   * Searches for each word in 8 directions.
   * If found, stores the letter positions.

4. **Highlighting:**

   * Draws rectangles over each letter of the found words using unique colors.

---

## 🚀 Getting Started

### Requirements

Install the required libraries:

```bash
pip install opencv-python pytesseract matplotlib numpy
```

You also need to have **Tesseract-OCR** installed and accessible in your system path.
👉 [Installation guide here](https://github.com/tesseract-ocr/tesseract)

---

### Run the Script

```bash
python main.py
```

Make sure `img.jpeg`, `teste_encontra_letras.py`, and `teste_encontra_palavras.py` are in the same directory.

---

## ✅ Sample Output

For each word in the list, the console will print:

```
PALAVRA1: Encontrada
PALAVRA2: Nao encontrada
...
```

And a visual image will pop up with the found words highlighted.

---

## 📌 Notes

* The image must be a clear and straight-on capture of a word search puzzle.
* The OCR might require tuning (e.g., preprocessing, grid size adjustment) for better accuracy.
* Colors are rotated for each word for better visibility.

---

## 📬 Future Improvements

* Improve OCR preprocessing for better accuracy.
* Allow user to upload an image and input words interactively.
* Export results as an image file instead of just displaying.

---

Let me know if you'd like me to generate this `README.md` as a file or include usage examples from your image!
