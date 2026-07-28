Pembaharuan terakhir: 28/07/26


# Kumpulan Dataset Domain Indonesia
Repository ini merupakan kumpulan domain atau situs website dengan TLD maupun ccTLD di Indonesia.

# Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation
Metodologi: https://tranco-list.eu/methodology
List ID: 46ZYX (2026-07-27)
lines: 17752
```
$ curl -O -J -L https://tranco-list.eu/download/46ZYX/full
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '{print $2}' | grep '\.id$' > domains.txt

```

| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 7352              |
| 2  | .co.id      | 3613              |
| 3  | .ac.id      | 1820              |
| 4  | .my.id      | 1175              |
| 5  | .go.id      | 869               |
| 6  | .sch.id     | 830               |
| 7  | .web.id     | 742               |
| 8  | .biz.id     | 524               |
| 9  | .net.id     | 488               |
| 10 | .or.id      | 288               |
| 11 | .mil.id     | 15                |
| 12 | .desa.id    | 32                |
| 13 | .ponpes.id  | 4                 |
|   Total |        | 17752             |

# ipsniper
| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id         | 1437060           |
| 2  | .my.id      | 1087449           |
| 3  | .co.id      | 487379            |
| 4  | .web.id     | 379822            |
| 5  | .biz.id     | 325110            |
| 6  | .sch.id     | 219076            |
| 7  | .or.id      | 73578             |
| 8  | .desa.id    | 62458             |
| 9  | .ac.id      | 49829             |
| 10 | .go.id      | 13760             |
| 11 | .ponpes.id  | 5834              |
| 12 | .net.id     | 4978              |
| 13 | .mil.id     | 481               |
| 14 | .xn--9tfky.id | 41               |
| 15 | .kop.id     | 29                |
|  Total  |        | 4146884           |


### Sampel
```
stkipahsingaraja.ac.id
pn-pariaman.go.id
riso.id
korem082.mil.id
rumput.or.id
```

# Domains Project
Metodologi: https://github.com/tb0hdan/domains#crawlers  
Source: https://domainsproject.org/
lines: 2544669


| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 634337            |
| 2  | .co.id      | 639898            |
| 3  | .sch.id     | 261613            |
| 4  | .my.id      | 255054            |
| 5  | .ac.id      | 211097            |
| 6  | .net.id     | 162538            |
| 7  | .go.id      | 157951            |
| 8  | .web.id     | 111324            |
| 9  | .or.id      | 65497             |
| 10 | .desa.id    | 30332             |
| 11 | .biz.id     | 10370             |
| 12 | .ponpes.id  | 3451              |
| 13 | .mil.id     | 1207              |
|   Total |        | 2544669           |


### Sampel
```
backup.poltekim.ac.id
mx.cahayabarumulia.co.id
sdnegeri16bandarrahmad.sch.id
www.langitpayment.web.id
cpanel.globaltrade.co.id
```

# Common Crawl
Metodologi: https://github.com/commoncrawl/cc-host-index  
Crawl: CC-MAIN-2025-18 (April 2025)  
lines: 420735

