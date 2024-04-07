import pandas as pd
import google.generativeai as genai

class Gemini:
    def __init__(self):
        API_KEY = "AIzaSyDKn_4sQ6n3HcyCmvx_Gmr-2q9FXsYFscA"
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.context = ""

    def set_context(self, context):
        print("Set context for model!")
        self.context = context

    def check_correctness(self, raw_output):
        bad_words = ["missing", "N/A", "not provided", "**", "Not specified", ":"]
        lines = raw_output.split("\n")
        for l in lines:
            if l[:2] != "- ":
                return False
            if any([bd_wrd in l for bd_wrd in bad_words]):
                return False
        return True

    def generate(self, text):
        legal_output = False
        while not legal_output:
            raw_result = self.model.generate_content(self.context + text)
            try:
                text = raw_result._result.candidates[0].content.parts[0].text
                print(text)
            except Exception:
                text = "- Error"
            legal_output = self.check_correctness(text)
        return text

model = Gemini()
bad_words = ["missing", "N/A", "not provided", "**"]
def check_correctness(raw_output):
    lines = raw_output.split("\n")
    for l in lines:
        if l[:2] != "- ":
            return False
        if any([bd_wrd in l for bd_wrd in bad_words]):
            return False
    return True

job_words = ["Requirements", "Qualifications"]
def has_job_thing(desc):
    if isinstance(desc, float):
        return False

    return any(word.lower() in ss.lower() for word in job_words for ss in desc.split("\n"))



context = """Given a job requirement text, return a Python list containing the listed requirements for the job. Be concise and abstract, listing software names individually. Ignore generic mentions of computer applications like Microsoft Office or CRM. List degree of applicability, avoid using "and" and other stop words, DONT use the words proficiency, ability or **knowledge**
"""
model.set_context(context)


df = pd.read_csv("job_id_summary.csv")


def generate_requirements(requir):
    response = model.generate(requir)
    return [r[2:]for r in response.split("\n")]


n, step = len(df), 20
jumps = list(range(0, n, step)) + [n]
for i, jump in enumerate(jumps):
    if i == 0: continue
    print(f'batch [{i}/{len(jumps)}] range {jumps[i-1]}-{jump}')
    tmp_df = df.iloc[jumps[i-1]:jump]
    tmp_df.loc[:, "clean_requirements"] = tmp_df["requirements"].apply(lambda x: generate_requirements(x))
    tmp_df.to_csv("requirements.csv", index=False, mode="a", header=(i == 1))