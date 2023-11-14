import random


class OTPGeneration:
    @staticmethod
    def generate_otp():
        otp_code = []
        for _ in range(6):
            otp_code.append(str(random.randint(0, 9)))

        random.shuffle(otp_code)
        return "".join(otp_code)
