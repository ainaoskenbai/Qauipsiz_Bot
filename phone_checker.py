import phonenumbers

# Локальный blacklist для MVP
BLACKLIST = {
    "+77001234567",
    "+77777777777"
}

def check_phone(phone: str) -> str:
    try:
        parsed = phonenumbers.parse(phone, "KZ")

        if not phonenumbers.is_valid_number(parsed):
            return "❌ Нөмір форматы дұрыс емес"

        normalized = phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )

        if normalized in BLACKLIST:
            return "🚨 Бұл нөмір алаяқтар тізімінде бар"

        return "✅ Бұл нөмір бойынша қауіп табылмады"

    except Exception:
        return "⚠️ Нөмірді тексеру мүмкін болмады"