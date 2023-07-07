from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
from better_profanity import profanity
import random
import warnings
warnings.filterwarnings("ignore")
fullPath  = 'C:/Users/avamc_srsebwe/OneDrive - University of Florida/projects/ig_post_compiler/text_generator/'
def generate(times, saveFile):
    model_list = []
    models_path = fullPath + 'model_list.txt'
    
    prompt_list = []
    prompt_path = fullPath + 'prompts.txt'
    
    saveFile = fullPath + saveFile
    
    with open(models_path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            model_list.append(line.replace('\n', ''))
            
    with open(prompt_path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            prompt_list.append(line.replace('\n', ' '))
            
    batch = ""
    for i in range(0, times):
        model_num = random.randint(0,len(model_list)-1)
        prompt_num = random.randint(0,len(prompt_list)-1)
        prompt_length = random.randint(10, 100)
        
        #print("Prompt was generated using model: " + model_list[model_num])
        tokenizer = AutoTokenizer.from_pretrained(fullPath + model_list[model_num])
        model = AutoModelWithLMHead.from_pretrained(fullPath + model_list[model_num])

        text_generator = pipeline(
            'text-generation', 
            model=model, 
            tokenizer=tokenizer,
            do_sample = True
            )
        
        gen_text = text_generator(
            prompt_list[prompt_num], 
            no_repeat_ngram_size=3, 
            repetition_penalty=2.2, 
            max_new_tokens=prompt_length)

        censored_text = profanity.censor(gen_text[0]['generated_text'], '<3 ')
        batch += censored_text + '\n'
    with open(saveFile, 'w', encoding = 'utf-8') as f:
        f.write(batch)
        
    # censor specific words from textfile
    # if __name__ == "__main__":
    #     profanity.load_censor_words_from_file('/path/to/my/project/my_wordlist.txt')

    #print(censored_text)
