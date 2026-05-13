import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# 1. Veriyi Yükleme ve Sütun İsimlerini Otomatik Düzeltme
# sep=None olası noktalı virgül/virgül ayrımı sorununu otomatik çözer.
df = pd.read_csv("forestfires.csv", sep=None, engine="python")

# Sütun isimlerinin başındaki/sonundaki boşlukları temizler ve hepsini küçük harfe çevirir.
# Böylece dosyada 'Wind', ' WIND ' veya 'WIND' yazsa bile 'wind' olarak sorunsuz algılanır.
df.columns = df.columns.str.strip().str.lower()

# 2. Değişkenleri Belirleme
X = df["wind"]
Y = df["temp"]

# 3. Modeli Kurma ve Eğitme (Sabit terim ekleyerek: Y = aX + b + e)
X_model = sm.add_constant(X)
model = sm.OLS(Y, X_model).fit()

# Analiz Özet Tablosunu Yazdırma
print("--- REGRESYON ANALİZİ ÖZET TABLOSU ---")
print(model.summary())

# Word Raporuna Kolayca Geçirmek İçin Özel Değerleri Çekip Yazdırma
a_katsayisi = model.params["wind"]
b_sabiti = model.params["const"]
t_degeri = model.tvalues["wind"]
p_degeri = model.pvalues["wind"]
r2_degeri = model.rsquared

print("\n--- WORD RAPORU İÇİN KULLANILACAK ÖZEL DEĞERLER ---")
print(f"Denklem: Y = {a_katsayisi:.4f} * X + {b_sabiti:.4f}")
print(f"Eğim Katsayısı (a - wind): {a_katsayisi:.4f}")
print(f"Sabit Terim (b - const): {b_sabiti:.4f}")
print(f"t-değeri (wind): {t_degeri:.4f}")
print(f"p-değeri (wind): {p_degeri:.4f}")
print(f"R-kare (R^2): {r2_degeri:.4f}")

# 4. Saçılım Grafiği ve Regresyon Doğrusunun Çizdirilmesi
y_pred = model.predict(X_model)

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="dodgerblue", alpha=0.6, label="Gözlem Noktaları (Veri)")
plt.plot(X, y_pred, color="red", linewidth=2, label="Regresyon Doğrusu")

plt.title("Rüzgar Hızı ve Sıcaklık İlişkisi (Regresyon Analizi)")
plt.xlabel("Rüzgar Hızı - wind (km/h)")
plt.ylabel("Sıcaklık - temp (°C)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Grafiği Word'e eklemek için kaydetme ve ekranda gösterme
plt.savefig("regresyon_grafigi.png", dpi=300)
print("\nGrafik başarıyla 'regresyon_grafigi.png' adıyla kaydedildi.")
plt.show()