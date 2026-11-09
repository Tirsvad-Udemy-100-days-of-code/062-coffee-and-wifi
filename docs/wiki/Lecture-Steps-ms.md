[English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Melayu**

# Langkah Pelajaran

Sembilan keperluan tugasan Hari ke-62. Setiap langkah mempunyai tangkapan skrin dan apa yang kita pelajari.

## Langkah 1: Halaman utama menggunakan `css/styles.css`

![Halaman utama yang digayakan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/01-home-page.png)

**Apa yang kita pelajari:** pewarisan templat. `base.html` memuatkan CSS Bootstrap-Flask dengan `bootstrap.load_css()` dan memaut `styles.css` kita dengan `url_for('static', filename=...)`; setiap halaman yang memperluaskannya mendapat rupa yang sama.

## Langkah 2: `/cafes` memaparkan jadual Bootstrap daripada CSV

![Jadual kafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/02-cafes-table.png)

**Apa yang kita pelajari:** membaca fail CSV dengan modul `csv`, menghantar baris ke templat dan mengulanginya dengan Jinja. Kelas Bootstrap `table table-dark table-striped table-hover` menggayakan jadual tanpa CSS tambahan.

## Langkah 3: Lokasi menjadi pautan "Maps Link"

![Lajur Maps Link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/03-maps-links.png)

**Apa yang kita pelajari:** satu peraturan kecil (nilai yang bermula dengan `http` ialah pautan) yang disimpan di satu tempat, supaya templat hanya menentukan cara paparan sel, bukan maksudnya.

## Langkah 4: "Show Me!" menuju ke halaman kafe

![Halaman kafe selepas menekan butang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/04-show-me-button.png)

**Apa yang kita pelajari:** `url_for('cafes')` membina pautan daripada nama fungsi, jadi laluan boleh bertukar tanpa merosakkan pautan.

## Langkah 5: Laluan rahsia `/add` memaparkan borang

![Borang tambah kafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/05-secret-add-form.png)

**Apa yang kita pelajari:** laluan yang tiada pautan kepadanya. `FlaskForm` Flask-WTF mengisytiharkan medan (medan teks dan `SelectField` untuk penilaian), dan `render_form` Bootstrap-Flask melukis seluruh borang dalam gaya Bootstrap.

## Langkah 6: Medan lokasi mengesahkan URL

![Ralat pengesahan URL](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/06-url-validation-error.png)

**Apa yang kita pelajari:** pengesah WTForms (`DataRequired`, `URL`). Pengesahan pelayar dimatikan dengan `novalidate`, jadi semakan pelayan dan mesejnya yang anda lihat. Borang memerlukan kunci rahsia untuk perlindungan CSRF; ia dibaca daripada persekitaran dan tidak pernah ditulis dalam kod.

## Langkah 7: Penghantaran yang sah menambah kafe

![Kafe baharu dalam jadual](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/07-cafe-added.png)

**Apa yang kita pelajari:** `validate_on_submit()` dan ubah hala selepas POST: selepas simpan berjaya, pelayar dihantar ke `/cafes`, jadi muat semula tidak menghantar borang dua kali.

## Langkah 8: Kafe ditambah pada `cafe-data.csv`

![Hujung fail CSV](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/08-csv-appended.png)

**Apa yang kita pelajari:** menambah dengan mod `"a"` dan `csv.writer`, yang meletakkan tanda petikan pada nama yang mengandungi koma. Pengendalian fail berada dalam kelas repositori di belakang antara muka, jadi kes guna boleh diuji tanpa fail.

## Langkah 9: Semua pautan navigasi berfungsi

![Halaman tambah dengan pautannya](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/raw/branch/main/docs/screenshots/09-navigation-links.png)

**Apa yang kita pelajari:** semua pautan dibina dengan `url_for`, dan ujian hujung-ke-hujung mengikuti setiap `href` pada halaman dan menyemak bahawa ia menjawab 200, jadi pautan rosak dikesan oleh ujian.
