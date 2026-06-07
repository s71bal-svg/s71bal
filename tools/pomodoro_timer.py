import time
from datetime import datetime

class PomodoroTimer:
    """ポモドーロタイマー"""
    
    def __init__(self, work_minutes=25, break_minutes=5, sessions=4):
        """
        初期化
        
        Args:
            work_minutes: 作業時間（分）
            break_minutes: 休憩時間（分）
            sessions: セッション数
        """
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes
        self.sessions = sessions
        self.current_session = 0
    
    def format_time(self, seconds):
        """秒を MM:SS 形式に変換"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"
    
    def countdown(self, seconds, label):
        """カウントダウン表示"""
        print(f"\n{'='*40}")
        print(f"📍 {label}")
        print(f"{'='*40}\n")
        
        while seconds > 0:
            print(f"\r⏱️  残り時間: {self.format_time(seconds)}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        
        print(f"\r⏱️  残り時間: {self.format_time(0)}  ✅ 完了！\n")
    
    def start(self):
        """タイマー開始"""
        print("\n🍅 ポモドーロタイマーを開始します")
        print(f"📊 設定: 作業{self.work_minutes}分 × 休憩{self.break_minutes}分 × {self.sessions}セッション\n")
        
        for session in range(1, self.sessions + 1):
            self.current_session = session
            
            # 作業時間
            work_seconds = self.work_minutes * 60
            self.countdown(work_seconds, f"セッション {session}/{self.sessions} - 作業中 💪")
            
            # 最後のセッション以外は休憩
            if session < self.sessions:
                break_seconds = self.break_minutes * 60
                self.countdown(break_seconds, f"休憩時間 ☕")
            else:
                print("🎉 すべてのセッションが完了しました！お疲れ様でした！\n")


# 使用例
if __name__ == "__main__":
    # デフォルト設定で開始（25分作業 × 5分休憩 × 4セッション）
    timer = PomodoroTimer()
    timer.start()
    
    # カスタム設定の例
    # timer = PomodoroTimer(work_minutes=20, break_minutes=3, sessions=6)
    # timer.start()
