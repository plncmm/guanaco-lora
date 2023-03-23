
from peft import PeftModel
from transformers import LlamaForCausalLM, LlamaTokenizer, GenerationConfig

tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-13b-hf")
model = LlamaForCausalLM.from_pretrained(
    "decapoda-research/llama-13b-hf",
    load_in_8bit=True,
    device_map="auto",
)
model = PeftModel.from_pretrained(model, "plncmm/guanaco-lora-13b")

def generate_prompt(instruction, input=None):
    if input:
        return f"""Abajo está una instrucción que describe una tarea, en conjunto con una entrada que entrega mas contexto. Escribe una respuesta que complete adecuadamente lo pedido.

### Instrucción:
{instruction}

### Entrada:
{input}

### Respuesta:"""
    else:
        return f"""Abajo está una instrucción que describe una tarea. Escribe una respuesta que complete adecuadamente lo pedido.

### Instrucción:
{instruction}

### Respuesta:"""

generation_config = GenerationConfig(
    temperature=0.1,
    top_p=0.75,
    num_beams=4,
)

def evaluate(instruction, input=None):
    prompt = generate_prompt(instruction, input)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].cuda()
    generation_output = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=256
    )
    for s in generation_output.sequences:
        output = tokenizer.decode(s)
        print("Respuesta:", output.split("### Respuesta:")[1].strip())


if __name__ == "__main__":

    evaluate("nombre las capitales regionales de Chile")
    evaluate("dime sobre guanacos")
    evaluate("dime sobre el presidente de mexico en 2019")
    evaluate("dime sobre el rey de francia en 2019")
    evaluate("traduce la frase 'hola mundo' a inglés")
    evaluate("escribe un programa de Python que imprima los primeros 10 números de Fibonacci")
