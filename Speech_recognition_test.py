import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Đang lắng nghe... Hãy nói điều gì đó:")
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

if __name__ == "__main__":
    speech_to_text()