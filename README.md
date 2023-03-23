# Guanaco: A spanish finetuned instruction LLaMA

This repository is intended to share all the steps and resources that we used to finetune our version of LLaMA.

This model is designed for research use only, i.e., cannot be used for commercial purposes or entertainment.

# References

We started this section with this citation because everything we did was only possible due to the strong community and works that other people and groups did. For our work, we rely mainly in the works developed by: [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca Lora](https://github.com/tloen/alpaca-lora), [Cabrita](https://github.com/22-hours/cabrita), [Bertin](https://huggingface.co/bertin-project), [ChatGPT](https://openai.com/blog/chatgpt) and [Hugging Face](https://huggingface.co/). So, thank you all for the great work and open this to the world!

# Data

We used the [alpaca-spanish dataset](https://huggingface.co/datasets/bertin-project/alpaca-spanish), which is a traslation of [alpaca_data.json](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json).

# Finetuning 

To finetuned the LLaMA model we used the code available on [Alpaca Lora](https://github.com/tloen/alpaca-lora) (also in [Cabrita](https://github.com/22-hours/cabrita)), which provides code to finetune the LLaMA model using PEFT from Hugging Face. With this, we could run our finetuning step using 1 A100 on top of LLaMA-7B and LLaMa-13B. The code we used is available [here](guanaco-lora.py).

# Evaluate

You can test the model using the code available [here](guanaco-test.py).

# Examples