Daftar *registered domain* unik ber-TLD `.id` yang berhasil dijangkau oleh crawler Common Crawl pada crawl tersebut. Domain diambil dari dataset publik **Host Index** (https://huggingface.co/datasets/commoncrawl/host-index-testing-v2) dengan memfilter `url_host_tld = 'id'`.


| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 210193            |
| 2  | .co.id      | 64543             |
| 3  | .my.id      | 57753             |
| 4  | .sch.id     | 25623             |
| 5  | .web.id     | 20675             |
| 6  | .desa.id    | 9151              |
| 7  | .or.id      | 8981              |
| 8  | .biz.id     | 8729              |
| 9  | .ac.id      | 8309              |
| 10 | .go.id      | 4699              |
| 11 | .net.id     | 1292              |
| 12 | .ponpes.id  | 557               |
| 13 | .mil.id     | 230               |
|   Total |        | 420735            |


### Sampel
```
stikes-muhammadiyahku.ac.id
tokoklungkung.biz.id
karyamandirikontraktor.id
staiypiqbaubau.ac.id
sdnpemotohbarat.sch.id
```

# Gabungan (latest.txt)
Gabungan semua dataset di atas, dinormalisasi (huruf kecil, tanpa `www.`, tanpa titik akhir) dan dideduplikasi. Setiap domain dicatat bersama jumlah sumber yang memuatnya.

| Sumber             | Domain unik |
|--------------------|-------------:|
| Tranco (full)      |      17,752 |
| Tranco (top-1M)    |       4,754 |
| ipsniper           |     885,939 |
| Domains Project    |   2,073,727 |
| Common Crawl       |     420,733 |
| **Union**          | **3,046,964** |


Sebaran jumlah sumber per domain:

| Sumber | Domain |
|--------|-------:|
| hanya 1 sumber | 2,791,371 |
| 2 sumber       |   167,212 |
| 3 sumber       |    79,365 |
| 4 sumber       |     6,065 |
| 5 sumber       |     2,951 |


| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 849654            |
| 2  | .co.id      | 612062            |
| 3  | .my.id      | 475917            |
| 4  | .sch.id     | 222892            |
| 5  | .web.id     | 197569            |
| 6  | .ac.id      | 181222            |
| 7  | .net.id     | 162865            |
| 8  | .go.id      | 132108            |
| 9  | .biz.id     | 109829            |
| 10 | .or.id      | 61134             |
| 11 | .desa.id    | 37038             |
| 12 | .ponpes.id  | 3586              |
| 13 | .mil.id     | 1083              |
| 14 | .kop.id     | 5                 |
|   Total |        | 3046964           |


Domain dengan jumlah subdomain `.id` terbanyak (di seluruh union, dikelompokkan per *registered domain*):

| No | Registered domain | Jumlah |
|----|-------------|-------------------|
| 1  | blogspot.co.id    | 120451            |
| 2  | cbn.net.id        | 82892             |
| 3  | indonetwork.co.id | 17275             |
| 4  | ipb.ac.id         | 13758             |
| 5  | three.co.id       | 12230             |
| 6  | fast.net.id       | 10800             |
| 7  | gunadarma.ac.id   | 8336              |
| 8  | ugm.ac.id         | 8077              |
| 9  | solnet.net.id     | 7943              |
| 10 | interlink.net.id  | 7516              |


File:
- `latest.txt` — union terurut ascending, satu domain per baris (~3.05 M baris).
- `combine.py` — skrip generator (Python 3, tanpa dependensi eksternal). Skrip ini juga bisa menulis `latest.csv` (jejak sumber) bila dihapus dari `.gitignore`.


# Sumber
https://domainsproject.org/

https://ipsniper.info/

https://commoncrawl.org/

# Cara mendapatkan data
Bagian ini menjelaskan langkah-langkah untuk mendapatkan atau memperbarui setiap dataset pada repositori ini.

## Tranco
Unduh list harian dari https://tranco-list.eu/latest_list, ambil kolom domain, lalu saring yang berakhiran `.id`. List ID berubah setiap hari — ganti `46ZYX` dengan ID terbaru.
```
$ curl -O -J -L https://tranco-list.eu/download/46ZYX/full
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '{print $2}' | grep '\.id$' > Tranco/domains.txt
```
Untuk subset top-1M (domain dengan peringkat ≤ 1.000.000):
```
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '$1<=1000000 && $2 ~ /\.id$/' | awk -F',' '{print $2}' | sort -u > Tranco/top-1m/domain.txt
```

## ipsniper
Unduh zonefile per TLD dari arsip publik ipsniper, lalu dekompresi.
```
$ mkdir -p ipsniper
$ for tld in ac biz co desa go kop mil my net or ponpes sch web xn--9tfky; do
>   curl -sL -o "ipsniper/$tld.id.txt.gz" \
>     "https://ipsniper.info/archive/latest/zonefiles/public/$tld.id.txt.gz"
> done
$ curl -sL -o ipsniper/id.txt.gz \
>   "https://ipsniper.info/archive/latest/zonefiles/public/id.txt.gz"
$ for f in ipsniper/*.gz; do gunzip -k "$f"; done
```
File `ipsniper/<tld>.id.txt` berformat zonefile: `domain\tIN\t<record>\t<value>` (A/AAAA/NS/CNAME).

## Domains Project
Sumber tidak menyediakan unduhan langsung per TLD; data .id tersedia sebagai satu shard `.xz` di mirror GitHub.
```
$ curl -sL -o "Domains Project/domain2multi-id00.txt.xz" \
>   "https://media.githubusercontent.com/media/tb0hdan/domains/master/data/indonesia/domain2multi-id00.txt.xz"
$ xz -dk "Domains Project/domain2multi-id00.txt.xz"
```
Untuk daftar lengkap TLD atau data negara lain: https://github.com/tb0hdan/domains (mirror `git lfs` + `./unpack.sh`). Versi raw di `https://dataset.domainsproject.org/` butuh autentikasi.

## Common Crawl
Data berasal dari dataset Host Index v2 (Parquet) di HuggingFace. Query dijalankan dengan DuckDB yang membaca Parquet lewat HTTP range — tidak perlu mengunduh seluruh dataset (~9 GB per crawl).
```
$ pip install duckdb
$ python3 - <<'EOF'
import duckdb
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
base = "https://huggingface.co/datasets/commoncrawl/host-index-testing-v2/resolve/main/data/crawl=CC-MAIN-2025-18"
files = [f"{base}/CC-MAIN-2025-18.part-{i:05d}.parquet" for i in range(30)]
con.execute(f"""
  COPY (
    SELECT DISTINCT url_host_registered_domain
    FROM read_parquet({files!r})
    WHERE url_host_tld = 'id'
    ORDER BY url_host_registered_domain
  ) TO 'commoncrawl/domain2multi-id.txt' (HEADER FALSE)
""")
EOF
```
Ganti `CC-MAIN-2025-18` dengan ID crawl terbaru dari https://commoncrawl.org/the-data/.

## Gabungan (latest.txt / latest.csv)
Setelah keempat dataset di atas diperbarui, jalankan `combine.py` untuk menghasilkan union yang dinormalisasi dan dideduplikasi.
```
$ python3 combine.py
```
Skrip membaca semua sumber, menulis `latest.txt` (union terurut) dan `latest.csv` (dengan jejak sumber), lalu mencetak ringkasan jumlah dan per-TLD ke stderr. Tidak butuh dependensi eksternal (hanya Python 3 standar).

## Pembaharuan
Pembaharuan mengikuti siklus rilis sumber:
- **Tranco** — harian (https://tranco-list.eu/latest_list)
- **ipsniper** — bulanan, biasanya awal bulan (https://ipsniper.info/)
- **Domains Project** — tidak terjadwal, beberapa bulan sekali
- **Common Crawl** — bulanan (https://commoncrawl.org/the-data/)