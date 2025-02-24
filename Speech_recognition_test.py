import random
import speech_recognition as sr
import difflib

# Hàm nhận diện giọng nói
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Đang lắng nghe... Hãy đọc dòng chữ xuất hiện trên màn hình:")
        try:
            audio = recognizer.listen(source)

            print("Đang xử lý...")
            text = recognizer.recognize_google(audio, language="en-US")  # Đặt ngôn ngữ
            print("Bạn vừa nói: ", text)
            return text

        except sr.UnknownValueError:
            print("Không thể nhận dạng được giọng nói.")
            return None
        except sr.RequestError as e:
            print(f"Không thể kết nối đến dịch vụ: {e}")
            return None

# Hàm in ngẫu nhiên một câu
def print_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Life is what happens when you're busy making other plans.",
        "To be or not to be, that is the question.",
        "Success is not final, failure is not fatal.",
        "Do what you can, with what you have, where you are.",
        "Happiness depends upon ourselves."
    ]
    return random.choice(sentences)

# Hàm so sánh hai chuỗi và tô màu đỏ phần khác biệt
def highlight_differences(original, spoken):
    original_words = original.split()
    spoken_words = spoken.split()

    highlighted_text = []

    for word in difflib.ndiff(original_words, spoken_words):
        if word.startswith("- "):  # Từ bị thiếu hoặc sai
            highlighted_text.append(f"\033[91m{word[2:]}\033[0m")  # Tô đỏ
        elif word.startswith("+ "):  # Từ bị thêm vào
            highlighted_text.append(f"\033[92m{word[2:]}\033[0m")  # Tô xanh lá
        else:
            highlighted_text.append(word[2:])  # Giữ nguyên

    return " ".join(highlighted_text)

if __name__ == "__main__":
    # In câu ngẫu nhiên
    sentence = print_random_sentence()
    print(f"Câu cần đọc: {sentence}")

    # Nhận diện giọng nói
    spoken_text = speech_to_text()

    if spoken_text:
        # So sánh và hiển thị sự khác biệt
        result = highlight_differences(sentence, spoken_text)
        print(f"Kết quả so sánh: {result}")
