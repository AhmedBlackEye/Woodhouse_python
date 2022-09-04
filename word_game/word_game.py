import random, sqlite3, re

class WordGame():
    def __init__(self):
        self.used_indexes = []
        self.possible_ans = []
        self.output_msg = ""
        self.score = 0
    
    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(f"file:{db_file}?mode=ro", uri=True)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    def fetch_row(self, index, conn):
        c = conn.cursor()
        c.execute(f"SELECT * FROM dictionary WHERE INTEGER={index}")
        row = c.fetchone()
        conn.commit()
        return row
    
    def get_random(self):
        index, index_2 = random.randint(1, 5494), random.randint(1, 5494)
        word_type = random.choice([2, 3]) #2 is the synonym's list's index while 3 is antonym's
        if index in self.used_indexes:
            return self.get_random()
        else: 
            self.used_indexes += [index, index_2]
            return [index, index_2, word_type]

    def usr_chat(self, count, sentence_1, sentence_2):
        msg = f"{count}. {sentence_1[0]} is to {sentence_1[1]}, as {sentence_2[0]} is to "
        ans = input("\n" + msg)
        for word in self.possible_ans:
            if ans.lower().strip() == self.clean(word).lower().strip():
                self.score += 1
                return
        self.output_msg += msg + sentence_2[1] + '\n'

    def extract_words(self, row, type_index=2):
        words_list = row[type_index].split(',')
        key_word = self.clean(row[1])
        chosen_word = random.choice(words_list)
        while '{' in chosen_word: chosen_word = random.choice(words_list)
        ans_word = self.clean(chosen_word)
        self.possible_ans = words_list
        return [key_word, ans_word]
        
    def clean(self, word):
        word = re.sub("[\[\\\].*?[\]\\\]", "", str(word))
        word = word.replace('.', '').strip()
        return word

    def run(self):
        conn = self.create_connection('words_db.db')
        rounds = 3
        for count in range(1,rounds+1):
            random_values = self.get_random()
            row_1 =  self.fetch_row(random_values[0], conn)
            row_2 = self.fetch_row(random_values[1], conn)
            sentence_1 = self.extract_words(row_1, random_values[2])
            sentence_2 = self.extract_words(row_2, random_values[2])
            self.usr_chat(count, sentence_1, sentence_2)
        print(f"\n***Your Score:\t{self.score/rounds*100:.2f}%\n\n***Corrections:\n{self.output_msg}")
        conn.close()

if __name__ == "__main__" :
    WordGame().run()