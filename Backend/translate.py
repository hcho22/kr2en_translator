from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

def translate(text: str):
    model_name = "hcho22/opus-mt-ko-en-finetuned-kr-to-en"
    #model_name = "../model/" #if running local
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

    input_text = text
    tokenized = tokenizer([input_text], return_tensors='np')
    out = model.generate(**tokenized, max_length=128)

    with tokenizer.as_target_tokenizer():
        result = tokenizer.decode(out[0], skip_special_tokens = True)

    return result


