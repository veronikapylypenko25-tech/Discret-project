class Cheking:
    def __init__(self):
        self.passw = input("Введіть Ваш пароль: ")

    def if_dif_case(self) -> tuple[bool, int]:
        has_upper = any(c.isupper() for c in self.passw)
        has_lower = any(c.islower() for c in self.passw)
        result = has_upper and has_lower
        return result, (20 if result else 0)

    def if_len_ok(self, min_len: int) -> tuple[bool, int]:
        result = len(self.passw) > min_len
        return result, (40 if result else 0)

    def if_spec_sumbol(self) -> tuple[bool, int]:
        symbols = "_!&?"
        result = any(c in symbols for c in self.passw)
        return result, (25 if result else 0)

    def if_no_cyrrilic(self) -> tuple[bool, int]:
        def is_cyrillic(ch: str) -> bool:
            return '\u0400' <= ch <= '\u04FF'

        has_cyr = any(is_cyrillic(c) for c in self.passw)
        result = not has_cyr
        return result, (15 if result else 0)

    def check_security(self):
        case_ok, case_points = self.if_dif_case()
        len_ok, len_points = self.if_len_ok(8)
        spec_ok, spec_points = self.if_spec_sumbol()
        cyr_ok, cyr_points = self.if_no_cyrrilic()
        result_score = case_points + len_points + spec_points + cyr_points
        if result_score < 50:
            print("Такий пароль не можна використовувати, адже він слабкий!!!")
        else:
            print(f"Ваш пароль: {self.passw}")
            print(f"Оцінка надійності Вашого паролю: {result_score}/100")
checking_password = Cheking()
checking_password.check_security()
