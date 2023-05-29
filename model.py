# Import necessary libraries and modules
from transformers import pipeline

# Create a translation pipeline for a specific language pair
def create_translation_pipeline(language_pair):
    model_name = f'Helsinki-NLP/opus-mt-en-{language_pair}'
    translation_pipeline = pipeline(model=model_name)
    return translation_pipeline

# Translate English to a specified language
def translate_text(text, language_pair):
    translation_pipeline = create_translation_pipeline(language_pair)
    results = translation_pipeline(text)
    return results[0]['translation_text']

# Translation function for English to Spanish
def en_to_es(text):
    return translate_text(text, 'es')

# Translation function for English to French
def en_to_fr(text):
    return translate_text(text, 'fr')

# Translation function for English to German
def en_to_de(text):
    return translate_text(text, 'de')

# Translation function for English to Chinese
def en_to_zh(text):
    return translate_text(text, 'zh')

# Translation function for English to Russian
def en_to_ru(text):
    return translate_text(text, 'ru')

# Translation function for English to Arabic
def en_to_ar(text):
    return translate_text(text, 'ar')

# Translation function for English to Japanese
def en_to_ja(text):
    return translate_text(text, 'jap')

# Translation function for English to Indonesian
def en_to_id(text):
    return translate_text(text, 'id')

# Translation function for English to Urdu
def en_to_ur(text):
    return translate_text(text, 'ur')

# Translation function for English to Hindi
def en_to_hi(text):
    return translate_text(text, 'hi')
