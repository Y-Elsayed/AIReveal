# AIReveal

**AIReveal** is an AI-generated text detector designed to identify instances of plagiarism and fake news. The model leverages a RoBERTa-based architecture fine-tuned on the [MAGE dataset](https://huggingface.co/datasets/yaful/MAGE), making it well-suited for distinguishing between human-written and AI-generated text.

## Performance

- **Accuracy:** 93.3%
- **AUROC:** 98%

AIReveal was developed using a custom trainer rather than the standard Transformers trainer, as part of the NLP class CSCI 5541 at the [University of Minnesota Twin Cities](https://twin-cities.umn.edu/) under the guidance of [Professor James Mooney](https://cs.umn.edu/people/faculty/mooney-james). While the model performs relatively well compared to other approaches in the field, it does encounter challenges with text that is paraphrased—whether by humans or by AI tools.

## Future Work

Planned improvements include:
- Experimenting with different hyperparameters and optimization techniques.
- Incorporating dropout layers to reduce overfitting.
- Expanding the dataset with additional paraphrased examples to better handle nuanced text variations.
- Exploring alternative model architectures and training strategies.

## Installation and Usage

To get started with AIReveal:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Y-Elsayed/AIReveal.git

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Run the fine-tuning notebook:**

   Open and run the `fine_tuning.ipynb` file. The model was trained on a local machine using CUDA 11.8 with an NVIDIA GEFORCE RTX 4070 (12GB VRAM).

## **Contributions & Suggestions**
I am open to contributions and suggestions. Enjoy exploring AIReveal and its capabilities in detecting AI-generated text! (please don't check if this readme is AI generated ;`)
