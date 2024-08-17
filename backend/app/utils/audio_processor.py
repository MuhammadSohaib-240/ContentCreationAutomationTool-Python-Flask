import os
from gtts import gTTS


class AudioProcessor:
    def __init__(self):
        self.sentences = []
        self.audio_files_count = 0

    def split_article_into_sentences(self, article):
        self.sentences = [sentence.strip() for sentence in article.replace("?", ".").split(".")]
        self.sentences = [sentence for sentence in self.sentences if sentence]
        self.audio_files_count = len(self.sentences)
        return self.sentences

    @staticmethod
    def create_audio_files(sentences, output_directory, additional_text=None):
        os.makedirs(output_directory, exist_ok=True)

        for i, sentence in enumerate(sentences):
            audio_output_path = os.path.join(output_directory, f"sentence{i + 1}.mp3")
            tts = gTTS(sentence, lang="en")
            tts.save(audio_output_path)

        # Process additional text
        if additional_text:
            additional_audio_output_path = os.path.join(output_directory, "output.mp3")
            additional_tts = gTTS(additional_text, lang="en")
            additional_tts.save(additional_audio_output_path)
