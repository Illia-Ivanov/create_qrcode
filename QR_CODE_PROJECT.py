import qrcode


def generate_qr_code(data,  # це дані про qr_code,тобто посилання або ще щось для qr-коду
                     file_name,  # тут створенна змінна для зберігання нашого qr-коду в певному форматі
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     # обробка рівня глибини помилки(в бібліотеці qrcode можна знайти більше корисної інформації про це)
                     box_size=12,  # розмір рамки в якій знаходиться QR-код
                     border=2  # товщина самого qr-коду
                     ):
    qr = qrcode.QRCode(error_correction=error_correction, box_size=box_size, border=border)  # вказуємо що за що відповідає,тобто обробку помилок,розмів qr-code та його кордони

    qr.add_data(data)  # зробили тут додавання об'єкту який ми зробили qr-кодом,тобто об'єкт qr

    qr.make(fit=True)  # тут ми генеруємо qr-код та вказуємо фіт щоб зазначити що він має вписуватися в розміри якім ми додали

    img = qr.make_image(fill_color='black', back_color='white')  # тут вказуємо що яким кольором буде заповнено наш qr-код,та на якому фоні він буде знаходитись
    img.save(file_name) # тут вказуємо що об'єкт img(змінна в якій ми вказали всі параметри кольору вище) зберігає через метод .save() наш файл,який ми вказуємо у функції


if __name__ == '__main__':
    generate_qr_code(

        'https://github.com/Ilya9312',  # вказуємо в це поле яке посилання буде встановлено в наший qr-code
        'qr_code.png'  # вказуємо назву файлу та його розширення(бажано .png/.jpg)

    )
