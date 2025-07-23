import requests
import pandas as pd
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO ---
API_KEY = "9eafb37b220b7bc75c3e885ff0f92521"  # Certifique-se de que esta é a sua API Key correta e ativa
CIDADE = "Rio de Janeiro"

# Endpoint do OpenWeatherMap para previsão de 5 dias / 3 horas
URL_PREVISAO = "http://api.openweathermap.org/data/2.5/forecast"


# --- FUNÇÃO PARA PEGAR DADOS DE PREVISÃO ---
def get_forecast_data(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Para obter temperatura em Celsius
        "lang": "pt_br"  # Para respostas em português
    }
    try:
        response = requests.get(URL_PREVISAO, params=params)
        response.raise_for_status()  # Lança um erro para status de erro HTTP
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API de previsão: {e}")
        return None


# --- PROCESSAR E SALVAR DADOS DA PREVISÃO ---
print(f"Buscando previsão do clima para {CIDADE} (próximos 5 dias)...")
forecast_raw_data = get_forecast_data(CIDADE, API_KEY)

if forecast_raw_data and "list" in forecast_raw_data:
    all_weather_data = []
    processed_dates = set()  # Para garantir um registro por dia

    for item in forecast_raw_data["list"]:
        dt_object = datetime.fromtimestamp(item["dt"])
        date_str = dt_object.strftime("%Y-%m-%d")

        # Pegar um registro por dia (ex: o registro mais próximo do meio-dia, ou o primeiro do dia)
        # Para simplicidade, vamos pegar o primeiro registro que vemos para cada dia
        # e evitar duplicatas. Se precisar de lógica mais avançada (min/max), terá que iterar mais.
        if date_str not in processed_dates:
            weather_info = {
                "Cidade": CIDADE,
                "Data_Hora_Previsao": dt_object.strftime("%Y-%m-%d %H:%M:%S"),
                "Temperatura_Celsius": item["main"]["temp"],
                "Sensacao_Termica_Celsius": item["main"]["feels_like"],
                "Umidade_Porcentagem": item["main"]["humidity"],
                "Descricao_Clima": item["weather"][0]["description"],
                "Velocidade_Vento_m_s": item["wind"]["speed"]
            }
            all_weather_data.append(weather_info)
            processed_dates.add(date_str)

        # O OpenWeatherMap /forecast dá 40 registros (a cada 3 horas por 5 dias).
        # Se você quiser mais do que apenas um ponto por dia, você pode ajustar
        # a lógica acima para pegar, por exemplo, o ponto do meio-dia, ou
        # calcular a média/min/max para cada dia.

    if all_weather_data:
        df = pd.DataFrame(all_weather_data)

        # --- SALVAR EM PLANILHA ---
        file_name = "previsao_clima_5_dias.xlsx"
        try:
            df.to_excel(file_name, index=False)
            print(f"Previsão do clima salva com sucesso em '{file_name}'")
        except Exception as e:
            print(f"Erro ao salvar a planilha: {e}. Certifique-se que 'openpyxl' está instalado.")
    else:
        print("Nenhum dado de previsão foi processado.")
else:
    print("Não foi possível obter os dados de previsão do clima ou a resposta está vazia.")