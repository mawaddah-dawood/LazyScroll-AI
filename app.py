import os
from ollama import Client

class LazyScrollAgent:
    def __init__(self):
        print("[*] Connecting to Local Ollama Inference Engine (Gemma 2)...")

        self.local_client = Client(host='http://localhost:11434')
        self.model_name = "gemma2:2b"  
        
        self.system_instruction = (
            "You are LazyScroll, the ultimate AI agent built to reward laziness. "
            "Your job is to read long, cluttered group chats or chaotic inboxes and "
            "condense them into an ultra-short, maximum 2-line summary. "
            "Focus only on action items or what actually matters. Keep it concise."
        )

    def generate_lazy_summary(self, raw_clutter: str) -> str:
        """معالجة النصوص الطويلة محلياً 100% بدون إنترنت"""
        try:
            response = self.local_client.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_instruction},
                    {"role": "user", "content": f"Summarize this chaotic text for a lazy user:\n{raw_clutter}"}
                ]
            )
            return response['message']['content']
        except Exception as e:
            print(f"[!] Ollama Connection Error: {e}")
            return "Error: Local inference engine is offline."

    def speak_to_lazy_user(self, text_summary: str):
        """نظام النطق الصوتي المحلي لبث الملخص مباشرة للسماعات دون حرق طاقة للنظر للشاشة"""
        print(f"\n🔊 Vocalizing the 2-line summary to your headphones...")
        
        clean_text = text_summary.replace("*", "").replace("\n", " ").replace("'", "").replace('"', "")
        
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(clean_text)
        except Exception:
            os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{clean_text}\')"')

    def process_sloth_mode(self, raw_text_input: str):
        print(f"\n📥 [Ingesting Chaotic Long Text Logs]...")
        summary = self.generate_lazy_summary(raw_text_input)
        print(f"\n🧠 [Gemma 2 Lazy Summary Output]:\n{summary}")
        self.speak_to_lazy_user(summary)

if __name__ == "__main__":
    print("==================================================")
    print("🦥 LazyScroll: Local AI Sloth-Mode Engine Active 🦥")
    print("==================================================")
    
    agent = LazyScrollAgent()
    
    chaotic_chat_logs = """
    John: Hey everyone, we need to talk about the project. I think the colors are wrong.
    Sarah: No, the colors are fine, but the logo is too small. Can someone fix it?
    Mike: I am away from my laptop right now, but I can check tonight.
    John: Also, don't forget we have a deadline tomorrow at 5 PM! We must submit the repo.
    Sarah: Wait, is it 5 PM or 9 PM?
    David: It is 5 PM. And someone needs to write the documentation or we will fail.
    Sarah: Okay, I will write the documentation after lunch. Mike, you fix the logo size.
    John: Perfect, so the final submission is on Sarah and Mike. I will just rest now.
    """
    
    agent.process_sloth_mode(chaotic_chat_logs)
