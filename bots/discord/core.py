class DiscordBot:
    @staticmethod
    def start():
        """디스코드 봇을 초기화"""
        print("DiscordBot.start() called")

    @staticmethod
    def run():
        """디스코드 봇을 실행"""
        print("DiscordBot.run() called")

    @staticmethod
    def create_invite():
        """초대 코드를 생성"""
        print("create_invite() called")
        return "https://discord.gg/dummy-invite-code"

    @staticmethod
    def send_message(channel_id, content):
        """특정 채널에 문자열 메시지 전송"""
        print(f"send_message() called: channel={channel_id}, content={content}")

    @staticmethod
    def grant_admin(user_id):
        """특정 유저에게 관리자 권한 부여"""
        print(f"grant_admin() called: user={user_id}")

    @staticmethod
    def grant_exec(user_id):
        """특정 유저에게 회장단 권한을 부여. add_role"""
        print(f"grant_exec() called: user={user_id}")

    @staticmethod
    def add_role(user_id, role_name):
        """특정 유저에게 새 역할을 부여"""
        print(f"add_role() called: user={user_id}, role={role_name}")

    @staticmethod
    def remove_from_role(user_id, role_name):
        """특정 역할에서 특정 유저를 제외"""
        print(f"remove_from_role() called: user={user_id}, role={role_name}")

    @staticmethod
    def create_sig(sig_name, member_list):
        """구성원 리스트를 기반으로 새로운 시그를 생성하고 = 채널을 만든다다"""
        print(f"create_sig() called: sig={sig_name}, members={member_list}")

    @staticmethod
    def archive_sig(sig_name):
        """특정 시그를 아카이브 처리하고 관련 채널을 이동시킵니다."""
        print(f"archive_sig() called: sig={sig_name}")
