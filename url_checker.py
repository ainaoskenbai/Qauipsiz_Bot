import requests

def check_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return "✅ Бұл сілтеме қауіпсіз көрінеді"
        else:
            return "⚠️ Бұл сілтеме күмәнді болуы мүмкін"

    except Exception:
        return "🚨 Бұл сілтеме ашылмайды немесе қауіпті болуы мүмкін"