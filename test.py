from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BundlingPohon:
    def __init__(self, driver):
        self.driver = driver

    def pilih_bundling(self, jumlah_pohon):
        """ Memilih bundling pohon berdasarkan jumlah yang diinginkan """
        xpath = f"//button[@class='bundling' and @data-value='{jumlah_pohon}']"

        # Tunggu hingga tombol bisa diklik
        bundling_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Scroll ke tombol agar terlihat
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bundling_button)
        time.sleep(1)  # Beri jeda

        # Klik tombol
        bundling_button.click()

def run_test():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()

    # Buka halaman
    driver.get("https://pedulimangrove.vercel.app/index.html")
    driver.maximize_window()

    # login admin
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class= 'admin']"))
    )
    login_button.click()

    # isi username dan password
    username_input = driver.find_element(By.XPATH, "//input[@id= 'email']")
    password_input = driver.find_element(By.XPATH, "//input[@id= 'password']")
    username_input.send_keys("siddiq@gmail.com")
    password_input.send_keys("123123")

    # klik tombol login
    login_button = driver.find_element(By.XPATH, "//input[@type= 'submit']")
    login_button.click()

    time.sleep(5)

    # Kembali ke halaman utama
    driver.get("https://pedulimangrove.vercel.app/index.html")  

    # Tunggu hingga tombol "Donasi Sekarang" bisa diklik
    donasi_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='data-relawan']"))
    )
    donasi_button.click()
    time.sleep(4)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='popup-form-donasi']"))
    )

    # 🔹 Pilih paket donasi dengan class `BundlingPohon` 1,5,10,50
    bundling = BundlingPohon(driver)
    bundling.pilih_bundling(1)  # Pilih bundling 10 pohon

    # Isi Nama
    nama_input = driver.find_element(By.XPATH, "//input[@id='dns-nama']")
    nama_input.send_keys("Test 1")

    # Tunggu checkbox muncul dan bisa diklik
    checkbox_anonim = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='anonim']"))
    )

    # Scroll ke elemen agar terlihat di layar
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox_anonim)
    time.sleep(1)  # Beri jeda agar scroll selesai

    # Klik checkbox
    # checkbox_anonim.click()

    # Masukkan Komentar
    komentar_input = driver.find_element(By.XPATH, "//textarea[@id='dns-komentar']")
    komentar_input.send_keys("Semoga pohon ini bermanfaat bagi lingkungan.")

    # Klik tombol "Donasi Sekarang"
    submit_button = driver.find_element(By.XPATH, "//button[@class='btn-submit']")
    submit_button.click()

    # Klik tombol konfirmasi "Iya"
    button_iya = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-iya']"))
    )
    time.sleep(3)
    button_iya.click()
    time.sleep(7)

    # Mengisi Formulir Informasi
    # Tunggu elemen formulir informasi muncul
    informasi_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@id='form-informasi']"))
    )

    # Scroll hingga formulir terlihat
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", informasi_form)
    time.sleep(2)  # Beri jeda agar scroll selesai

    # Isi formulir informasi
    input_nama = driver.find_element(By.XPATH, "//input[@id='info-nama']")
    input_nama.send_keys("Nama Donatur")

    input_email = driver.find_element(By.XPATH, "//input[@id='info-email']")
    input_email.send_keys("email@example.com")

    # Klik tombol "Salurkan Informasi"
    button_salurkaninformasi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-informasi']"))
    )
    button_salurkaninformasi.click()

    # Tunggu input sebelum menutup (Opsional)
    input("Tekan Enter untuk menutup browser...")
    driver.quit()
